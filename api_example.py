from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is a fastapi example."}


def hello(name) -> str:
    return f"Hello {name}. Welcome to this api example."


@app.get(
    "/v1/hello",
    description='Say Hello to you.',
    responses={
        400: {"description": 'get_hello fail'},
        500: {"description": 'Internal server error'}
    }
)
async def get_hello(name: str):
    hello_msg = hello(name)

    return JSONResponse(status_code=200, content={"data": hello_msg})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="api_example:app", host="0.0.0.0", port=8000, reload=False)
    # uvicorn api_example:app --reload
