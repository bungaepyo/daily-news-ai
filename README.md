# daily-news-ai

daily-news-ai is a project designed to scrape and filter news articles from top RSS sources, and curate them with LLM. The goal of the project is to automatically identify and prioritize articles based on user-defined interests and deliver via email.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m daily_news_ai.main
```

## Environment Variables

Create a `.env` file in the root directory with the following content:

```
EMAIL_RECIPIENTS=["your_email@example.com"]
SENDER_EMAIL=your_email@example.com
PASSWORD=your_email_password (App-specific password)
```
