# PROYECTO
 Jose Miguel Fanola[enlace](https://www.facebook.com/josemiguel.fanola?locale=es_LA)
## Introducción
 Proporciona una visión general del sistema de recomendación de películas desarrollado. El sistema utiliza técnicas de procesamiento de lenguaje natural (NLP) y aprendizaje automático para recomendar películas similares a partir de una base de datos de películas.

## Objetivo
 El objetivo principal de este proyecto es desarrollar un sistema de recomendación de películas que pueda proporcionar recomendaciones precisas y relevantes para los usuarios en función de sus preferencias.

## Marco Teórico
 El sistema se basa en los siguientes conceptos y tecnologías:

 Procesamiento de lenguaje natural (NLP): Utilizado para procesar la descripción de las películas y extraer características relevantes.
 Aprendizaje automático: Se emplea un modelo de redes neuronales para aprender patrones en los datos y generar recomendaciones.
 API de TMDb: Se utiliza para obtener información detallada sobre las películas, como el título, descripción, género y fecha de lanzamiento.
 Metodología
 La metodología seguida para desarrollar el sistema de recomendación incluye los siguientes pasos:

 - Recopilación de datos: Se recopilan datos de películas de la base de datos de TMDb.
 - Preprocesamiento de datos: Se realiza un preprocesamiento de texto en las descripciones de las películas para eliminar palabras irrelevantes y normalizar el texto.
 - Construcción del modelo: Se construye un modelo de redes neuronales utilizando la biblioteca Keras para aprender patrones en los datos y generar recomendaciones.
 - Evaluación del modelo: Se evalúa el rendimiento del modelo utilizando métricas de evaluación adecuadas.
 - Despliegue del sistema: Se implementa el sistema de recomendación como una aplicación web utilizando Flask.
 - Modelado o Sistematización
 El sistema de recomendación se basa en un modelo de redes neuronales construido con la biblioteca Keras. El modelo utiliza técnicas de procesamiento de lenguaje natural para analizar las descripciones de las películas y generar recomendaciones basadas en similitudes semánticas.

## Conclusiones
El sistema de recomendación desarrollado es capaz de proporcionar recomendaciones precisas y relevantes para los usuarios. Sin embargo, existen áreas de mejora que podrían explorarse en futuras iteraciones del proyecto, como la incorporación de información adicional sobre las preferencias de los usuarios y la optimización del modelo de recomendación.

# Bibliografía
- Documentación de la biblioteca Keras: [enlace](https://keras.io/)
- Documentación de la API de TMDb: [enlace](https://developers.themoviedb.org/3/getting-started/introduction)
- Documentación de Flask: [enlace](https://flask.palletsprojects.com/en/2.1.x/)

# Anexos
El código fuente del sistema de recomendación se encuentra disponible en el archivo recomendacion.py. Además, se incluyen ejemplos de cómo utilizar el sistema en los archivos app.py y index.html.