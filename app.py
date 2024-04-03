from flask import Flask, render_template, request
import requests
from recomendacion import MovieRecommendationSystem
import csv

app = Flask(__name__)

# Crear sistema de recomendación y cargar datos de películas
movie_data = []
with open('movies_metadata.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie = {
            "title": row['original_title'],
            "description": row['overview'],
            "genres": row['genres'],
            "release_date": row['release_date']
        }
        movie_data.append(movie)

recommendation_system = MovieRecommendationSystem(movie_data)

@app.route('/')
def index():
    # Cargar películas de la API al inicializar la página de inicio
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": "9205d584155330aa711c4a723d7ca7a5",  # Reemplaza esto con tu propia clave de API de TMDb
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": "false",
        "include_video": "false",
        "page": "1"
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Obtener los resultados de la consulta
    movies = data.get('results', [])

    return render_template('index.html', movies=movies)


@app.route('/buscar', methods=['POST'])
def buscar_pelicula():
    busqueda = request.form['busqueda']
    if busqueda:
        # Hacer la solicitud a la API de TMDb para buscar películas
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "9205d584155330aa711c4a723d7ca7a5",  # Reemplaza esto con tu propia clave de API de TMDb
            "query": busqueda
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'results' in data:
            movies = data['results']
            return render_template('index.html', movies=movies)
        else:
            return render_template('index.html', message="No se encontraron resultados.")
    else:
        return render_template('index.html', message="Por favor ingrese un término de búsqueda.")


@app.route('/detalle/<title>')
def ver_detalle(title):
    # Hacer la solicitud a la API de TMDb para obtener detalles de la película
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "9205d584155330aa711c4a723d7ca7a5",  # Reemplaza esto con tu propia clave de API de TMDb
        "query": title
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'results' in data:
        movie = data['results'][0]  # Tomar la primera película coincidente
        # Obtener información relevante de la película
        description = movie.get('overview', '')
        release_date = movie.get('release_date', '')
        genres = ', '.join([genre['name'] for genre in movie.get('genres', [])])
        original_language = movie.get('original_language', '')
        title = movie.get('title', '')

        # Obtener películas similares
        similar_movies = recommendation_system.get_similar_movies(title)

        # Renderizar el template con la información obtenida
        return render_template('detalle.html', title=title, description=description,
                               release_date=release_date, genres=genres,
                               original_language=original_language, similar_movies=similar_movies)
    else:
        return render_template('detalle.html', title=title, message="No se encontraron detalles para esta película.")



if __name__ == '__main__':
    app.run(debug=True)
