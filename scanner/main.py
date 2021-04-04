from threading import Thread
from uvicorn import run

from web.app import app
from view.App import App
from ws.ws import Client


t = Thread(target=run, args=(app,), kwargs={
    "port": 3000
}).start()
App().run()
# Client(lambda x: print(f"Token: {x}")).run_sync()
