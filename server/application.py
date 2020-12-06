from flask import Flask, request
from flask_cors import CORS
from markov import Markov

application = Flask(__name__)
CORS(application, supports_credentials=True)


@application.route('/')
def index():
    return 'Hi'


@application.route('/markov/evaluate/<input_string>', methods=['POST'])
def hello_world(input_string):
    rules = {}
    for key, value in request.form.items():
        rules[key] = value
    m = Markov(rules)
    try:
        result = m.evaluate(input_string)
    except RuntimeError:
        result = 'INFINITE RUNTIME'
    return {
        'result': result
    }


if __name__ == "__main__":
    application.run(port=80, debug=False)
