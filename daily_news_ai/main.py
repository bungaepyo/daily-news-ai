from transformers import pipeline
from daily_news_ai.constants import (
    RSS_SOURCES,
    KEYWORDS,
)
from daily_news_ai.helper import (
    fetch_articles_from_rss,
    group_articles_by_keyword,
    group_articles_by_publisher,
    format_keyword_articles,
    format_publisher_articles,
    send_email,
)

def main():
    print("Fetching articles from RSS feeds...")
    articles = fetch_articles_from_rss(RSS_SOURCES)
  
    print("Filtering articles based on keywords...")
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    articles_by_keyword = group_articles_by_keyword(articles, KEYWORDS, classifier)

    print("Grouping articles by publisher...")
    articles_by_publisher = group_articles_by_publisher(articles)

    print("Formatting articles for email...")
    keyword_body = format_keyword_articles(articles_by_keyword)
    publisher_body = format_publisher_articles(articles_by_publisher)
    body = keyword_body + "\n" + publisher_body

    print("Generating email...")
    send_email("Daily News AI: Today's Articles", body)

if __name__ == "__main__":
    main()
  