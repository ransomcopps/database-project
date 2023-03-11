from flask import Flask, render_template
import requests
import  sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    sandwich = get_all_sandwich()

    return render_template('index.html', sandwich = sandwich)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')

def edit(rowid):
    sandwich = get_sandwich




#(name, bread, cheese, meat, sauce, toping, anything)
