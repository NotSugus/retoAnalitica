##importamos la biblioteca de pandas
import pandas as pd
##definimos que queremos observar todas las columnas
pd.set_option('display.max_columns',None)

##le decimos a la computadora que queremos leer los datos con pandas
data = pd.read_csv("covid19_tweets.csv")

#queremos observar los tipos de datos presentes en cada columna
print(data.dtypes)
#queremos una vista simple de los datos
print(data)
#queremos un analisis sencillo de aquellos datos numericos que nos sean posibles
print(data.describe())
#queremos sortear los tweets por orden cronologico
print(data.sort_values(by='date'))
