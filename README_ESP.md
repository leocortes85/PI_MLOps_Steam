![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)

# Proyecto MLOps para la Plataforma Steam

Proyecto individual parar el bootcamp de Data Science de 'Soy Henry'

## Descripción del Proyecto

Este proyecto simula el rol de un MLOps Engineer, combinando las responsabilidades de un Data Engineer y un Data Scientist, para la plataforma multinacional de videojuegos Steam. El objetivo es desarrollar un Producto Mínimo Viable que incluya una API deployada en un servicio en la nube y la aplicación de dos modelos de Machine Learning. Estos modelos abordan el análisis de sentimientos sobre los comentarios de los usuarios de los juegos, la recomendación de juegos basada en información de usuarios y la similitud entre los juegos por generos.

Steam, una plataforma de distribución digital de videojuegos, cuenta con más de 325 millones de usuarios y ofrece más de 25,000 juegos en su catálogo.

## Conjuntos de Datos Utilizados

Se utilizaron tres archivos JSON proporcionados:

1. `australian_user_reviews.json`: Contiene comentarios de usuarios sobre juegos, información de recomendación, emoticones y estadísticas. También incluye el ID del usuario, la URL del perfil y el ID del juego.

2. `australian_users_items.json`: Proporciona información sobre los juegos jugados por los usuarios y el tiempo acumulado jugado por cada usuario en un juego específico.

3. `output_steam_games.json`: Contiene datos relacionados con los juegos, como título, desarrollador, precios y características técnicas.

## Transformaciones y Feature Engineering

- Se realizó una Extracción, Transformación y Carga (ETL) utilizando la librería Pandas.
- Se aplicaron estrategias para manejar datos anidados y se eliminaron columnas irrelevantes o con muchos valores nulos.
- Se creó la columna 'sentiment_analysis' para clasificar comentarios en malos, neutrales o positivos utilizando TextBlob.
- Se generaron dataframes auxiliares para optimizar el rendimiento de la API y se guardaron en formato parquet para eficiencia de almacenamiento.

## Análisis Exploratorio de Datos (EDA)

- Se realizó un EDA en los conjuntos de datos transformados utilizando Pandas, Matplotlib y Seaborn.
- Se identificaron variables relevantes para la creación del modelo de recomendación.

## Modelos de Recomendación

- Se desarrollaron dos modelos de recomendación: ítem-ítem y usuario-juego.
- Se utilizaron algoritmos basados en memoria, utilizando la similitud del coseno para medir similitudes entre juegos y usuarios.
- Se generaron listas de 5 juegos recomendados para un juego específico o un usuario, respectivamente.

Este README proporciona una visión general del proyecto MLOps para la plataforma Steam, destacando los procesos clave y los resultados obtenidos. Para obtener información detallada sobre la implementación, consulte la documentación y el código fuente en el [repositorio de GitHub](https://github.com/leocortes85/PI_MLOps_Steam). También puede acceder a la API y explorar la documentación en [Enlace de la API](https://mlops-steam-leo.onrender.com/). 

Para conocer más sobre el creador de este proyecto, visite su  [LinkedIn profile](https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano-13522295/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano-13522295/).
