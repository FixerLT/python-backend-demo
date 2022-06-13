# TODO: add missing controllers
# TODO: split controllers to controllers modules
# TODO: load parameters
# TODO: do we need startup scripts? Do we place them here?
# TODO: switch db logic to utilizing adapter
from dotenv import load_dotenv
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from adapters.contract import PostgresEnv

from controllers import auth, post, analytics, user


load_dotenv("local.env")

app = FastAPI()

app.include_router(auth.router)
app.include_router(post.router)
app.include_router(analytics.router)
app.include_router(user.router)

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=PostgresEnv.get_url())


@app.get("/")
async def root():
    return {"message": "hello world"}


# To run locally
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
