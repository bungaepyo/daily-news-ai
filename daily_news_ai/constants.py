# RSS Sources
RSS_SOURCES = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://rss.ft.com/rss/uk",
    # TODO: Add more RSS sources as needed
    # "https://www.wsj.com/xml/rss/3_7014.xml",
]

# LLM Config
KEYWORDS = [
  # "Technology",
  # "Finance",
  "Politics",
  # "Economy"
]
KEYWORD_SCORE_THRESHOLD = 0.5

# Exporter Config
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587