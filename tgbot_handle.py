# 处理tgbot的请求
import sys
import json
import base64

class PayloadType:
    """Payload类型

    Attributes:
        UPDATE_TOPIC_REPO (str): 更新主题仓库
        UPDATE_TOPIC_VAR (str): 更新主题变量
        UPDATE_TOPIC_SECRET (str): 更新主题密钥
    """
    UPDATE_TOPIC_REPO = 'update_topic_repo'
    UPDATE_TOPIC_VAR = 'update_topic_var'
    UPDATE_TOPIC_SECRET = 'update_topic_secret'

def  base64_decode(text:str):
    return json.loads(base64.b64decode(text).decode('utf-8'))

# topic_payload
topic_payload = sys.argv[1]

if topic_payload:
    topic_payload = base64_decode(topic_payload)
else:
    raise Exception('topic_payload is empty')

type = topic_payload['type']

if type == PayloadType.UPDATE_TOPIC_REPO:
    # 更新主题仓库
    pass
elif type == PayloadType.UPDATE_TOPIC_VAR:
    # 更新主题变量
    pass    
elif type == PayloadType.UPDATE_TOPIC_SECRET:
    # 更新主题密钥
    pass
else:
    pass