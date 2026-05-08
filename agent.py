from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool,ToolRuntime
from tavily import TavilyClient
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI
import base64
import io
import discord
import asyncio
tavily_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))


@tool
def generateAndSendImage(prompt:str,runTime:ToolRuntime):
    """Use this tool to generate and send image"""

    llm = ChatOpenAI(model="gpt-5.4-mini")
    config=runTime.config.get('configurable')
    message=config.get('message')
    loop=config.get('loop')
    tool = {"type": "image_generation", "quality": "low"}

    llm_with_tools = llm.bind_tools([tool])

    ai_message = llm_with_tools.invoke(prompt)

    image=ai_message.content_blocks(0)['base64']

    base64_str=base64.b64decode(image)
    image_bytes=io.BytesIO(base64_str)
    file=discord.file(fp=image_bytes,filename='image.png')

    asyncio.run_coroutine_threadsafe(message.channel.send(file=file),loop)

    return 'Image generated and send succesfully.'

@tool
def surfInternet(query:str):
    """USe this tool of search internt and give latest information of result back to LLM"""

    result=tavily_client.search(query=query)
    return str(result)

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

agent=create_agent(model=model,tools=[surfInternet,generateAndSendImage],system_prompt="""Provide clean output to the user""")