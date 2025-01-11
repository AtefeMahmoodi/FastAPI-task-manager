# Task Manager API

A simple task management API built with FastAPI and PostgreSQL.

## Features

- CRUD operations for tasks
- PostgreSQL database integration
- Swagger documentation
- Linux server deployment ready
- Systemd service configuration

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd task-manager
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database:
```bash
sudo -u postgres psql
CREATE DATABASE taskdb;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE taskdb TO myuser;
```

5. Configure environment variables in `.env`:
```
DATABASE_URL=postgresql://myuser:mypassword@localhost/taskdb
```

## Development Server

Run the development server with:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks/` | Retrieve all tasks |
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/{task_id}` | Get a specific task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Data Model

Task object structure:
```json
{
    "id": integer,
    "title": string,
    "description": string (optional),
    "is_completed": boolean,
    "created_at": datetime
}
```

## Production Deployment

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Create a systemd service file at `/etc/systemd/system/taskmanager.service`:
```ini
[Unit]
Description=Task Manager API
After=network.target

[Service]
User=yourusername
Group=yourgroup
WorkingDirectory=/path/to/your/app
Environment="PATH=/path/to/your/venv/bin"
ExecStart=/path/to/your/venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000

[Install]
WantedBy=multi-user.target
```

3. Start and enable the service:
```bash
sudo systemctl start taskmanager
sudo systemctl enable taskmanager
```

4. Verify the service status:
```bash
sudo systemctl status taskmanager
```

## Documentation

- API documentation (Swagger UI) is available at: `http://localhost:8000/docs`
- Alternative documentation (ReDoc) is available at: `http://localhost:8000/redoc`

## Development

### Project Structure
```
app/
├── main.py           # Main application file
├── models.py         # Database models
├── schemas.py        # Pydantic schemas
├── crud.py          # CRUD operations
├── database.py      # Database configuration
└── routers/
    └── tasks.py     # Tasks router
```

## Error Handling

The API includes standard HTTP status codes:
- 200: Successful operation
- 201: Resource created
- 404: Resource not found
- 422: Validation error
- 500: Server error


## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.