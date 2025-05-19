# 📰 NewsProject-Django_Roshan

**NewsProject-Django_Roshan** is a Dockerized Django application that scrapes the latest news articles from [Zoomit.ir](https://www.zoomit.ir), filters them based on tags and keywords, and stores them in a PostgreSQL database. It uses **Celery with Redis** for periodic background task execution and **Flower** for task monitoring.

---

## 🚀 Features

- 🔁 Periodic scraping of [Zoomit.ir](https://www.zoomit.ir) using Celery & Beat  
- 🏷️ News filtering based on tags, included/excluded keywords  
- 💾 Persistent storage using PostgreSQL  
- 📡 RESTful API using Django REST Framework  
- 📈 Task monitoring with Flower  
- 🐳 Fully Dockerized with Docker & Docker Compose  

---

## 🧰 Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/NewsProject-Django_Roshan.git
cd NewsProject-Django_Roshan
````

### 2. Build and run the project

```bash
docker-compose up --build
```

This command will:

* 🟢 Start the Django web server at `http://localhost:8000`
* 🔴 Start Redis as the message broker
* 🟡 Launch Celery workers and the Beat scheduler
* 🔵 Start the Flower dashboard at `http://localhost:5555`

### 3. Create a superuser (optional, for admin access)

```bash
docker-compose exec web python manage.py createsuperuser
```

Then visit the Django admin at: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 📡 API Endpoints

| Endpoint        | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| `/api/news/`    | Fetch all stored news with filters: `?tag=...&include=...&exclude=...` |
| `/zoomit-news/` | Fetch live scraped news (not saved to the database)                    |

---

## 🕒 Periodic Tasks

* Celery Beat triggers the scraping task on a defined interval (e.g., every 30 seconds).
* Tasks are defined using `django-celery-beat` and can be managed through the Django admin.
* Only new and unique news articles are stored in the database automatically.

---

## 📊 Flower Dashboard

Monitor Celery task queues in real-time with Flower:

🌐 [http://localhost:5555](http://localhost:5555)

---

## 📂 Project Structure

```bash
NewsProject-Django_Roshan/
│
├── news/                  # Main Django app (scraping, models, API)
├── Dockerfile             # Django container setup
├── docker-compose.yml     # Services: web, redis, celery, beat, flower
├── requirements.txt       # Python dependencies
├── celery.py              # Celery app config
├── utils.py               # Scraping logic (Zoomit)
└── README.md              # This file
```

---

## 🧹 Teardown

To stop all running services:

```bash
docker-compose down
```

To stop and remove volumes and networks:

```bash
docker-compose down --volumes --remove-orphans
```

---

## 📬 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the change you have in mind.

---

## 📫 Contact

Have questions or suggestions? Feel free to reach out!
