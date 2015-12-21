# coding=utf-8


# 数据库配置
db_config = {
	'host':'localhost',
	'user':'root',
	'passwd':"",
	'db':'cmdb'
}


page_config = {
    brand_name:'Woniu Admin'
    menu:[{
        "name": 'user',
        "title": '用户',
        "desc":'这个是用户的配置，尽量不要改',
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
    }]
}

# 页面配置
# page_config = [
#     {
#         "name": 'role',
#         "title": '权限',
#         "data": [{
#             "name": 'name',
#             "title": '权限名'
#         },{
#             "name":'password',
#             "title":'999'
#         }]
#     }
# ]


