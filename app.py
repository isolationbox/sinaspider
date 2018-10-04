from flask import Flask
from flask import request
import sinasql
import json
app = Flask(__name__)

@app.route('/api/getlastinfo', methods=['POST'])
def getLastInfoByNode():
    res = sinasql.getLastInfoByNode(request.form['node'],request.form['page'],request.form['num'])
    return res

@app.route('/api/gethistory', methods=['POST'])
def getHistory():
    print(request.method)
    res = sinasql.getHistory(request.form['code'],request.form['num'])
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0')