from collections import defaultdict
import requests
import certifi
import feedparser
import smtplib
import os
import json
from dotenv import load_dotenv
import email.utils as eut
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from daily_news_ai.constants import (
    KEYWORD_SCORE_THRESHOLD,
    KEYWORDS,
    SMTP_SERVER,
    SMTP_PORT,
)

# Load environment variables from .env file
load_dotenv()

def get_publisher_from_url(url):
    if "nytimes" in url:
        return "New York Times"
    elif "ft" in url:
        return "Financial Times"
    # TODO: add more publishers as needed
    return "Unknown"


def format_date(published):
    parsed_date = eut.parsedate_to_datetime(published)
    formatted_date = parsed_date.strftime("%m/%d, %H:%M") if parsed_date else published
    return formatted_date
    

def fetch_articles_from_rss(rss_sources: list[str]) -> list[dict]:
    articles = []
    for url in rss_sources:
        response = requests.get(url, verify=certifi.where())
        feed = feedparser.parse(response.text)
        publisher = get_publisher_from_url(url)
        for entry in feed.entries:
            article = {
                'publisher': publisher,
                'title': entry.title,
                'link': entry.link,
                'description': entry.description,
                'published': entry.published,
            }
            articles.append(article)
    return articles


def classify_article(article_content: str, candidate_labels: list[str], classifier) -> float:
    result = classifier(article_content, candidate_labels)
    return result['scores'][0]


def filter_keyword_articles(articles: list[dict], keywords: list[str], classifier) -> list[dict]:
    keyword_articles = []
    for article in articles:
        score = classify_article(f"{article['title']}. {article['description']}", keywords, classifier)
        if score > KEYWORD_SCORE_THRESHOLD:
            keyword_articles.append(article)
    return keyword_articles


def group_articles_by_publisher(articles: list[dict]) -> dict[str, list[dict]]:
    articles_by_publisher = defaultdict(list)
    for article in articles:
        publisher = article['publisher']
        articles_by_publisher[publisher].append(article)
    return articles_by_publisher


def format_keyword_articles(keyword_articles: list[dict]) -> str:
    body = f"<h3>By Keyword: {KEYWORDS[0]}</h3>"
    body += "<ul>"
    for article in keyword_articles:
        publisher = article['publisher']
        title = article['title']
        link = article['link']
        published = article['published']
        formatted_date = format_date(published)
        body += f"<li>{publisher}: <a href='{link}'>{title}</a> (Published {formatted_date})</li>"
    body += "</ul>"
    return body


def format_publisher_articles(articles_by_publisher: dict[str, list[dict]]) -> str:
    body = "<h3>By Publisher</h3>"
    for publisher, articles in articles_by_publisher.items():
        body += f"<h4>{publisher}</h4>"
        body += "<ul>"
        for article in articles:
            title = article['title']
            link = article['link']
            published = article['published']
            formatted_date = format_date(published)
            body += f"<li><a href='{link}'>{title}</a> (Published {formatted_date})</li>"
        body += "</ul>"
    return body


def send_email(subject: str, body: str):
    sender_email = os.getenv("SENDER_EMAIL")
    if not sender_email:
        raise ValueError("Sender email not found in environment variables.")
    
    recipient_emails = json.loads(os.getenv("EMAIL_RECIPIENTS"))
    if not recipient_emails:
        raise ValueError("Recipient emails not found in environment variables.")

    password = os.getenv("PASSWORD")
    if not password:
        raise ValueError("Password not found in environment variables.")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ",".join(recipient_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, ",".join(recipient_emails), msg.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
