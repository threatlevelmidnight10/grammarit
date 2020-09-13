
from grammarit.src import app
from flask import Flask, request, jsonify, make_response
from grammarit.models.auto_complete.markov_auto_complete import suggest_auto_complete


#autocomplete api
@app.route('/auto_complete/<input_text>', methods=['GET', 'POST'])
def auto_complete(input_text):
    res = suggest_auto_complete(input_text)
    return make_response(jsonify(res), 200)

@app.route('/grammarit/<input_text>', methods=['GET', 'POST'])
def grammar_check(input_text):
    res = suggest_auto_complete(input_text)
    return make_response(jsonify(res), 200)