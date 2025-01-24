
""" Libreria conexion que permite ver ciudades de los paises registrados. see citys of the countrys in BD"""
import mysql.connector

conexion = mysql.connector.connect(user="root",password="vegetal3745",host=
                                "localhost", database="sakila",port="3306")

#definir el cursor
cursor = conexion.cursor()

def Cerrarconexion():
    #input(" ")
    conexion.close()
    print("fin de la conexion")

def Consulta_ciudades(pais):
    cursor.execute("SELECT country_id FROM country WHERE country ='"+pais+"';")
    id_pais = cursor.fetchone()

    if (id_pais != None):
        cursor.execute("SELECT city FROM city WHERE country_id ='"+str(id_pais[0])+"' LIMIT 5;")
        registro_city = cursor.fetchall()
        
        ciudades_s= ""
        for valor in registro_city:
            ciudades_s += valor[0]+" \n"

    else: 
        print("nombre del pais no encontrado")
        ciudades_s = ""
    
    return ciudades_s

### final de la conexion
#Cerrarconexion()
