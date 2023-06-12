from flask import Flask
import mysql.connector
from redis import Redis

app = Flask(__name__)
db = mysql.connector.connect(
    host='mysql',
    user='root',
    password='example',
    database='flask_app'
)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return f'Hello! You are visitor No: {redis.get("hits").decode()} .'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
