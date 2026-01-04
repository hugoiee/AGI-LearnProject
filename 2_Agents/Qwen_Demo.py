import os
from dotenv import load_dotenv
from openai import OpenAI

# 配置 API 密钥
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

client = OpenAI(
    api_key = api_key,
    # 以下是北京地域base_url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model = "qwen-flash",
    messages = [{'role': 'user', 'content': '你是谁？'}]
)
print(completion.choices[0].message.content)