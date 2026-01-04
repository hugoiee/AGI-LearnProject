from http.client import responses

import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
)

@tool('get_weather', description="返回查询的天气", return_direct=False)
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()


agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一个充满幽默的天气助手",
)

response = agent.invoke({
    "message": [
        {"role": "user", "content": "New York的天气怎么样"}
    ]
})

print(response["message"][-1])
