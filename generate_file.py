
# coding=utf-8

import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")


name = 'test'

head = '''
{% extends "layout.html" %}
{% block body %}
{% endblock %}
{% block js %}
<script>	
$(function() {

    $.rebootOps(
'''

foot = '''
)
})
</script>
{% endblock %}

'''




import json



config = {
    "name": 'user',
    "title": '用户',
    "data": [{
        "name": 'name',
        "title": '用户名'
    },{
    	"name":'password',
    	"title":'密码'
    }]
}

print json.dumps(config).encode('utf-8')
with open('templates/'+name+'.html','w') as f:
	f.write(head)
	f.write(json.dumps(config))
	# f.write(str({'name':'你好'}))
	# f.write(unicode(str(config),'utf-8').decode('gbk'))
	f.write(foot)


