

from flask import Flask, request, render_template, Response, redirect, url_for, jsonify
app = Flask(__name__,static_url_path='')
import os
import csv
import pandas
import json

#csv files
app.config.from_object('config')

@app.route('/title')
def indextitle():
    title = "Bex"
    myName = "Bex"
    return render_template('name.html', name=myName, title=title) #remmemmber to list vars when declaring! these objects are used with jinja in name.html

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
   
    return render_template("index.html")

@app.route('/inspo')
def inspo():
    
    return render_template("inspiration.html")

@app.route('/page/<string:title>') #whatever is put after page/ will redirect to inspiration.html via /inspo route
def page(title):
    #return 'Title: ' + title
    return redirect(url_for("inspo"))
   


@app.route('/form')
def form():
    
    return render_template("form.html")

@app.route('/response', methods=['POST'])
def response():
    name = request.form.get("name")
    return render_template("form.html", name=name)

@app.route('/stocks')
def Stocks():
    filename = 'life_expectancy_years.csv'
    data = pandas.read_csv(filename, header=0)
    stocklist = list(data.values.flatten())
    return render_template('csv.html', stocklist=stocklist)

#mongodb stuff    

from mongoengine import *
connect('Checkpoint_DB')

class User(Document):
    email = StringField()
    first_name = StringField()
    last_name = StringField()
#bex = User(first_name='Bex', last_name='S')
#bex.save()

class Country(Document):
    name = StringField()
    data = DictField()

@app.route('/load_data')
def load_data():
    #individual csvs
    path = os.path.join(app.config['FILES_FOLDER'],"internet_users.csv")
    f = open(path)
    r = csv.reader(f)
    d = list(r)

    filename = os.fsdecode(path)
    print(filename)
    #for data in d:
       # print(data)
   
    for data in d:
        country = Country()
       
        for data in d:
            country = Country() # a blank placeholder country
            dict = {} # a blank placeholder data dict
            for key in data: # iterate through the header keys
                if key == "country":
                    for data in d:
                        countryName = data[0]
                        print(countryName)

                    # if the country does not exist, we can use the new blank country we created above, and set the name

                    
                        if Country.objects(name = countryName).count() == 0:

                            print('No entries')
                            country['name'] = countryName
                            country.save()

                    # if the country already exists, replace the blank country with the existing country from the db, and replace the blank dict with the current country's 
                    # data 
                        else:
                            f = filename.replace(".csv","") # we want to trim off the ".csv" as we can't save anything with a "." as a mongodb field name
                            print("filename f without the .csv", f)
                            if f in dict: # check if this filename is already a field in the dict
                                dict[f][key] = data[key] # if it is, just add a new subfield which is key : data[key] (value)
                            else:
    
                                dict[f] = {key:data[k]} # if it is not, create a new object and assign it to the dict
    
                            print(dictionary)
    
    return("printyboi")


    
@app.route('/load_data2')
def load_data2():
    for file in os.listdir(app.config['FILES_FOLDER']):
        filename = os.fsdecode(file)
        path = os.path.join(app.config['FILES_FOLDER'],"internet_users.csv")
        f = open(path)
        r = csv.DictReader(f) 
        d = list(r)
        for data in d:
            country = Country() # a blank placeholder country
            dict = {} # a blank placeholder data dict
            for key in data: # iterate through the header keys
                if key == "country":
                    countryName = data[key]
                # if the country does not exist, we can use the new blank country we created above, and set the name
                    if Country.objects(name = countryName).count() == 0:
                        country['name'] = countryName
                        country.save()
                # if the country already exists, replace the blank country with the existing country from the db, and replace the blank dict with the current country's 
                    else:
                        country['name'] = countryName
                        country.save()

                # data                
                else:
                    f = filename.replace(".csv","") # we want to trim off the ".csv" as we can't save anything with a "." as a mongodb field name
                    if f in dict: # check if this filename is already a field in the dict
                        dict[f][key] = data[key] # if it is, just add a new subfield which is key : data[key] (value)
                    else:
                        dict[f] = {key:data[key]} # if it is not, create a new object and assign it to the dict
                # add the data dict to the country
                country['data'] = dict
            # save the country
            country.save()
    return Country.objects.to_json()
            

        


 #all csvs
    #for file in os.listdir(app.config['FILES_FOLDER']):
     #   filename = os.fsdecode(file)
       # path = os.path.join(app.config['FILES_FOLDER'],filename)
        #f = open(path)
       # r = csv.reader(f)
       # datalist = list(r)
        #for data in datalist:
            #print(data)
            
           # print('***********************************************************************************')
    #return render_template("csv.html")
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
                output = {"message": 'No Country entered, Complete list', "countries": getcountry}
                output = json.dumps(output)
               # output = 'No Country entered, Complete list: \n' + getcountry 
        #if country_id is given in route display all  matching values
        else:
                country = Country.objects(name=country_id).all()
                output = country.to_json()
                output = json.dumps(output)
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
            #get the Country to be deleted that matches input
            #delname  = Country.objects.get(name=name) will throw an error if multiples
            delname = Country.objects(name=name)
            #delete from db
            delname.delete()
            output = name + ' deleted! \n' + country.to_json()
        #if no name is entered    
        else:
            output = "No input received, nothing deleted"
        return output 

   
        


@app.route('/users', methods=['GET'])
def users():
    users = User.objects
    return users.to_json()

@app.route('/users/<first_name>', methods=['GET'])
def getUserByFirstName(first_name):
    users = User.objects.get(first_name=first_name)
    return users.to_json()

@app.route('/users', methods=['POST'])
def new_user():
    users = User.objects.get()
 #   first_name = request.json['first_name']
   # last_name = request.json['last_name']
  #  email= request.json['email']

    db.user.insert( { first_name: "Ken", last_name: "Smith", email: "Ken@Smith.com" } )

    return('success')

@app.route('/newuserr', methods=['POST'])
def new_user1():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    return render_template("form.html", first_name=first_name, last_name=last_name, email=email)

@app.route('/userform')
def userform():
    return render_template("form.html")


users2 = [
    {
        'first_name': 'cats',
        'last_name': 'dogs',
        'email': 'cats@dogs.com'
    }
    
]
#@app.route('/users2')
#def getusers2():
#@app.route('/users2', methods = ['POST'])
#def new_user():
   # User.append(request.get_json())
    #first_name = request.form.get('first_name')
   # last_name = request.form.get('last_name')
    #email = request.form.get('last_name')
    #newuser = User(first_name = "first_name", last_name = "last_name", email="email" )
    #newuser.save
    ##newuser = db.user.insert({ "first_name": first_name, "last_name": last_name, "email": email })
    #return render_template("form.html", first_name = first_name, last_name = last_name, email=email)


if __name__ =="__main__":
    #app.run(host='10.25.100.59',debug=True,port=8080) #for deployment
    app.run(debug=True,port=8080) #for local





