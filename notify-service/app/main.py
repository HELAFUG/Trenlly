from core import fs_broker
from faststream import FastStream

app = FastStream(fs_broker)


@app.after_startup
async def startup():
    await fs_broker.start()


@app.after_shutdown
async def shutdown():
    await fs_broker.stop()
