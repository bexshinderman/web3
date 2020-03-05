from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/cats')
def hello_world():
    message = "return me plz"
    return 'Hello, World!'
    return render_template('index.html', message=message)

if __name__ =="__main__":
    app.run(debug=True,port=8080)