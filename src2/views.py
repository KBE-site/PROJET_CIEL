# PARTIE 1

from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO # type: ignore
from flask import request
from api import get_all_solar_pattern_objects
import os
import time

# PARTIE 2

socketio = SocketIO()


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
socketio.init_app(app)
    

@app.route('/')
def index():
    return redirect(url_for('infos'))

@app.route('/infos/', methods=['GET', 'POST'])
def infos():
    title = "Projet Ciel"
    objs = ['sun', 'moon', 'mars']

    templateData = {
        "title": title,
        "objs": objs,
    }

    return render_template('infos.html', **templateData)

@app.route('/infos/<name>')
def infos_obj(name):
    title = "Projet Ciel"
    objs = ['sun', 'moon', 'mars']

    templateData = {
        "title": title,
        "objs": objs,
        "obj": name,
    }
    return render_template('infos.html', **templateData)


@app.route('/commandes/')
def commandes():
    title = "Projet Ciel"

    templateData = {
        "title": title,
    }

    return render_template('commandes.html', **templateData)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('server_response', {'data': 'Connected to server'})


# PARTIE 3

if __name__=="__main__":
    port = int(os.environ.get('PORT', 5066))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)