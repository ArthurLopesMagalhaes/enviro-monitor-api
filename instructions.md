
python -m uvicorn main:app --host 0.0.0.0 --port 8000


const socket = new WebSocket("wss://d8c0-2804-14c-fc86-800f-d52c-c43-891c-2959.ngrok-free.app/ws/temperature");

socket.onopen = () => {
    console.log("Conexão WebSocket estabelecida");
};

socket.onmessage = (event) => {
    console.log("Temperatura recebida:", event.data);
};
