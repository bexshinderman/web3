from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
@app.route('/cats')
def hello_world():
    return 'Hello, World!'
    return render_template('index.html', name=index)

if __name__ =="__main__":
    app.run(debug=True,port=8080)