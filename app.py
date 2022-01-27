from flask import Flask, render_template, request
from stories import Story, story

app = Flask(__name__)

@app.route('/')
def madlib_form():

    items = story.prompts

    return render_template('madlib_form.html', words=items)

@app.route('/completed_madlib')
def madlip_gen():

    answers = request.args

    finished_story = story.generate(answers)

    return render_template('completed_madlib.html', story=finished_story)