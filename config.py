# coding=utf-8


# 数据库配置

db_config = {
	'host':'localhost',
	'user':'root',
	'passwd':"",
	'db':'cmdb'
}


page_config = {
    menu:[{
        "name": 'host',
        "title": '服务器',
        "data": [{
            "name": 'cabinet',
            "title": '机柜'
        },{
            "name":'hostname',
            "title":'主机名'
        }]
    }]
}