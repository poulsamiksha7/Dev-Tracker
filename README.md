# Dev-Tracking API

A REST API built with Python and Flask to track job applications.
Built independently as a skill-validation project.

## 🔗 Live Demo
https://dev-tracker-zmeb.onrender.com

## 🛠️ Tech Stack
- Python
- Flask
- SQLAlchemy
- SQLite
- Gunicorn
- Render

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /applications | Fetch all applications |
| POST | /applications | Create new application |
| PUT | /applications/<id> | Update existing application |
| DELETE | /applications/<id> | Delete application |

## 📥 Request Examples

### POST /applications
```json
{
    "job_title": "Python Developer",
    "status": "Applied",
    "application_id": 1
}
```

### PUT /applications/<id>
```json
{
    "job_title": "Flask Developer",
    "status": "Interviewed"
}
```

## 📤 Response Examples

### GET /applications
```json
{
    "applications": [
        {
            "id": 1,
            "job_title": "Python Developer",
            "status": "Applied"
        }
    ]
}
```

### POST /applications
```json
{
    "id": 1,
    "job_title": "Python Developer",
    "status": "Applied"
}
```

### DELETE /applications/<id>
```json
{
    "message": "ID Deleted"
}
```

## ⚙️ Run Locally

```bash
git clone https://github.com/poulsamiksha7/dev-tracking-api
cd dev-tracking-api
pip install -r requirements.txt
python app.py
```

## 👩‍💻 Built By
Samiksha Poul — MCA Graduate 2026
GitHub: github.com/poulsamiksha7
Portfolio: samiksha-poul-portfolio-two.vercel.app
