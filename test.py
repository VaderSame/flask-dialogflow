## Render, Github, Flask and DialogFlow integration Example.
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from uuid import uuid4
import os




# Determine environment
prod = True if os.getenv("PRODUCTION") == "production" else False

print(prod)

# Create Flask App
app = Flask(__name__)





@app.route("/test", methods=["POST"])
def example_route():
    data = request.get_data(as_text=True)
    print(data)
 
    return jsonify(data)

#  make sure the app is running , postman request working , render request fetch
if __name__ == "__main__":
    if prod:
        app.run(debug=True)
    else:
        app.run(debug=True, host="127.0.0.1", port=8080)