# 处理tgbot的请求
import sys
import json
import base64

# topic_payload
topic_payload = sys.argv[1]

if topic_payload:
    topic_payload = base64.b64decode(topic_payload).decode('utf-8')
    payload = json.loads(topic_payload)
else:
    raise Exception('topic_payload is empty')

print(payload['topic'])