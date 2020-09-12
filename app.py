from flask import Flask, request, jsonify

from main import process_input

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "hola"


@app.route('/grammarit/<input_text>', methods=['GET', 'POST'])
def process_request(input_text):
    processed_input = process_input(input_text)
    print(processed_input)
    return jsonify(process_input(input_text))
    # param1 = request.args.get('input_text', default='', type='str')

if __name__ == "__main__":
    app.run(debug=True)
