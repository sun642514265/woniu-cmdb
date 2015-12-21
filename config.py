# coding=utf-8


# 数据库配置

db_config = {
	'host':'localhost',
	'user':'root',
	'passwd':"",
	'db':'cmdb'
}


page_config = {
    "menu":[{
        "name": 'user',
        "title": '用户管理',
        "data": [{
            "name": 'username',
            "title": '用户名'
        },{
            "name":'password',
            "title":'密码'
        }]
    },{
        "name": 'host',
        "title": '服务器',
        "data": [{
            "name": 'cabinet',
            "title": '机柜'
        },{
            "name":'hostname',
            "title":'主机名'
        }]
    },{
        "title": '业务',
        "sub":[
            {
                'name': 'product',
                'title': '业务线',
                'data': [{
                    'name': 'service_name',
                    'title': '服务名'
                },{
                    'name':'module_letter',
                    'title':'模块简称'
                },{
                    'name':'dev_interface',
                    'title':'开发者'
                },{
                    'name':'op_interface',
                    'title':'运维接口人'
                }]
            },
            {
                'name': 'raidtype',
                'title': 'Raid厂商',
                'data': [{
                    'name': 'name',
                    'title': 'Raid厂商'
                }]
            }


        ]
    }]
}