import os

import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

# 配置 API 密钥
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

@tool('get_weather', description="返回查询的天气", return_direct=False)
def get_weather(city: str):
    return "未知城市，暂无数据 (模拟返回: 晴, 22°C)"

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

agent = create_agent(
    model,
    tools = [get_weather],
    system_prompt = "你是一个乐于助人的天气助手。如果用户询问天气，请调用 get_weather 工具告诉她"
)

response = agent.invoke({
    "messages" : [
        {
            "role": "user",
            "content": "纽约的天气怎么样？"
        }
    ]
})

print(response)
print(response["messages"][-1])