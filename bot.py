import os
import discord
from dotenv import load_dotenv
load_dotenv()
from agent import agent
from langchain.messages import HumanMessage
import asyncio
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    async with message.channel.typing():
        content=message.content

        res=await agent.ainvoke(
            {"messages":[HumanMessage(content)]},
            config={'configurable':{'message':message,'loop':asyncio.get_event_loop()}}
            )

        agent_msg=res['messages'][-1].text

    await message.channel.send(agent_msg)


client.run(token=os.getenv('DISCORD_API_KEY'))