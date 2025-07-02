from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! This is Sowrab. My First AWS CI/CD Project'

if __name__ == '__main__':
    # This allows the Flask app to be accessible from outside the container
    app.run(host='0.0.0.0', port=5000)

