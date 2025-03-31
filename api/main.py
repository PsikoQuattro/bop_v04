from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def index():
    return {'msg': 'AI Money Engine API'}