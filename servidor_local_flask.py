from flask import Flask, Response
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/assignment_callback', methods=['POST','GET'])
def assignment_callback():
    """For now, we will respond to assignment callbacks with empty 200 response"""
    resp = Response({"el json"}, status = 200, mimetype = 'application/json')
    return resp

if __name__ == "__main__":
    app.run()

