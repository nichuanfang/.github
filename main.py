#!/usr/local/bin/python
# coding=utf-8
import json
import yaml
import re

with open('config.json', encoding='utf-8') as config_f:
    config = json.load(config_f)
    
with open('.github/gen_templates/variables_gen.yml','r+',encoding='utf-8') as var_tpl_f:
    vars_tpl = yaml.load(var_tpl_f,Loader=yaml.SafeLoader)

with open('.github/gen_templates/secrets_gen.yml','r+',encoding='utf-8') as secrets_tpl_f:
    secrets_tpl = yaml.load(secrets_tpl_f,yaml.SafeLoader)

vars_steps = []

secrets_steps = []

for item in config:
    topic:str = item['topic']
    data:dict = item['data']
    vars = data['vars']
    repos = data['repositories']
    secrets = data['secrets']
    
    vars_job = vars_tpl['jobs']['job1']
    secrets_job = secrets_tpl['jobs']['job1']
    
    # 处理vars
    for repo in repos:
        for var in vars:
            var_dict = {}
            # uses: action-pack/set-variable@v1
            # with:
            #     name: 'MY_VARIABLE'
            #     value: 'Lorem ipsun dolor simit'
            #     token: ${{ secrets.REPO_ACCESS_TOKEN }}
            
            
            var_dict['name'] = f'更新nichuanfang/{repo}的变量{var}'
            var_dict['uses'] = 'action-pack/set-variable@v1'
            var_dict['with'] = {
                'owner': 'nichuanfang',
                'repository': f'{repo}',
                'name': var,
                'value': '${{ vars.'+f'{var}'+' }}',
                'token': '${{ secrets.GH_TOKEN }}'
            }
            vars_steps.append(var_dict)
        
        # 处理secrets
        for secret in secrets:
            secret_dict = {}
            secret_dict['name'] = f'更新nichuanfang/{repo}的密钥{secret}'
            secret_dict['uses'] = 'jon-grey/github-actions-secrets-creator@v1'
            secret_dict['with'] = {
                'location': f'nichuanfang/{repo}',
                'name': secret,
                'value': '${{ secrets.'+f'{secret}'+' }}',
                'pa_token': '${{ secrets.GH_TOKEN }}'
            }
            secrets_steps.append(secret_dict)
    
# 添加到对应的synchronize_variables.yml和synchronize_secrets.yml中
vars_tpl['jobs']['job1']['steps'] = vars_steps
secrets_tpl['jobs']['job1']['steps'] = secrets_steps

with open('.github/workflows/synchronize_variables.yml','w+',encoding='utf-8') as var_f:
    yaml.dump(vars_tpl,var_f,sort_keys=False,allow_unicode=True)

with open('.github/workflows/synchronize_secrets.yml','w+',encoding='utf-8') as secret_f:
    yaml.dump(secrets_tpl,secret_f,sort_keys=False,allow_unicode=True)

# 将 'on' 替换为on
new_lines = ''
with open('.github/workflows/synchronize_variables.yml','r+',encoding='utf-8') as var_f:
    lines = var_f.readlines()
    new_lines = list(filter(lambda x: re.match(r'\'on\'', x) == None, lines))
    new_lines.insert(1,'on:\n')
    
with open('.github/workflows/synchronize_variables.yml','w+',encoding='utf-8') as var_f:
    var_f.write(''.join(new_lines))
    
new_lines = ''
with open('.github/workflows/synchronize_secrets.yml','r+',encoding='utf-8') as secret_f:
    lines = secret_f.readlines()
    new_lines = list(filter(lambda x: re.match(r'\'on\'', x) == None, lines))
    new_lines.insert(1,'on:\n')
    
with open('.github/workflows/synchronize_secrets.yml','w+',encoding='utf-8') as secret_f:
    secret_f.write(''.join(new_lines))