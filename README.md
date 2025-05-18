# 🚀 FastAPI + Streamlit + PostgreSQL + Docker Stack

This project demonstrates a full-stack web application with:

- **FastAPI** for the backend API
- **Streamlit** for the frontend interface
- **PostgreSQL** for the database
- **Docker** and **Docker Compose** for containerization

---

## 📁 Project Structure

```
my_web_app/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   └── requirements.txt
├── docker/
│   ├── backend.Dockerfile
│   └── frontend.Dockerfile
├── .env
└── docker-compose.yml
```

---

## 📦 Requirements

Make sure you have installed:

- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)
- (Optional) [Python 3.10+](https://www.python.org/) for local testing

---

## ⚙️ Environment Configuration

`.env` file:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=mydb
```

---

## 🛠️ How to Run

Open **Command Prompt** and run the following:

```cmd
docker-compose up --build
```

---

## 🌐 Access the Application

| Service         | URL                         |
|------------------|-----------------------------|
| FastAPI API      | http://localhost:8000        |
| FastAPI Docs     | http://localhost:8000/docs   |
| Streamlit App    | http://localhost:8501        |
| PostgreSQL       | Internal (port 5432 in Docker network) |

---

## 🔍 File Descriptions

### 🔹 Backend (`backend/`)

- `main.py`: FastAPI server with sample route.
- `requirements.txt`: Backend Python dependencies.

### 🔹 Frontend (`frontend/`)

- `app.py`: Streamlit app that fetches data from FastAPI.
- `requirements.txt`: Frontend Python dependencies.

### 🔹 Dockerfiles (`docker/`)

- `backend.Dockerfile`: Builds the FastAPI container.
- `frontend.Dockerfile`: Builds the Streamlit container.

### 🔹 Docker Compose

- `docker-compose.yml`: Orchestrates all containers.
- Uses environment variables from `.env`.

---

## 🚧 Future Improvements

- Add SQLAlchemy models and database migrations
- Create real endpoints (CRUD)
- Style the Streamlit interface
- Add authentication (e.g., JWT)
