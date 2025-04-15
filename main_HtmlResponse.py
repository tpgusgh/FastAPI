##Updated Code with HtmlResponse
#main_HtmlResponse.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request):
    client_host = request.client.host  # Client IP Address
    headers = dict(request.headers)  # Request Headers
    query_params = dict(request.query_params)  # Query Parameters
    url = str(request.url)  # Requested URL

    # HTML template for better UI display
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Request Details</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                max-width: 600px;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                color: #333;
            }}
            pre {{
                background: #eee;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Request Details</h2>
            <p><strong>Client Host:</strong> {client_host}</p>
            <p><strong>Requested URL:</strong> {url}</p>
            <h3>Headers:</h3>
            <pre>{headers}</pre>
            <h3>Query Parameters:</h3>
            <pre>{query_params}</pre>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)