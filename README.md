# woniu-cmdb
### 奇技淫巧--写配置文件生成增删改查系统


> 运维人员都不喜欢搞CMDB，因为有很多前端的内容，但CMDB却在运维圈占有重要的地位，开发CMDB就是各种增删改查，之后我有个想法，不如重新开发一个属于自己的CMDB。写配置文件就自动生成页面的CMDB, 请支持我的woniu-cmdb,喜欢请star


### 功能
* 配置生成页面
* 页面自带增删改查和查看详情

### 使用规范

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
