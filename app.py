from flask import Flask, render_template, request 
import requests
import json
import logging


API_URL = "http://localhost:11434/api/generate"


logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filemode='w+')



app = Flask(__name__)

@app.route("/")
def index():
    logger.info('----------------- STARTING APP')
    return render_template("index.html")

@app.route("/answer", methods=["GET", "POST"])
def answer():
    input_data = request.get_json()
    message = input_data["message"]
    data = {"model": "llama3.2", "prompt": message, 'stream': True}
    logger.info(f'Prompting llm API with: {data}')

    session = requests.Session()
    try:
        # TODO add try to rm old ollama container and rebuild new one if error here
        response = session.post(API_URL, json=data, stream=True)
        response.raise_for_status()
        status_code = response.status_code
        logger.info(f'Response status code: {status_code}')
    except requests.exceptions.RequestException as err:
        logger.exception('Failed to establish session to prompt llm API ')
        raise err

    def generate():
        for line in response.iter_lines():
            if line:
                try:
                    line_decoded = line.decode('utf-8')
                    res_json = json.loads(line_decoded)            
                    response_text = res_json['response']
                except Exception as err:
                    #response_text = 'NO ANSWER IN API RESPONSE !!!!!'
                    logger.exception('Failed streaming llm API answer')
                    raise err

                yield response_text

    return generate(), {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(debug=True)