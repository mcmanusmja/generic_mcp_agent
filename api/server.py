from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from agents.responder.agent import ResponderAgent
from schemas.message import MCPMessage
from pydantic import ValidationError

app = FastAPI()
agent = ResponderAgent()


@app.post("/mcp")
async def handle_mcp(request: Request):
    try:
        raw_data = await request.json()
        message = MCPMessage.model_validate(raw_data)
        result = agent(message)
        return JSONResponse(content=result.model_dump(mode='json'))
    except ValidationError as ve:
        return JSONResponse(status_code=400, content={"error": "Invalid message", "details": ve.errors()})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
