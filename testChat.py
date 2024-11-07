import requests
import json

url = "https://sztuwork.sligenai.cn/sztuapi/api/chat/stream"

headers = {
    "sztuAiApiKeyAuthorization": "6c310bc74140f79a181df8f94397781c",
    "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
    "Content-Type": "application/json",
}

data = {
    "message": "你好",
    "sessionId": "0",
    "keepMessageNum": 5,
}

responses = requests.post(url, headers=headers, data=json.dumps(data),stream=True)


# 遍历响应流
try:
    for chunk in responses.iter_lines():
        # 确保块非空
        if chunk:
            # 解码每个JSON对象字符串
            decoded_chunk = chunk.decode('utf-8')
            #print(decoded_chunk)
            # 将字符串解析为JSON
            json_object = json.loads(decoded_chunk)
            # 提取并打印`token`字段
            print(json_object)
         #   print(json_object['data']['token'],end='')

except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
except Exception as e:
    print("An error occurred:", e)