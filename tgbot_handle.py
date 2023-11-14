# 处理tgbot的请求
import sys

# payload_type
payload_type = sys.argv[1]
# tgbot_payload
tgbot_payload = sys.argv[2]

if payload_type == 'update_topic_repo':
    print('update_topic_repo已成功触发')
else:
    print(payload_type)