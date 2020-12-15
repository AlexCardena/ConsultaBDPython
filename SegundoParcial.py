# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:23:14 2020

@author: Alex
"""
import psycopg2 as pc

conexion =pc.connect(user="postgres",
                      password="123456",
                      host="127.0.0.1",
                      port="5432",
                      database="SistemaEducativo")


print("Ingrese su CI")
ci = input()
#Puede ingresar estos CI: 8325946, 5325846, 9563214, 8369745, 6645754


cursor=conexion.cursor()
sql="select alumno.nombre, alumno.ap_paterno, alumno.ap_materno, materia.nombre, cursa.nota from materia, alumno, cursa where '"+ci+"'=cursa.ci and '"+ci+"'=alumno.ci and materia.id_materia=cursa.id_materia"
cursor.execute(sql)

registros=cursor.fetchall()
print("Alumn@: "+registros[0][0]+" "+registros[0][1]+" "+registros[0][2])
print("MATERIAS INSCRITAS:")
print("********************************")
for i in registros:
    print("Materia: ",i[3])
    print("Nota: ",i[4])
    print("********************************")
cursor.close()
conexion.close()

