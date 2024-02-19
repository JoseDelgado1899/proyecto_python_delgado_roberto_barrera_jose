import json


data={} #diccionario
data["campers"]=[]#lista
data["campers"].append({
    "nombre": "jose",
    "apellido": "delgado",
    "direccion":"cra 19#33-18",
    "acudiente":"cielo barrera",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "dany",
    "apellido": "bernal",
    "direccion":"cra 19#33-18",
    "acudiente":"julio",
    "telefono":3114645663,
    "estado":"en proceso de inscripcion",
    "riesgo":""})

data["campers"].append({
    "nombre": "luis",
    "apellido": "hernandes",
    "direccion":"cra 24#32-18",
    "acudiente":"laura",
    "telefono":3114643427,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "federico",
    "apellido": "gutierrez",
    "direccion":"cra 26#5-18",
    "acudiente":"karem",
    "telefono":3109871323,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "karen",
    "apellido": "sanchez",
    "direccion":"cra 12#33-18",
    "acudiente":"cielo ",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "william",
    "apellido": "galvis",
    "direccion":"cra 19#33-18",
    "acudiente":"valentina",
    "telefono":3209871223,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "valentina",
    "apellido": "amaya",
    "direccion":"cra 19#33-18",
    "acudiente":"sofia",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "laura valentina",
    "apellido": "rivera",
    "direccion":"cra 19#33-18",
    "acudiente":"camilo",
    "telefono":3006751234,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "natalia",
    "apellido": "gonzalez",
    "direccion":"cll22#11-22",
    "acudiente":"andres",
    "telefono":31147713233,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "vanessa",
    "apellido": "martinez",
    "direccion":"cra 19#8-66",
    "acudiente":"francisco",
    "telefono":3132498765,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "angie",
    "apellido": "delgado",
    "direccion":"cra 33#33-18",
    "acudiente":"vanessa",
    "telefono":3114656737,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "kelly",
    "apellido": "lopez",
    "direccion":"cra 29#33-18",
    "acudiente":"camilo",
    "telefono":3114664347,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "yohhana",
    "apellido": "amaya",
    "direccion":"cra 19#33-18",
    "acudiente":"kelly",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "xiomara",
    "apellido": "carvajar",
    "direccion":"canaveral",
    "acudiente":"jose",
    "telefono":31146546467,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "luis david",
    "apellido": "gamboa",
    "direccion":"cra 2#33-18",
    "acudiente":"luis",
    "telefono":3114323067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "cesar",
    "apellido": "cepeda",
    "direccion":"cra 19#33-18",
    "acudiente":"mateo",
    "telefono":3114642267,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "anderson",
    "apellido": "mendez",
    "direccion":"cra 19#33-18",
    "acudiente":"stiven",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "sebastian",
    "apellido": "linares",
    "direccion":"cll22#22-56",
    "acudiente":"juan",
    "telefono":3213456789,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "santiago",
    "apellido": "de",
    "direccion":"cra 19#33-18",
    "acudiente":"cielo barrera",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "juan david",
    "apellido": "ramirez",
    "direccion":"cra 19#33-18",
    "acudiente":"johhana",
    "telefono":31146694347,
    "estado":"en proceso de inscripcion",
    "riesgo":""})
data["campers"].append({
    "nombre": "jose",
    "apellido": "delgado",
    "direccion":"cra 19#33-18",
    "acudiente":"cielo barrera",
    "telefono":3114669067,
    "estado":"en proceso de inscripcion",
    "riesgo":""})






with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)