from flask import Flask, request, render_template, Response, redirect, url_for, jsonify
app = Flask(__name__,static_url_path='')

from mongoengine import *
connect('Checkpoint_DB')

class Country(Document):
    name = StringField()


#API stuff



@app.route('/country', methods=['POST', 'GET', 'DELETE'])
def country():
    if request.method == 'GET':
        country = Country.objects
        return country.to_json()


    if request.method == 'POST':
       country = Country.objects
       name = request.form.get('name') 
       new = Country(name=name).save()
       return country.to_json()

    if request.method == 'DELETE':
       country = Country.objects
       name = request.form.get('name') 
       delname  = Country.objects.get(name=name)
       delname.delete()
       return country.to_json()
     

    # new = Countries(name=name).save()
   
@app.route('/getCountry', methods=['GET'])
def getCountry():
    country = Country.objects
    return country.to_json()

@app.route('/getCountry/<name>', methods=['GET'])
def getCountryByName(name):
    country = Countries.objects.get(name=name)
    return country.to_json()

if __name__ =="__main__":
    #app.run(host='10.25.100.59',debug=True,port=8080) #for deployment
    app.run(debug=True,port=8080) #for local

