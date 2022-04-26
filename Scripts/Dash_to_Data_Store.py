#!/usr/local/bin/python
# Python script to automatize interactions between Dashboard and Data Store
# This program uses the TCP server/client model where:
# Data Store acts as the server due to being hosted on the CS server
# Dash acts as the client due to being external to the CS server

# using websockets to communicate with dash due to dash being browser based

# Module Imports
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, 'cs.csis.work', 8082):
        await asyncio.Future()  # run forever

asyncio.run(main())
