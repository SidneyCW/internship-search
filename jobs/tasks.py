from celery import shared_task
import requests
from .models import Job
from datetime import date, timedelta
from django.conf import settings

@shared_task
def fetch_google_jobs():
    """Fetch recent jobs using Google Custom Search and save them to DB."""
    base_url = "https://www.googleapis.com/customsearch/v1"
    week_ago = (date.today() - timedelta(days=7)).isoformat()
    query = f'"Software Engineer Internship" site:indeed.com OR site:linkedin.com/jobs after:{week_ago}'

    params = {
        "key": settings.GOOGLE_API_KEY,
        "cx": settings.GOOGLE_CX,
        "q": query,
    }

    try:
        res = requests.get(base_url, params=params)
        data = res.json().get("items", [])

        for item in data:
            Job.objects.get_or_create(
                url=item.get("link"),
                defaults={
                    "title": item.get("title", "No title"),
                    "company": "Unknown",
                    "description": item.get("snippet", ""),
                    "location": "Remote",
                },
            )

        print(f"✅ Fetched {len(data)} jobs from Google API")

    except Exception as e:
        print(f"⚠️ Error fetching jobs: {e}")
