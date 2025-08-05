from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.tts_engine import text_to_speech
import os

app = FastAPI()

# Serve audio files from the "audio" directory
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

# HTML templates (Jinja2)
templates = Jinja2Templates(directory="app/templates")

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/tts")
async def convert_text_to_speech(input: TextInput):
    try:
        file_path = text_to_speech(input.text)
        return {"audio_file": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/stt")
async def convert_speech_to_text():
    return {"message": "Speech-to-Text not yet implemented"}