from flask import Flask, render_template, request, url_for, redirect
import requests
import sandwich_function as sf

app = Flask(__name__)

@app.route('/')
def index():
    sandwich = sf.get_all_sandwich_table()
    return render_template('index.html', sandwich = sandwich)

def edit(rowid):
    sandwich = sf.get_sandwich(rowid)
    return render_template('edit.html', sandwich = sandwich)

@app.route('/edit-sandwich_table/<rowid>', methods=['POST'])
def edit_sandwich(rowid):
    name = request.form['name']
    bread = (request.form['bread']) 
    cheese = request.form['cheese']
    meat = request.form['meat']
    sauce = request.form['sauce']
    toping = request.form['toping']
    anything = request.form['anything']
    creator =  request.form ['creator']

    sf.update_sandwich(name, bread, cheese, meat, sauce, toping, anything, creator)
    return redirect(url_for('index'))

@app.route('/post-sandwich', methods=['POST'])
def submit():
    name = request.form['name']
    bread = (request.form['bread']) 
    cheese = request.form['cheese']
    meat = request.form['meat']
    sauce = request.form['sauce']
    toping = request.form['toping']
    anything = request.form['anything']
    creator =  request.form ['creator']
    sf.add_sandwich(name, bread, cheese, meat, sauce, toping, anything, creator)

    return redirect(url_for('index.html'))

@app.route('/delete-sandwich/<rowid>')
def delete(rowid):
    sf.delete_sandwich(rowid)
    return redirect(url_for('index'))

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')

