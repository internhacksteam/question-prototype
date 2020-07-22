from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/questionstart-page')
def input():
    return render_template('index.html')

@app.route('/questionstart-page', methods=['POST', 'GET'])
def output():
    if request.method == 'POST':
        answer = request.form.get('Answer')

        q1answers = {
            'print("Hello World!")',
            'print("Hello world!")',
            'print("hello world!")',
            'print("hello World!")'
        }

        if answer in q1answers:
            return {'response': "Correct!")
        else:
            return {'response': "Sorry, try again!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='true')




