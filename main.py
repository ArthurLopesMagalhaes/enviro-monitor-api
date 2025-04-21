# main.py
from fastapi import FastAPI, WebSocket, Depends
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from sensor_reader import read_temperature
from models import Leitura
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session

# Cria tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência para obter sessão de banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.websocket("/ws/temperature")
async def websocket_temperature(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            temperature = read_temperature()
            await websocket.send_text(f"{temperature:.2f}")

            # salva no banco
            with SessionLocal() as db:
                leitura = Leitura(temperature=temperature)
                db.add(leitura)
                db.commit()

            await asyncio.sleep(1)
    except Exception as e:
        print("Erro:", e)
        await websocket.close()

@app.get("/historico")
def get_historico(limit: int = 50, db: Session = Depends(get_db)):
    leituras = db.query(Leitura).order_by(Leitura.timestamp.desc()).limit(limit).all()
    return [
        {
            "temperature": l.temperature,
            "timestamp": l.timestamp.isoformat()
        } for l in leituras
    ]
