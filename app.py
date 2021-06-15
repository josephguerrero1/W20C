from werkzeug.utils import html
import dbconnect
import mariadb
import traceback
import json
from flask import Flask, request, Response
app = Flask(__name__)


@app.get('/animals')
def getAnimalList():
    conn = dbconnect.get_db_connection()
    cursor = dbconnect.get_db_cursor(conn)
    try:
        animalList = ["jaguar", "cougar", "leopard", "tiger", "lion"]
    except:
        traceback.print_exp()
    dbconnect.close_db_cursor(cursor)
    dbconnect.close_db_connection(conn)
    result_json = json.dumps(animalList, default=str)
    return Response(result_json, mimetype='application/json', status=201)


@app.post('/animals')
def addAnimal():
    try:
        animalList = ["jaguar", "cougar", "leopard", "tiger", "lion"]
        animalList.append("owl")
        successMessage = "Animal has been added!"
    except:
        traceback.print_exp()
    result_json = json.dumps(successMessage, default=str)
    return Response(result_json, mimetype="text/html", status=201)


@app.patch('/animals')
def updateAnimal():
    try:
        animalList = ["jaguar", "cougar", "leopard", "tiger", "lion"]
        animalList[2] = "giraffe"
        successMessage = "Animal has been updated!"
    except:
        traceback.print_exp()
    result_json = json.dumps(successMessage, default=str)
    return Response(result_json, mimetype="text/html", status=201)


@app.delete('/animals')
def updateAnimal():
    try:
        animalList = ["jaguar", "cougar", "leopard", "tiger", "lion"]
        animalList.remove("jaguar")
        successMessage = "Animal has been deleted!"
    except:
        traceback.print_exp()
    result_json = json.dumps(successMessage, default=str)
    return Response(result_json, mimetype="text/html", status=201)


app.run(debug=True)
