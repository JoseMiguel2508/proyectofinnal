import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

class MovieRecommendationSystem:
    def __init__(self, movie_data):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.model = self.build_model()
        self.movie_data = movie_data  # Cargar datos de películas al inicializar
    
    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [token for token in tokens if token.isalnum()]
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)

    def build_model(self):
        model = Sequential([
            Dense(512, activation='relu', input_shape=(30000,)),
            Dropout(0.5),
            Dense(256, activation='relu'),
            Dropout(0.5),
            Dense(5000, activation='softmax')
        ])
        model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def get_similar_movies(self, movie_title, top_n=10):
        if not self.movie_data:
            return "No hay películas disponibles en el sistema."

        target_movie = next((movie for movie in self.movie_data if movie["title"].lower() == movie_title.lower()), None)
        if not target_movie:
            return "Película no encontrada."

        similar_movies = self._find_similar_movies_recursive(target_movie, [], top_n)

        if not similar_movies:
            return "No se encontraron películas similares."

        return [(movie["title"], movie["release_date"][:4]) for movie in similar_movies]

    def _find_similar_movies_recursive(self, target_movie, similar_movies, top_n):
        if len(similar_movies) >= top_n:
            return similar_movies[:top_n]

        for movie in self.movie_data:
            if movie["title"] != target_movie["title"] and movie not in similar_movies:
                if movie["release_date"] and target_movie["release_date"]:
                    if movie["release_date"][:4] == target_movie["release_date"][:4]:
                        similar_movies.append({"title": movie["title"], "release_date": movie["release_date"][:4]})

        if len(similar_movies) < top_n:
            return self._find_similar_movies_recursive(target_movie, similar_movies, top_n)
        else:
            return similar_movies

# Crear una instancia del sistema de recomendación con los datos del archivo CSV
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
