from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello World"

@app.get('/')
def root():
    return FileResponse("static/index.html")

@app.get('/favicon.ico', response_class=FileResponse)
def favicon():
    return "static/favicon.ico"
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="localhost")