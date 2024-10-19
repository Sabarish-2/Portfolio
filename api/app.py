from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return redirect('/')

@app.route('/journey')
def journey():
    return render_template('journey.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/projects#tcw')
def projectstcw():
    return render_template('projects.html#tcw')
@app.route('/projects#bbg')
def projectsbbg():
    return render_template('projects.html#bbg')
@app.route('/projects#dit')
def projectsdit():
    return render_template('projects.html#dit')
@app.route('/projects#log')
def projectslog():
    return render_template('projects.html#log')
@app.route('/projects#csw')
def projectscsw():
    return render_template('projects.html#csw')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/<path:subpath>')
def catch_all(subpath):
    return redirect('/')

# @app.route('/greet')
# def greet():
    # name = request.form.get("name", "World")
    # return render_template('greet.html', name=name)


# if __name__ == '__main__':
#     app.run()
# if __name__ == '__main__':
#     app.run(debug=True)
