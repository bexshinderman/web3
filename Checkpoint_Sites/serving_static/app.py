from flask import Flask, render_template, request
from mongoengine import *

import json
import os
import csv
import jinja2

connect('web3')


app = Flask(__name__)
#before the routes , later on will go in a seperate file for structure
app.config.from_object('config')


class Country(Document):
    name = StringField()


@app.route('/countries', methods=['GET','POST','DELETE'])
def getCountries(countries_id=None):
    if request.method == 'GET':
        #getting data from the database
        #countries = utility()
        
        if countries_id is None:
             countries = Country.objects
        else:
             countries = Country.objects.get(name=countries_id)
        name = countries
        #print them to html      
        return  render_template('country.html', countries=countries, name=name)
         
    if request.method == 'POST':
        #updating data in database
        countries = Country.objects
        name=request.form['name']
        new = Country(name=name).save()
        return render_template('country.html',countries=countries, name=name)

    #if request.method == 'DELETE':
       # """delete country with ID <countries_id>"""
    else:
    # POST Error 405 Method Not Allowed
        return render_template('countries.html')
if __name__ == "__main__":
    app.run(debug=True, port=8080)
    #app.run(host='0.0.0.0', port=80)
    


	