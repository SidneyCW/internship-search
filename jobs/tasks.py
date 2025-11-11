from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Job
from datetime import date, timedelta
from django.conf import settings
import time

@shared_task
def fetch_google_jobs():
    """Fetch recent jobs using Google Custom Search and extract full descriptions."""
    base_url = "https://www.googleapis.com/customsearch/v1"
    week_ago = (date.today() - timedelta(days=7)).isoformat()
    location = "Toronto"
    query = f'"Software Engineer Internship" "{location}" site:linkedin.com/jobs after:{week_ago}'

    params = {
        "key": settings.GOOGLE_API_KEY,
        "cx": settings.GOOGLE_CX,
        "q": query,
    }

    try:
        res = requests.get(base_url, params=params)
        res.raise_for_status()
        results = res.json().get("items", [])

        print(f"🔍 Found {len(results)} job results from Google")

        for item in results:
            url = item.get("link")
            snippet = item.get("snippet", "")
            title = item.get("title", "No title")


            full_desc = snippet
            try:
                html = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"}).text
                soup = BeautifulSoup(html, "lxml")

                if "indeed" in url:
                    job_text = soup.find("div", {"id": "jobDescriptionText"})
                    company_tag = soup.find("div", {"class": "jobsearch-CompanyInfoWithoutHeaderImage"})
                elif "linkedin" in url:
                    job_text = soup.find("div", {"class": "show-more-less-html__markup"})
                    company_tag = soup.find("a", {"class": "topcard__org-name-link"})
                else:
                    job_text = " ".join([p.get_text() for p in soup.find_all("p")[:6]])
                    company_tag = None

                full_desc = job_text.get_text(strip=True) if job_text else snippet
                company = company_tag.get_text(strip=True) if company_tag else "Unknown"

            except Exception as scrape_err:
                print(f"⚠️ Could not scrape {url}: {scrape_err}")

            Job.objects.get_or_create(
                url=url,
                defaults={
                    "title": title,
                    "company": company,
                    "description": full_desc,
                    "location": "Remote",
                },
            )
            import random
            time.sleep(random.uniform(1, 2.5))

        print("✅ Job fetching complete")

    except Exception as e:
        print(f"⚠️ Error fetching jobs: {e}")

