import flask
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if flask.request.args:
        args = flask.request.args
        inputText = args.get('inputText')
    else:
        inputText = ''
    return flask.render_template('form.html', inputText=inputText)