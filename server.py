from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'I love tacos'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    choices = ['foot', 'nuke', 'cockroach']
    computer_choice = random.randint(0,2)
    session['computer_choice'] = choices[computer_choice]
    session['you_chose'] = request.form['selected']
    if session['computer_choice'] == request.form['selected']:
        session['results'] = 'Draw'
    if session['computer_choice'] == 'nuke' and request.form['selected'] == 'cockroach':
        session['results'] = 'You win!'
    if session['computer_choice'] == 'nuke' and request.form['selected'] == 'foot':
        session['results'] = 'You lose!'
    if session['computer_choice'] == 'foot' and request.form['selected'] == 'cockroach':
        session['results'] = 'You lose!'
    if session['computer_choice'] == 'foot' and request.form['selected'] == 'nuke':
        session['results'] = 'You win!'
    if session['computer_choice'] == 'cockroach' and request.form['selected'] == 'foot':
        session['results'] = 'You win!'
    if session['computer_choice'] == 'cockroach' and request.form['selected'] == 'nuke':
        session['results'] = 'You lose!'
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)