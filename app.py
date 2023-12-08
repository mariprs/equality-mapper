from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
 app.run(debug=True)