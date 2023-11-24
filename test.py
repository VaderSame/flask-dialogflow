## Render, Github, Flask and DialogFlow integration Example.
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from google.api_core.exceptions import InvalidArgument
from google.cloud.dialogflow_v2 import SessionsClient
from google.cloud.dialogflow_v2.types import TextInput, QueryInput
from uuid import uuid4
import os

# Set google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = "restrobud-curs"
dialogflow_lang_code = "en"
session_id = uuid4()

# Create DialogFlow Session Client
session_client = SessionsClient()
session = session_client.session_path(project_id, session_id)
# text_input = TextInput(text = "Hello" , language_code = dialogflow_lang_code)
# query_input = QueryInput(text = text_input)



# Determine environment
prod = True if os.getenv("PRODUCTION") == "production" else False

print(prod)

# Create Flask App
app = Flask(__name__)

@app.route("/test-df", methods=["POST"])
def example_df_route():
    data = request.get_json(silent=True)
    message = data["message"]

    print(message)

    text_input = TextInput(text=message, language_code=dialogflow_lang_code)
    query_input = QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input
        )
    except InvalidArgument as e:
        return f"Failed to parse result {e}"

    print("Fulfillment text:", response.query_result.fulfillment_text)

    return jsonify({"response": response.query_result.fulfillment_text})



@app.route("/test", methods=["POST"])
def example_route():
    data = request.get_json(silent=True)
    print(data)
 
    return jsonify(data)


if __name__ == "__main__":
    if prod:
        app.run(debug=True)
    else:
        app.run(debug=True, host="127.0.0.1", port=8080)