from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime as dth
from dome.auxiliary.enums.intent import Intent

app = Flask(__name__)
CORS(app)


def parseIntent(intent: str) -> Intent:
    match intent:
        case "ADD":
            return Intent.ADD
        case "UPDATE":
            return Intent.UPDATE
        case "DELETE":
            return Intent.DELETE
        case "GREETING":
            return Intent.GREETING
        case "READ":
            return Intent.READ
        case "GOODBYE":
            return Intent.GOODBYE
        case "HELP":
            return Intent.HELP
        case "CANCELLATION":
            return Intent.CANCELLATION
        case "CONFIRMATION":
            return Intent.CONFIRMATION
        case "MEANINGLESS":
            return Intent.MEANINGLESS
        case _:
            return None


def startServer(msgHandler):
    @app.route("/message", methods=["POST"])
    def ProcessRoute():
        data = request.get_json()
        message = data["message"]
        request_user_data = data["user_data"]

        # change the intent from json (string) to enum
        if "pending_intent" in request_user_data:
            request_user_data["pending_intent"] = parseIntent(
                request_user_data["pending_intent"]
            )

        # call the handler
        processedMessage = msgHandler(message, request_user_data, dth.now())

        # change the intent from enum to string (json)
        processedMessage["user_data"]["pending_intent"] = str(
            processedMessage["user_data"]["pending_intent"]
        )

        # change the previous intent from enum to string (json)
        processedMessage["user_data"]["previous_intent"] = str(
            processedMessage["user_data"]["previous_intent"]
        )

        return jsonify(
            {
                "message": processedMessage["response_msg"],
                "user_data": processedMessage["user_data"],
            }
        )

    app.run(host="0.0.0.0", use_reloader=False)
