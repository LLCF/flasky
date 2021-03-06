from flask import Flask, request, abort, render_template
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>', 400


@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s</h1>' % name


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


@app.route('/browser')
def browser():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser is %s</p>" % user_agent


@app.route("/404")
def _404():
    abort(404)
if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()