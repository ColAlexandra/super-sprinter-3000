from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', user_stories=user_stories)

@app.route('/add')
def route_add():
    return render_template('add.html')

@app.route('/update')
def route_update():
    return render_template('update.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
