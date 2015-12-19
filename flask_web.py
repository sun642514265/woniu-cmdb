from flask import Flask,request,render_template,redirect,url_for
import requests
app = Flask(__name__)
import json

from dbutil.dbutil import DB
# import dbutil.
db = DB(host="localhost", mysql_user="root", mysql_pass="", \
                mysql_db="cmdb")

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

    obj = request.form.to_dict()
    table = obj.pop('action_type')
    keys = obj.keys()
    values = obj.values()

    sql = 'insert into %s (%s) values ("%s")' % (table,','.join(keys),'","'.join(values))
    print sql
    db.execute(sql)
    res = {'result':'ok'}
    return json.dumps(res)
@app.route('/delapi', methods=['POST'])
def delapi():

    obj = request.form.to_dict()
    table = obj.pop('action_type')
    table_id = obj.pop('id')
    sql = 'delete from %s where id=%s' %(table,table_id)
    # sql = 'insert into %s (%s) values ("%s")' % (table,','.join(keys),'","'.join(values))
    print sql
    db.execute(sql)
    res = {'result':'ok'}
    return json.dumps(res)

@app.route('/listapi')
def listapi():
    action_type = request.args.get('action_type')
    sql = 'select * from '+action_type
    cur = db.execute(sql)
    res = {"result":cur.fetchall()}
    return json.dumps(res)





@app.route('/updateapi',methods=['POST'])
def updateapi():
    obj = request.form.to_dict()
    table = obj.pop('action_type')
    table_id = obj.pop('id')
    arr = []
    for key,val in obj.items():
        arr.append('%s="%s"'%(key,val))
    print arr
    keys = obj.keys()
    values = obj.values()
    sql = 'update %s set '%(table)

    sql += ','.join(arr)
    sql += ' where id='+table_id
    print sql
    db.execute(sql)
    res = {'result':'ok'}
    return json.dumps(res)









@app.route('/aaa')
def aaa():
    return render_template('layout1.html')
@app.route('/')
def index():
    return redirect('/page/host')
    # return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,port=9092,host='0.0.0.0')







