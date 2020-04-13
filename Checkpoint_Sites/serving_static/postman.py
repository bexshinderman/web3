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

        #obtain name from formm in postman
        name = request.form.get('name')

        #if name entered
        if name:
            #find country that matches name
            country = Country.objects.get(name=name)
            output = country.to_json()

            #if no input entered
        else:
            country = Country.objects
            getcountry = country.to_json()
            output = 'No Country entered, Complete list: \n' + getcountry 
        return output
   


    if request.method == 'POST':
       #get countries from db
       country = Country.objects
       #obtain country name from form in postman
       name = request.form.get('name') 
       #if name obtained
       if name:
             #save new country name to Country table
            new = Country(name=name).save()
            output = name + ' added to  database \n' + country.to_json()
       #if no name obtained
       else:
            output = "No input received, no Country added"
       return output

    if request.method == 'DELETE':
        country = Country.objects
        name = request.form.get('name') 
        if name:
            delname  = Country.objects.get(name=name)
            delname.delete()
            output = name + ' deleted! \n' + country.to_json()
        else:
            output = "No input received, nothing deleted"
    return output 

   
   
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

