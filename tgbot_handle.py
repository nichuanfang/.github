# 处理tgbot的请求
import sys
import json

# topic_payload
topic_payload = sys.argv[1]

payload = json.loads(topic_payload)

print(payload['topic'])