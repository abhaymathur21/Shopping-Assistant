from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low
import requests

class Message(Model):
    value: str
    
local_agent = Agent(name="local_agent", endpoint=["http://localhost:8002"], port=8002)

@local_agent.on_query(model=Message)
async def query_handler(ctx:Context, destination: str, _msg: Message):
    # query_message = input("Enter a message: ")
    query_message = "iPhone 9"
    message = Message(value=query_message)
    await ctx.send(destination, Message(value=message.value))
    
if __name__ == "__main__":
    fund_agent_if_low(local_agent.wallet.address())
    local_agent.run()

    
