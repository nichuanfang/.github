#!/usr/local/bin/python
# coding=utf-8
import json

with open('config.json', encoding='utf-8') as config_f:
    config = json.load(config_f)
    

for item in config:
    topic:str = item['topic']
    data:dict = item['data']
    vars = data['vars']
    secrets = data['secrets']
    
    # 添加到对应的synchronize_variables.yml和synchronize_variables.yml中
    pass

pass
