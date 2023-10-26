# -*- coding: utf-8 -*-
import datetime
import os.path
import socket
import shortuuid
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import FileResponse
import engine


class TtsRequest(BaseModel):
    text: str
    lang: str | None = None
    gender: int | int = 0


INNER_IP = socket.gethostbyname(socket.gethostname())

app = FastAPI()

PORT: int = 5000

def save_wav(text, file_id, speaker_id, model):
    now = datetime.datetime.now()
    str_now = now.strftime('%Y-%m-%d')

    try:
        if not os.path.exists(str_now):
            os.makedirs(str_now)
        engine.save(text, f'./{str_now}/{file_id}.wav', speaker_id, model)
    except OSError as e:
        return {"result": {
            "status": "error",
            "code": e.errno,
            "message": e.strerror
        }}
    return {"result": {
        "tts_url": f'http://{INNER_IP}:{PORT}/tts/{file_id}'
    }}


@app.on_event("startup")
def startup_event():
    print("App started")


@app.post('/tts')
async def request_tts(req: TtsRequest):
    model = f'./voices/es_ES-sharvard-medium.onnx'
    file_id = shortuuid.uuid()
    result = save_wav(req.text, file_id, req.gender, model)
    return result


@app.get('/tts/{file_id}')
async def download_tts(file_id):
    now = datetime.datetime.now()
    str_now = now.strftime('%Y-%m-%d')
    try:
        return FileResponse(f'./{str_now}/{file_id}.wav', media_type="audio/wav")
    except OSError as e:
        return {"result": {
            "status": "error",
            "code": e.errno,
            "message": e.strerror
        }}
#
#
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
