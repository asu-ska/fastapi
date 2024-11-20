from fastapi import FastAPI
from fastapi.responses import FileResponse
from model.user import User

app = FastAPI()

@app.get("/hi")
async def greet():
    return "Hello World"

@app.post('/user')
async def post_user(user: User):
    print(f'{user.name=}')
    return user

@app.get('/')
async def root():
    return FileResponse("static/index.html")

@app.get('/favicon.ico', response_class=FileResponse)
async def favicon():
    return "static/favicon.ico"
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="localhost")