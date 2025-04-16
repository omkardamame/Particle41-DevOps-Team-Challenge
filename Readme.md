# SimpleTimeService

A minimal Flask-based microservice that returns the current timestamp and the requester's IP address in JSON format.

## 📦 Features

- Returns current timestamp in ISO 8601 UTC format.
- Returns the IP address of the requester.
- Lightweight, minimal Docker image.
- Runs as a non-root user for better security.

## 🖥️ Sample JSON Output

```json
{
  "timestamp": "2025-04-14T15:30:00Z",
  "ip": "172.17.0.1"
}
```

# 🚀 Getting Started

### 🛠️ Prerequisites

- Docker installed on your system.

### 🐳 Build the Docker Image

```bash
docker build -t simple-time-service .
```

### 📦 Run the Container

```bash
docker run -dit --name simple-time-service -p 5000:5000 simple-time-service
```

> The service will now be available at: `http://localhost:5000/`

### 🔍 Test the Output

You can test the service on your server using:

```
curl http://localhost:5000/
```

### 🧑‍💻 Check Running User (Security Check)

To verify the container is running as a non-root user:

```bash
docker exec -it simple-time-service whoami
```

Expected output:

```bash
appuser
```

## 📁 Project Structure

```
.
├── app.py          # Flask app source code
├── Dockerfile      # Multi-stage Docker build (optimized for size and security)
└── README.md       # You're here
```

## 📦 Image Info

- Base image: `python:3.11-alpine`
- Final size: ~69MB
- No root access inside the container

## 📦 Pull my image for reference

```bash
docker run -dit --name simple-time-service -p 5000:5000 omkardamame/simpletimeservice
```

# 🧹 Cleanup

```bash
docker stop simple-time-service 
```

```
docker rm simple-time-service
```
