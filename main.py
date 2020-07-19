from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
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
            return render_template('output.html', response="Correct!")
        else:
            return render_template('output.html', response="Sorry, try again!")

@app.route('/q2/')
def input_2():
    return render_template('q2.html')

@app.route('/q2/', methods=['POST', 'GET'])
def output_2():
    if request.method == 'POST':
        answer = request.form.get('Answer')

        q2answers = {
            '[box1 = “Divergent”]',
            '[box1 = “divergent”]'
        }

        if answer in q2answers:
            return render_template('output_q2.html', response="Correct!")
        else:
            return render_template('output_q2.html', response="Sorry, try again!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='true')




