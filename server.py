from sanic import Sanic
from sanic.response import stream, text
import datetime
import pandas as pd
import pyshark
import asyncio

app = Sanic("Streaming_dataset")


def call_data():
    capture = pyshark.LiveCapture(interface=r'Wi-Fi')
    data = capture.sniff(packet_count=0)
    breakpoint()
    return data


async def get_data():
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, call_data)

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data="hello ! The current date is" +  str(datetime.datetime.now())
        data = await get_data()
        if data:
            print(str(data))
            await ws.send(str(data))
        else:
            await ws.send("None received")
        data=await ws.recv()
        print("received"+data)




if __name__ =="__main__":
    app.run(auto_reload=True)