

from flask import Flask, request, render_template
app = Flask(__name__,static_url_path='')


@app.route('/load_data')
def load_data():
    return 'Success'



@app.route('/index')
@app.route('/home')
def index():
    
    return render_template("index.html")

@app.route('/inspo')
def inspo():
    
    return render_template("inspiration.html")

@app.route('/page/<string:title>')
def page(title):
    return 'Title: ' + title
   


@app.route('/form')
def form():
    return render_template("form.html")
@app.route('/response', methods=['POST'])
def response():
    name = request.form.get("name")
    titletag = request.args.get('url')
    return render_template("form.html", name=name)




if __name__ =="__main__":
    app.run(debug=True,port=8080)

