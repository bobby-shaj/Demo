from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def demo():
    html_content = """
        <h1>Hello World!</h1>
    """
    return HTMLResponse(content=html_content, status_code=200)
