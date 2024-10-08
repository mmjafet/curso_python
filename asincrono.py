import asyncio

async def decir_hola():
    print("Hola...")
    await asyncio.sleep(2)
    print("...Mundo!")

# Ejecutar la función asíncrona
asyncio.run(decir_hola())
