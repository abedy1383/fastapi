from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def run():
    return {'code':'200'}
