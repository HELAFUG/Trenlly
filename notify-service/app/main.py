import asyncio

from core import fs_broker
from faststream import FastStream

app = FastStream(fs_broker)


async def main():
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
