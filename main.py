#run command
# FASK_APP=main.py flask run

from flask import Flask, request, jsonify
from DataStore.MySQL import MySQL
dns = {
    'user': 'root',
    'host': 'localhost',
    'password': '',
    'database': 'db1'
}
db = MySQL(**dns)

app = Flask(__name__)
# jsonで返却する値の文字コードをUTF-8に
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():
    return "index page"

@app.route('/users/<int:id>')
def user(id):
    stmt = 'SELECT * FROM users WHERE id = ?'
    user = db.query(stmt, id, prepared=True)
    print(user)
    return jsonify({"user_id": user[0][0], "user_name": user[0][1]}), 200


#(mimeがapplication/jsonで送られている)
# Content-Type: application/json" --data '{"key": "value"}'
@app.route('/post_data', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        data = request.json['key']
    return data
