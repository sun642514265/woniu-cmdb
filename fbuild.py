
# coding=utf-8

import os,sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json

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


def gen_file(config):
    with open('templates/'+config['name']+'.html','w') as f:
    	f.write(head)
    	f.write('              '+json.dumps(config))
    	# f.write(str({'name':'你好'}))
    	# f.write(unicode(str(config),'utf-8').decode('gbk'))
    	f.write(foot)

def gen(config):
    for c in config:
        gen_file(c)
