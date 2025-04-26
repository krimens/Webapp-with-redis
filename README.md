# 📨 Redis Message Board

A simple web app for submitting and viewing messages, powered by:

- **Frontend:** HTML/CSS + Nginx
- **Backend:** Flask (Python) + Redis Streams
- **Database:** Redis
- **Containerized with:** Docker & Docker Compose

---

## 🚀 Features

- Submit messages with your name
- Store messages in Redis using Streams
- Retrieve and view all submitted messages
- Containerized with Docker Compose for easy deployment

---

## 📁 Project Structure
. ├── backend/ │ ├── app.py # Flask backend │└── requirements.txt # Python dependencies │└── Dockerfile # Flask container build ├── frontend/ │ ├── index.html # Static frontend (HTML/CSS/JS) │ └── Dockerfile # Nginx container build    ├──docker-compose.yml # Compose setup for Redis, Flask, and Nginx
