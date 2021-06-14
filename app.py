from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    from_query = request.args.get('from')
    to_query = request.args.get('to')

    if from_query == None or to_query == None:
        return {
            "message": "Request forbidden. Review your URL"
        }, 401

    try:
        payload = {
            "from": from_query,
            "to": to_query,
        }
        response = requests.get('https://api.exchangerate.host/convert',
            params=payload
        )
        data = response.json()
        if not data["info"]["rate"]:
            return jsonify({
                "message": "One of your currencies is not supported" 
            })
        return jsonify({
            "exchange": data["info"]["rate"]
        })
    except requests.exceptions.ConnectionError as error:
        return error
    except requests.exceptions.Timeout as error:
        return error
    except requests.exceptions.RequestException as error:
        return error
