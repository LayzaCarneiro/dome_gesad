from flask import Flask, request, jsonify




def startServer(msgHandler):
    app = Flask(__name__)
    @app.route('/message')
    def ProcessRoute():
        data = request.get_json()
        message = data['message']
        user_data = {'chat_id': '12345', 'debug_mode': False}
        
        
        processedMessage = msgHandler(message, user_data)
    
        return jsonify({'message': processedMessage['response_msg']})
    
    app.run(use_reloader=False)

