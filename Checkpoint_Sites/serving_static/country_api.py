from flask import Flask, request, render_template, Response, redirect, url_for, jsonify
app = Flask(__name__,static_url_path='')

from mongoengine import *
connect('Checkpoint_DB')

class Country(Document):
    name = StringField()


#API stuff


@app.route('/country', methods=['POST', 'GET', 'DELETE'])
@app.route('/country/<country_id>', methods=['GET'])

def country(country_id=None):
    if request.method == 'GET':
        #if no country_id is given in route
        if country_id is None:
        #obtain name from formm in postman
            name = request.form.get('name')

            #if name entered in postman list matching fields
            if name:
                #find country that matches name
                country = Country.objects.get(name=name)
                output = country.to_json()

                #if no input entered in postman list all 
            else:
                country = Country.objects
                getcountry = country.to_json()
                output = 'No Country entered, Complete list: \n' + getcountry 
        #if country_id is given in route display all  matching values
        else:
                country = Country.objects(name=country_id).all()
                output = country.to_json()
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
        #get countries from db
        country = Country.objects
        #obtain country name from form in postman
        name = request.form.get('name') 
        if name:
            #get the Country to be deleted that matches input *delname  = Country.objects.get(name=name) throws error if multiple
            delname = Country.objects(name=country_id).all()
            #delete from db
            delname.delete()
            output = name + ' deleted! \n' + country.to_json()
        #if no name is entered    
        else:
            output = "No input received, nothing deleted"
    return output 


if __name__ =="__main__":
    #app.run(host='10.25.100.59',debug=True,port=8080) #for deployment
    app.run(debug=True,port=8080) #for local

