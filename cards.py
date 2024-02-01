from flask import Blueprint, render_template

cards = Blueprint("cards", __name__, url_prefix='/cards')

@cards.route('/')
@cards.route('/select-topics')
def select_topics():
    return render_template('select-topics.html')

@cards.route('/edit')
def edit():
    return render_template('edit.html')

@cards.route('/add')
def add():
    return render_template('add.html')

@cards.route('/quiz')
def quiz():
    return render_template('quiz.html')

