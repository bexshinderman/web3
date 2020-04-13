from flask import Flask, request, render_template, Response, redirect, url_for, jsonify
app = Flask(__name__,static_url_path='')

from mongoengine import *
connect('Checkpoint_DB')

class Countries(Document):
    name = StringField()


@app.route('/')
@app.route('/countries', methods=['GET', 'POST'])
def getCountries(countries_id=None):
    if request.method == 'GET':
        if countries_id is None:
            countries = Countries.objects
        else:
            countries = Countries.objects.get(name=countries_id)
            name = country
        #print them to html      
            return  render_template('country.html', countries = countries, name=name)

    if request.method =='POST':
        country = Countries.objects
        name = request.form['name']
        new = Countries(name=name).save()

        return render_template('country.html',country=country, name=name)

if __name__ =="__main__":
    #app.run(host='10.25.100.59',debug=True,port=8080) #for deployment
    app.run(debug=True,port=8080) #for local

#db.user.insert( { first_name: "Ken", last_name: "Smith", email: "Ken@Smith.com" } )