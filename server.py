from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)

DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', user_stories=user_stories, DATA_HEADER=DATA_HEADER)


@app.route('/add', methods=['GET', 'POST'])
def route_add():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        title = request.form['title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        data_handler.export_to_file(title, user_story, acceptance_criteria, business_value, estimation, status)
        return redirect(url_for('route_list'))


@app.route('/update/<id>', methods=['GET', 'POST'])
def route_update(id):
    user_story_choose = data_handler.choose_story_id(id)
    if request.method == 'GET':
        return render_template('update.html', user_story_choose=user_story_choose, id=id)
    if request.method == 'POST':
        title = request.form['title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        data_handler.export_update(title, user_story, acceptance_criteria, business_value, estimation, status, id)
        return redirect(url_for('route_list'))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
