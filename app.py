import flask
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    inputText = getData()
    filteredData = filterInput(inputText)
    result = calculate(filteredData)
    return flask.render_template('form.html', result=result)



splitCharacters = ['+', '-']

def getData():
    if flask.request.args:
        args = flask.request.args
        inputText = args.get('inputText')
    else:
        inputText = ''
    return inputText

def filterInput(inputText):
    try:
        inputText = inputText.replace(' ', '')
        for splitCharacter in splitCharacters:
            inputText = inputText.replace(splitCharacter, ' ' + splitCharacter)
        splitedText = inputText.split()
        expandedSplitedText = []
        for value in splitedText:
            if not value[0] in splitCharacters:
                value = '+' + value
            expandedSplitedText.append(value)
        return expandedSplitedText
    except:
        return inputText

def calculate(expandedSplitedText):
        result = 0
        for value in expandedSplitedText:
            if value[0] == '+':
                result += float(value[1:])
            elif value[0] == '-':
                result -= float(value[1:])
        return expandedSplitedText