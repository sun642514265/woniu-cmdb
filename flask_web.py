from flask import Flask,request,render_template,redirect,url_for
import requests
app = Flask(__name__)
import json

data = {
        "jsonrpc": "2.0",
        "id":1,
        "auth":None,
}


headers = {"Content-Type": "application/json"}

@app.route('/page/<template>')
def render(template):
    return render_template(template+'.html')
@app.route('/addapi', methods=['POST'])
def addapi():
    print request.form
    data['params'] = request.form
    action_type = request.form.get('action_type')
    data['method'] = action_type+".create"
    
    print data
    url = 'http://127.0.0.1:5000/api'
    r = requests.post(url, headers=headers, json=json.dumps(data))
    return r.content
@app.route('/listapi')
def listapi():
    action_type = request.args.get('action_type')
    data['method'] = action_type+".get"
    data['params'] = {}
    print data
    url = 'http://127.0.0.1:5000/api'
    r = requests.post(url, headers=headers, json=json.dumps(data))
    return r.content
@app.route('/updateapi',methods=['POST'])
def updateapi():
    formdata = request.form.to_dict()
    # print formdata
    action_type = formdata.pop('action_type')
    # del request.form['action_type']
    data['method'] = action_type+".update"
    data['params'] = {
        "data":formdata,
        "where":{
            "id":request.form.get('id')
        }
    }
    print data
    url = 'http://127.0.0.1:5000/api'
    r = requests.post(url, headers=headers, json=json.dumps(data))
    return r.content





@app.route('/aaa')
def aaa():
    return render_template('layout1.html')
@app.route('/')
def index():
    return redirect('/page/host')
    # return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=9092,host='0.0.0.0')







