
#pip install mysql-connector-pysthon
## CONFIGURACION DE LA BASE DE DATOS
import mysql.connector
import pandas as pd


cnx = mysql.connector.connect(
    host="ec2-34-222-110-235.us-west-2.compute.amazonaws.com",
    port=3306,
    user="data",
    password="######AAAA########",
    database="movielens"
)

print("success")

# ## Comandos SQL
# cursor = cnx.cursor()

# cursor.execute("SHOW TABLES") MOSTRAR TABLAS

# result = cursor.fetchall()

# print(result). RESULTADO DE CONSULTAR TABLAS

### Dataframes
cursor = cnx.cursor()
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print(result)

cursor.close() ## Cerramos la conexion
### Consulta a CSV
df = pd.DataFrame(result, columns=['user_id', 'gender', 'age', 'occupation', 'zip'])
df.head()

df.to_csv("movies_users.csv")