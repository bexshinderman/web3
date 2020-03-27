

from flask import Flask, request, render_template, Response, redirect, url_for
app = Flask(__name__,static_url_path='')

if __name__ =="__main__":
    app.run(host='127.0.0.3', port=80)



@app.route('/load_data')
def load_data():
    return 'Success'

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










