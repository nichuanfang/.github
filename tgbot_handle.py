# 处理tgbot的请求
import sys
import json
import base64
from tgbot_types import PayloadType, UpdateType

def  base64_decode(text:str):
    return json.loads(base64.b64decode(text).decode('utf-8'))

# topic_payload
topic_payload = sys.argv[1]
# 读取config.json
with open('config.json', encoding='utf-8') as config_f:
    config = json.load(config_f)

if topic_payload:
    topic_payload = base64_decode(topic_payload)
else:
    raise Exception('topic_payload is empty')

type = topic_payload['type']

if type == PayloadType.UPDATE_TOPIC_REPO:
    # 更新主题仓库
    
    # 更新的仓库
    repositories = topic_payload['repositories']
    # 是添加还是更新 add / update
    topic_update_type = topic_payload['topic_update_type']
    if topic_update_type == UpdateType.TOPIC_ADD:
        # 新增主题仓库
        config.append({
            'topic': topic_payload['topic'],
            'data': {
                'vars': [],
                'repositories': repositories,
                'secrets': []
                }
        })
    elif topic_update_type == UpdateType.TOPIC_REPO_ADD or topic_update_type == UpdateType.TOPIC_REPO_DELETE:
        # 更新主题仓库
        for item in config:
            topic = item['topic']
            data = item['data']
            if topic == topic_payload['topic']:
                # 更新仓库
                data['repositories'] = repositories
                item['data'] = data
                break
    else:
        pass
    
    # 保存config.json
    with open('config.json', 'w+', encoding='utf-8') as config_f:
        json.dump(config, config_f, ensure_ascii=False, indent=4)
    
elif type == PayloadType.UPDATE_TOPIC_VAR:
    # 更新主题变量
    pass    
elif type == PayloadType.UPDATE_TOPIC_SECRET:
    # 更新主题密钥
    pass
else:
    pass