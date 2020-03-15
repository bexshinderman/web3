

from flask import Flask, request, render_template
app = Flask(__name__,static_url_path='')


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
@app.route('/about-us')
@app.route('/aboutUs')
def about():    
    return "Just some plain text on the about page"

@app.route('/page')
def page():
    return 'on page'

@app.route('/index')
def hello():
    
    return render_template("index.html")

@app.route('/inspo')
def inspo():
    
    return render_template("inspiration.html")




if __name__ =="__main__":
    app.run(debug=True,port=8080)

