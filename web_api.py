import flask
from flask import request, jsonify
import student_generator2 as sg

#create a flask app
app = flask.Flask(__name__)

#use student generator as a base
#get student dictionaries
#create 2 routes
#return all students
#return students by major

#auto reload server when changes are made
app.config["DEBUG"] = True

#get the student dictionaries
student_dictionaries = sg.get_student_dictionaries()

#create a route for the server home page
@app.route("/", methods = ['GET'])
def index():
    return "<h1>Hello World, my name is Cristiano Ronaldo, SIUUUUUUUU</h1>"

#create a route to return all student data in json format
@app.route('/api/students/all', methods = ['GET'])
def api_all():
    return jsonify(student_dictionaries)

app.run()