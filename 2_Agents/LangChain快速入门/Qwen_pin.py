import os
from venv import create

from dotenv import load_dotenv
from langchain_qwq import ChatQwen

load_dotenv()
qwen_api_key = os.getenv("DASHSCOPE_API_KEY")

model = ChatQwen(
    api_key=qwen_api_key,
    model="qwen-flash",
    max_tokens=3_000,
    timeout=None,
    max_retries=2,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Chinese."
        "Translate the user sentence.",
    ),
    ("user", "I love programming."),
]

# ai_msg = model.invoke(messages)
# print(ai_msg.content)

from langchain.tools import tool
from langchain.agents import create_agent

@tool('get_weather', description="返回查询的天气", return_direct=False)
def get_weather(city: str):
    return "未知城市，暂无数据 (模拟返回: 晴, 22°C)"

agent = create_agent(
    model,
    tools=[get_weather],
    system_prompt = "你是一个乐于助人的天气助手。如果用户询问天气，请调用 get_weather 工具告诉她"
)

ai_msg = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "New York的天气怎么样"
        }
    ]
})

print(ai_msg["messages"][-1])