from sanic import Sanic
from sanic.response import stream, text
import datetime
import pandas as pd
import pyshark
import asyncio

app = Sanic("Streaming_dataset")

def call_data(interface=r'eth'):
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(packet_count=2)
    listsd = []
    for packet in capture.sniff_continuously(packet_count=0):
        # print ('Just arrived:', packet)
        di = {}
        captured_length = packet.captured_length
        attributes= [f for  f  in dir(packet) if '__'  not in f]
        for i in attributes:
            var = getattr(packet,i)
            if isinstance(var, str):
                di.update({i: var})
            else:
                attributes= [f for  f  in dir(var) if '__'  not in f]
                for i in attributes:
                    var2 = getattr(var,i)
                    if isinstance(var2, str):
                        di.update({i: var2})
            
            listsd.append(di)
            
        return str(listsd)


async def get_data(interface):
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, call_data,interface)
        return result

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data="hello ! The current date is" +  str(datetime.datetime.now())
        interface =await ws.recv()
        
        data = await get_data(interface)
        if data:
            await ws.send(str(data))
        else:
            await ws.send("None received")

        #print("received"+data)




if __name__ =="__main__":
    app.run(auto_reload=True)