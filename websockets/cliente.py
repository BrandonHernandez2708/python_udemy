import asyncio
import websockets
#definimos la funcion que manejara la conexion
async def cliente():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hola, servidor")
        respuesta = await websocket.recv()
        print(f"Respuesta del servidor: {respuesta}")

asyncio.run(cliente())
