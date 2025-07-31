import flask
import os
from dotenv import load_dotenv
load_dotenv()

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return f"Hello {os.environ['YOURAPP_WHAT']}!"

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000)
