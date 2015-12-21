# woniu-cmdb
### :snail: 奇技淫巧--写配置文件生成增删改查系统:mushroom: 

[线上demo](http://admin.51reboot.com/)

> 运维人员都不喜欢搞CMDB，因为有很多前端的内容，但CMDB却在运维圈占有重要的地位，开发CMDB就是各种增删改查，之后我有个想法，做一个写配置文件就自动生成页面的CMDB, 请支持我的woniu-cmdb,喜欢请star

### 写好配置文件，自从生成页增删改查面不是梦

此项目不仅限于cmdb，各种管理系统，都可以用此项目配置，我会一直维护这个项目，大家有新需求请提issue

### 效果图（我们只写左边的配置，右边的是自动生成的）
![](http://7xjoq9.com1.z0.glb.clouddn.com/cmdb01.png)


### 简单配置，生成页面
命令只有两个

> python woniu-build.py init # 初始化数据库+根据配置生成文件
> python woniu-build.py 仅根绝配置生成文件 

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

```

page_config = {
    # menu是一个list，包含所有的页面信息
    "menu":[{
        //页面的名字，和数据库表一致
        "name": 'user',
        // 显示的页面标题
        "title": '用户管理',

        # 页面里具体的字段，如果有两个字段，配置两个即可，包含name和title
        "data": [{
            "name": 'username',
            "title": '用户名'
        },{
            "name":'password',
            "title":'密码'
        }]
    }}]
}

```

4. 执行 python woniu-build.py 处理文件，启动flask_web.py，浏览器访问http://localhost:9092/
5. 默认有一个用户，账号和密码都是51reboot


### 字段详解

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

### 依赖

本项目python依赖flask和mysqldb模块，直接pip安装一下即可
