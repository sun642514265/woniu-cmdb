import fbuild.py
config = [{
    "name": 'test',
    "title": '用户1',
    "data": [{
        "name": 'name',
        "title": '用户名'
    },{
    	"name":'password',
    	"title":'密码'
    }]
}]



fbuild.gen(config)