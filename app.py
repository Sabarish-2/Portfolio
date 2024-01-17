from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # name = "World!"
    if name in request.args.get:
        name = request.args.get('name')
        return render_template('greet.html', name = name)
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run()
