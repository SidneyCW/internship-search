## Internship Search
This is a pretty rudementary web app for searching for internships it aggregates job postings based on qualifications to give a easy application process.

## Tech Stack
### Backend:
- Django (REST Framework)
- Celery (for background tasks)
- SQLite (default for django data storage)
- Redis (as Celery broker)
### Frontend:
- React (Vite)
- Axios (for API calls)
- TailwindCSS (for styling)

## Project Setup
1. Clone the repo
```bash
git clone https://github.com/your-username/internship-search.git
cd internship-search
```
2. Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip freeze > requirements.txt # Only if you don't have a requirements.txt
pip install -r requirements.txt
```
4. Configure Environment Variables
Create a .env file in the project root
```bash
touch .env
```
Add your variables
```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CX=your_cx_key
```
5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
7. Run the Django Dev Server
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000/admin]
Login with the credentials you set up in step 6

8. (Optional) Run Celery for Background Tasks
Start Redis in one terminal
```bash
redis-server
```
Then in another terminal
```bash
celery -A backend worker --loglevel=info
```
9. Navigate to the Frontend Directory
```bash
cd frontend
```
10. Install Frontend Dependencies
```bash
npm install
```
11. Start the React Development Server
```bash
npm run dev
```
Visit [http://localhost:5173]

| Task                | Command                                                       |
| ------------------- | ------------------------------------------------------------- |
| Run backend server  | `python manage.py runserver`                                  |
| Run frontend server | `npm run dev`                                                 |
| Apply migrations    | `python manage.py makemigrations && python manage.py migrate` |
| Create admin        | `python manage.py createsuperuser`                            |
| Start Celery worker | `celery -A backend worker --loglevel=info`                    |
| Start Redis         | `redis-server`                                                |
