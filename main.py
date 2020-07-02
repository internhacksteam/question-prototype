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
            "Kristen",
            "kristen",
            "Niveda",
            "niveda",
            "Isabel",
            "isabel",
            "Crystal",
            "crystal",
            "Ashley",
            "ashley"
        }

        if answer in q1answers:
            return render_template('output.html', response="Correct!")
        else:
            return render_template('output.html', response="Sorry, try again!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='true')




