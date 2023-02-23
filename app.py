from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
import create_test
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__ , static_folder='./templates/img/')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def post():
    f = request.files.get('image')
    filename = secure_filename(f.filename)
    filepath = './templates/img/' + filename
    ar = create_test.img_test(filepath)
    return render_template( "index.html" , array=ar , flag = True)

if __name__ == '__main__':
    app.debug = True
    app.run()