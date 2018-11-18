from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/courses')
def about():
    return render_template('courses.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if(__name__=='__main__'):
    app.run(debug=True)