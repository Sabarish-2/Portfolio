from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/journey')
def greet():
    return render_template('journey.html')

@app.route('/projects')
def greet():
    return render_template('projects.html')

@app.route('/contact')
def greet():
    return render_template('contact.html')



# if __name__ == '__main__':
#     app.run()
