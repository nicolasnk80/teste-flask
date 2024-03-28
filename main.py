# pip3 install gunicorn
# pip3 freeze > requirements.txt
# heroku login

from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
  name = request.args.get('name')

  if name == "João":

    response = {"message": True}

  else:
     response = {"error": False}

  return response

if __name__ == '__main__':
    app.run(debug=True)
