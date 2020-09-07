# coding=utf-8


# 数据库配置


db_config = {
	'host':'127.0.0.1',
	'user':'test_user',
	'passwd':"test_user",
	'db':'test'
}


page_config = {
    "brand_name":'CMDB For DBA',
    'title':'DBA资产管理平台',
    "favicon":'https://pic1.zhimg.com/6d660dd4156c64bfad13ff97d79c2f98_l.jpg',
    "menu":[
        {
            # user配置最好不要修改，是和登陆认证相关的，直接在下面加配置即可
            "name": 'user',
            "title": '用户管理',
            "modal_detail": '1',
            "data": [{
                "name": 'username',
                "title": '用户名'
            },{
                "name":'password',
                "title":'密码'
            },{
                "name":'chinese_name',
                "title":'中文名'
            },{
                "name":'telephone',
                "title":'联系方式',
                "empty":"yes"
            }]
        },

	{   
            "name":'idc',
            "title":'数据中心',
            "data":[{
                "name":"name",
                "title":'数据中心名'
            },{
                "name":"remark",
                "title":'备注',
		"empty":"yes"
            }]
        },
        {
            "name":"host",
            "title":"服务器",
            "modal_detail": '1',
            "data":[{
                "name":"idc",
                "title":'数据中心',
                "type":'select',
                "select_type":'idc'
            },

            {
                "name":"region",
                "title":'区域',
                "type":'select',
                "value":{1:'自建机房',2:'自建屏蔽机房',3:'阿里云华北1(青岛)',4:'阿里云华北2(北京)',5:'阿里云华东1(杭州)'}
            },

            {
                "name":"caninet",
                "title":'位置'
            },

            {   
                "name":"asset_no",
                "title":'资产ID'
            },

            {
                "name":"hostname",
                "title":'主机名'
            },

            {
                "name":"priv_ip",
                "title":'内网IP'
            },

            {
                "name":"cpu",
                "title":'CPU(核)'
            },

            {
                "name":"memory",
                "title":'内存(GB)'
            },

            {
                "name":"system_disk",
                "title":'系统盘(GB)'
            },

            {
                "name":"data_disk",
                "title":'数据盘(GB)'
            },

            {
                "name":'data_disk_type',
                "title":"数据盘类型",
                "type":'select',
                "value":{1:'SSD',2:'HHD'}
            },

            {
                "name":'start_time',
                "title":"购买日期",
                "type":'date'
            },

            {   
                "name":'maintenance_years',
                "title":"维保年限",
		"type":'select',
		"value":{1:'1年',2:'2年',3:'3年',4:'4年',5:'5年'}
            },

            {
                "name":'maintenance_company',
                "title":"维保公司"
            },			

            {
                "name":'maintenance_principal',
                "title":"维保人员"
            },				

            {
                "name":'maintenance_telephone',
                "title":"维保电话"
            },					

            {
                "name":'status',
                "title":'状态',
                "type":'select',
                "value":{1:'在线',2:'下线'}
            }]
        },

        {
            "name":"disk",
            "title":"硬盘",
            "modal_detail": '1',
            "data":[{
                "name":"idc",
                "title":'数据中心',
                "type":'select',
                "select_type":'idc'
            },

            {
                "name":"region",
                "title":'区域',
                "type":'select',
                "value":{1:'自建机房',2:'自建屏蔽机房',3:'阿里云华北1(青岛)',4:'阿里云华北2(北京)',5:'阿里云华东1(杭州)'}
            },

            {
                "name":"caninet",
                "title":'位置'
            },

            {
                "name":"asset_no",
                "title":'资产ID'
            },

            {
                "name":"hostname",
                "title":'主机名'
            },

            {
                "name":"priv_ip",
                "title":'内网IP'
            },

            {
                "name":"disk_brand",
                "title":'品牌'
            },

            {
                "name":"disk_model",
                "title":'型号'
            },

            {
                "name":'disk_type',
                "title":"类型",
                "type":'select',
                "value":{1:'SSD',2:'HHD',3:'PCI-E'}
            },

            {
                "name":"disk_capacity",
                "title":'容量(GB)'
            },

            {
                "name":"disk_sn",
                "title":'SN号'
            },
            {
                "name":"disk_revision",
                "title":'固件版本'
            },

            {
                "name":'disk_raid',
                "title":"RAID级别",
                "type":'select',
                "value":{1:'raid0',2:'raid1',3:'raid5',4:'raid1/0'}
            },

            {
                "name":'disk_start_time',
                "title":"购买日期",
                "type":'date'
            },

            {
                "name":'disk_maintenance_years',
                "title":"维保年限",
                "type":'select',
                "value":{1:'1年',2:'2年',3:'3年',4:'4年',5:'5年'}
            },

            {
                "name":'disk_maintenance_company',
                "title":"维保公司"
            },

            {
                "name":'disk_maintenance_principal',
                "title":"维保人员"
            },

            {
                "name":'disk_maintenance_telephone',
                "title":"维保电话"
            },

            {
                "name":'disk_status',
                "title":'状态',
                "type":'select',
                "value":{1:'在线',2:'下线'}
            }]
        },


        {
            "name":"db",
            "title":"数据库",
            "modal_detail": '1',
            "data":[{
                "name":"idc",
                "title":'数据中心',
                "type":'select',
                "select_type":'idc'
            },

            {   
                "name":"service_name",
                "title":'服务名称'
            },

            {
                "name":'service_type',
                "title":'服务类型',
                "type":'select',
                "value":{1:'生产',2:'预演',3:'测试'}
            },

            {
                "name":"priv_ip",
                "title":'内网IP'
            },

            {
                "name":"vip",
                "title":'虚拟IP',
		"empty":"yes"
            },

            {
                "name":'db_type',
                "title":'数据库类型',
                "type":'select',
                "value":{1:'MySQL',2:'MariaDB',3:'Oracle',4:'Redis',5:'MongoDB'}
            },

            {
                "name":"db_port",
                "title":'数据库端口'
            },

            {
                "name":"db_name",
                "title":'数据库名'
            },

            {
                "name":"split_db_name",
                "title":'分库数据库名',
                "empty":"yes"
            },

            {
                "name":"username",
                "title":'用户名'
            },

            {
                "name":"password",
                "title":'密码'
            },

            {
                "name":'start_time',
                "title":"上线日期",
                "type":'date'
            },
			
           {
                "name":"charge",
                "title":'研发负责人',
		"empty":"yes"
            },

	    {
                "name":'status',
                "title":'状态',
                "type":'select',
                "value":{1:'在线',2:'下线'}
            }]
        },

        {
            "name":"dbproxy",
            "title":"数据库代理",
            "modal_detail": '1',
            "data":[{
                "name":"idc",
                "title":'数据中心',
                "type":'select',
                "select_type":'idc'
            },

            {
                "name":"service_name",
                "title":'服务名称'
            },

            {   
                "name":'service_type',
                "title":'服务类型',
                "type":'select',
                "value":{1:'生产',2:'预演',3:'测试'}
            },

            {   
                "name":"instance_id",
                "title":'实例ID',
                "empty":"yes"
            },

            {   
                "name":"vip",
                "title":'虚拟IP',
                "empty":"yes"
            },

            {
                "name":'dbproxy_type',
                "title":'proxy类型',
                "type":'select',
                "value":{1:'Mycat',2:'DBLE',3:'Sharding-JDBC',4:'MaxScale'}
            },

            {
                "name":"dbproxy_port",
                "title":'proxy端口',
		"empty":"yes"
            },

            {
                "name":"mysql_port",
                "title":'MySQL端口'
            },

            {
                "name":'dbproxy_readwrite',
                "title":'读写分离',
                "type":'select',
                "value":{1:'否',2:'是'}
            },			

            {
                "name":"sharding_policy",
                "title":'分库分表策略'
            },			

            {
                "name":"primaryid_policy",
                "title":'主键生成策略'
            },
			
            {
                "name":"username",
                "title":'proxy用户名',
		"empty":"yes"
            },

            {
                "name":"password",
                "title":'proxy密码',
		"empty":"yes"
            },

            {
                "name":'start_time',
                "title":"上线日期",
                "type":'date'
            },

           {
                "name":"charge",
                "title":'研发负责人',
                "empty":"yes"
            },

            {
                "name":'status',
                "title":'状态',
                "type":'select',
                "value":{1:'在线',2:'下线'}
            }]
        }


    ]
}





# ,{
#         "name": 'host',
#         "title": '服务器',
#         "data": [{
#             "name": 'cabinet',
#             "title": '机柜'
#         },{
#             "name":'hostname',
#             "title":'主机名'
#         }]
#     },{
#         "title": '业务',
#         "sub":[
#             {
#                 'name': 'product',
#                 'title': '业务线',
#                 'data': [{
#                     'name': 'service_name',
#                     'title': '服务名'
#                 },{
#                     'name':'module_letter',
#                     'title':'模块简称'
#                 },{
#                     'name':'dev_interface',
#                     'title':'开发者'
#                 },{
#                     'name':'op_interface',
#                     'title':'运维接口人'
#                 }]
#             },
#             {
#                 'name': 'raidtype',
#                 'title': 'Raid厂商',
#                 'data': [{
#                     'name': 'name',
#                     'title': 'Raid厂商'
#                 }]
#             }


#         ]
#     }
