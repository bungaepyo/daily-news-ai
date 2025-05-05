# RSS Sources
RSS_SOURCES = [
  # Wall Street Journal
  # Note: Only provides RSS feed by category (https://www.wsj.com/news/rss-news-and-feeds)
  "https://feeds.content.dowjones.io/public/rss/RSSWorldNews",
  "https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness",
  "https://feeds.content.dowjones.io/public/rss/RSSMarketsMain",
  "https://feeds.content.dowjones.io/public/rss/RSSWSJD",

  # Financial Times
  "https://www.ft.com/rss/home",

  # Bloomberg
  "https://feeds.bloomberg.com/news.rss"

  # Nikkei Asia
  "https://asia.nikkei.com/rss/feed/nar",

  # New York Times
  "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",

  # The Economist
  # Note: Only provides RSS feed by category
  "https://www.economist.com/international/rss.xml",

  # Washington Post
  # Note: Only provides RSS feed by category
  # TODO: washington post throws a ConnectionResetError
  # "https://feeds.washingtonpost.com/rss/politics",
  # "https://feeds.washingtonpost.com/rss/business/technology",
  # "https://feeds.washingtonpost.com/rss/national",
  # "https://feeds.washingtonpost.com/rss/world",
  # "https://feeds.washingtonpost.com/rss/business",
  
  # Politico
  # Note: Only provides RSS feed by category (https://www.politico.com/rss)
  "https://rss.politico.com/congress.xml",
  "https://rss.politico.com/healthcare.xml",
  "https://rss.politico.com/defense.xml",
  "https://rss.politico.com/economy.xml",
  "https://rss.politico.com/energy.xml",
  "https://rss.politico.com/politics-news.xml",


  # South China Morning Post
  "https://www.scmp.com/rss/91/feed",
]

# LLM Config
KEYWORDS = [
  # "Technology",
  # "Finance",
  "Politics",
  # "Economy"
]
KEYWORD_SCORE_THRESHOLD = 0.75

# Exporter Config
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587