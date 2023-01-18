from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.on_event("startup")
def on_startup():
    if False:
        return HTTPException(status_code=404, detail="Something went wronr.")


@app.on_event("shutdown")
def on_shutdown():
    pass


@app.get("/")
def root():

    # Welcome message from root
    return {
        "message": (
            """Hello, everyone!\
 It's simple API for lighthouse. Let's play!"""
        )
    }
