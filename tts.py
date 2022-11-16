from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi import requests
import librosa
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
# from fastapi.responses import FileResponse

app = FastAPI(
    title="Text to Speech",
    description="This is a simple API to convert text to speech",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

URL = "http://216.48.183.26/convert"

"""
{
    "text": "We’re a company of builders who care deeply about real-world implications and applications.",
    "voice": "gabby_reading",
    "seed": 3,
    "rate": 16000

}
"""

async def get_audio(text, voice, seed, rate):
    data = {
        "text": text,
        "voice": voice,
        "seed": seed,
        "rate": rate
    }
    response = requests.post(URL, data=data)
    return response

class Item(BaseModel):
    text: str ="We’re a company of builders who care deeply about real-world implications and applications."
    voice: str ="gabby_reading"
    seed: int = 3
    rate: int = 16000
    

@app.get("/")
def index():
    return {"message": "Welcome to the Text to Speech API"}

@app.get("/tts")
async def tts():
    # send text to TTS API
    # data = {
    #     "text": "We’re a company of builders who care deeply about real-world implications and applications.",
    #     "voice": "gabby_reading",
    #     "seed": 3,
    #     "rate": 16000
    # }

    # read audio file from local storage
    # audio = librosa.load("subash.mp3")
    # return audio as response file
    return FileResponse("audio-file/subash.mp3")

if __name__ == "__main__":
    uvicorn.run(app, port=5500, host="0.0.0.0")
