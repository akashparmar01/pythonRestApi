#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import MySQLdb  # connection with MySql db

connected_db = MySQLdb.connect(host='localhost',user='root',passwd='root')  # change according to your database settings
cursor=connected_db.cursor()   # cursor for connected Database
cursor.execute('CREATE database akash_python_rest_api')   # Database creation


application = Flask(__name__)  # app creation using Flask
api_rest = Api(app)  # api for the app



class Students(Resource):
    def get(self):   # GET request
        conn = connected_db.connect() # connection with the database
		query = conn.execute("select * from student") # This line performs query and returns json result
        return {'students': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is student ID
    
    def post(self):   # POST request
        conn = connected_db.connect()
        print(request.json)
        Name = request.json['Name']
        LastName = request.json['LastName']
        NickName = request.json['NickName']
        FatherName = request.json['FatherName']
        BirthDate = request.json['BirthDate']
        RegDate = request.json['RegistrationDate']
        Address = request.json['Address']
        City = request.json['City']
        State = request.json['State']
        Country = request.json['Country']
        PostalCode = request.json['PostalCode']
        Phone = request.json['Phone']
        Email = request.json['Email']
        query = conn.execute("insert into student values(null,'{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}'  \
                             )".format(Name,LastName,NickName,                         
                             FatherName, BirthDate, RegDate, Address,                  
                             City, State, Country, PostalCode, Phone,                  
                             Email))
        return {'message':'successful insertion'}  # returns message successful insertion on POST request

    
class Tracks(Resource):
    def get(self):    # GET request
        conn = connected_db.connect()  # connection with the database
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}   #DS used --> dictionary
        return jsonify(result)

    
class Student_Name(Resource):
    def get(self, student_id):   # GET request
        conn = connected_db.connect() # connection with the database
        query = conn.execute("select * from student where StudentId =%l "  %long(student_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}  # DS Used --> dictionary
        return jsonify(result)  # returns the result in json format


api_rest.add_resource(Students, '/students') # Mapping_1
api_rest.add_resource(Tracks, '/tracks') # Mapping_2
api_rest.add_resource(Student_name, '/students/<student_id>') # Mapping_3


if __name__ == '__main__':
     application.run()
