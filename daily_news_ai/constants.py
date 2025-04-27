# Publisher RSS sources
RSS_SOURCES = [
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://rss.ft.com/rss/uk",
    # TODO: Add more RSS sources as needed
    # "https://www.wsj.com/xml/rss/3_7014.xml",
]

# AI model configuration
KEYWORDS = [
  # "Technology",
  # "Finance",
  "Politics",
  # "Economy"
]
KEYWORD_SCORE_THRESHOLD = 0.5

# Email configuration
EMAIL_RECIPIENTS = [
  "bungaepyo@gmail.com"
]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587