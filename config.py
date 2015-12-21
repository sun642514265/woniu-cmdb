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


