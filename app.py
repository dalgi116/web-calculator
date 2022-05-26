import flask
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    inputText = getData()
    filteredData = filterInput(inputText)
    print(filteredData)
    result = calculate(filteredData)
    return flask.render_template('form.html', result=result)



operators1 = ['+', '-']
operators2 = ['*', '/']

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
        for operator in operators1:
            inputText = inputText.replace(operator, ' ' + operator)
        splitedText = inputText.split()
        expandedSplitedText = []
        for value in splitedText:
            if not value[0] in operators1:
                value = '+' + value
            for operator in operators2:
                if operator in value:
                    value = value.replace(operator, ' ' + operator)
                    value = value.split()
            expandedSplitedText.append(value)
        return expandedSplitedText
    except:
        return inputText

def calculate(expandedSplitedText):
        result = 0
        for value in expandedSplitedText:
            if type(value) is list:
                for listValue in value:
                    if listValue[0] == '*':
                        newValue = float(newValue) * float(listValue[1:])
                    elif listValue[0] == '/':
                        newValue = float(newValue) / float(listValue[1:])
                    else:
                        newValue = listValue
                value = str(newValue)
                if not value[0] in operators1:
                    value = '+' + value
            if value[0] == '+':
                value = value[1:]
                result += float(value)
            elif value[0] == '-':
                result -= float(value[1:])
        return result