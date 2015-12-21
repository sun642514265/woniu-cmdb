# woniu-cmdb
### 奇技淫巧--写配置文件生成增删改查系统


> 运维人员都不喜欢搞CMDB，因为有很多前端的内容，但CMDB却在运维圈占有重要的地位，开发CMDB就是各种增删改查，之后我有个想法，做一个写配置文件就自动生成页面的CMDB, 请支持我的woniu-cmdb,喜欢请star

此项目其实就是生成增删改查系统，不仅限于cmdb，各种管理系统，都可以用此项目配置，我会一直维护这个项目，大家有新需求请提issue

### 功能
* 配置生成页面
* 自带一个user表，负责登录功能
* 页面自带增删改查和查看详情

### 使用指南

1. 下载该项目到本地
2. config.py是我们唯一要修改的文件
2. 修改config.py里的db_config变量，配置数据库的host，用户名，密码和要操作的数据库

```python
db_config = {
    'host':'localhost',
    'user':'root',
    'passwd':"",
    'db':'cmdb'
}

```

3. 修改config.py的page_config变量，此变量是设置具体的页面变量，先做一个简单的配置







| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

```

{
    name:名字
    titile:中文
    modal_detail:是否用模态窗展示详情（有隐藏字段没展示）
    具体字段数据
    data：[
        {
            name:
            title:
            type:类型，默认input text
            select_type：获取数据的action_type的值
            option_val list的显示字段 默认id
            option_name list的显示字段 默认name
            toname:preload数据里，完成id到name得转换显示，select默认true
            value：select直接从value里渲染，不发ajax和preload，如果没有type，就是input里的value属性
             hide:默认false，true的话隐藏此字段


        }
    ]
}
```

todolist:

* 侧边栏生成
* 初始化数据库
* 登录页面
