# coding=utf-8


# 数据库配置
db_config = {
	'host':'localhost',
	'user':'root',
	'passwd':"",
	'db':'cmdb'
}


# 页面配置
page_config = [
    {
        "name": 'test',
        "title": '用户',
        "data": [{
            "name": 'name',
            "title": '用户名'
        },{
            "name":'password',
            "title":'密码'
        }]
    },
    {
        "name": 'role',
        "title": '权限',
        "data": [{
            "name": 'name',
            "title": '权限名'
        },{
            "name":'password',
            "title":'密码'
        }]
    },
    # {
    #     name: 'cabinet',
    #     title: '机柜',
    #     data: [{
    #         name: 'name',
    #         title: '机柜名'
    #     },{
    #         name:'idc_id',
    #         title:'IDC',
    #         type:'select',
    #         select_type:'idc'
    #     },{
    #         name:'power',
    #         title:'电源'
    #     }]
    # }
]


