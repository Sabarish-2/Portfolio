from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # name = "World!"
    # if name in request.args:
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get("name", "World")
    return render_template('greet.html', name=name)



# if __name__ == '__main__':
#     app.run()
