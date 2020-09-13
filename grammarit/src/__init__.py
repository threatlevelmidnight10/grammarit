from flask import Flask, request, jsonify

app = Flask(__name__)


from grammarit.api_routes import api_routes
