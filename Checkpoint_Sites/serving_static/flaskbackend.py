

from flask import Flask, request, render_template, Response, redirect, url_for
app = Flask(__name__,static_url_path='')






@app.route('/title')
def indextitle():
    title = "Bex"
    myName = "Bex"
    return render_template('name.html', name=myName, title=title) #remmemmber to list vars when declaring!

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/inspo')
def inspo():
    
    return render_template("inspiration.html")

@app.route('/page/<string:title>')
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


    

from mongoengine import *
connect('Checkpoint_DB')
class User(Document):
    email = StringField()
    first_name = StringField()
    last_name = StringField()
bex = User(first_name='Bex', last_name='S')
bex.save()

class Countries(Document):
    name = StringField()


@app.route('/load_data')
def load_data():
  # nz = Checkpoint_DB.Countries.insert({ "name":"new zealand"})
   #  nz.save()
  #  list = db.Countries.find()
  #  return list
    nz1 = Countries(name="New Zealand 1")
    nz1.save()
    return "Success"

    



if __name__ =="__main__":
   # app.run(host='10.25.100.59',debug=True,port=8080) for deployment
    app.run(debug=True,port=8080) #for local





