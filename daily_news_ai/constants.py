# RSS Sources
RSS_SOURCES = [
  # Wall Street Journal
  "https://feeds.content.dowjones.io/public/rss/RSSWorldNews",
  "https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness",
  "https://feeds.content.dowjones.io/public/rss/RSSMarketsMain",
  "https://feeds.content.dowjones.io/public/rss/RSSWSJD",
  "https://feeds.content.dowjones.io/public/rss/socialeconomyfeed",

  # Financial Times
  "https://www.ft.com/rss/home",
  "https://www.ft.com/energy?format=rss",
  "https://www.ft.com/industrials?format=rss",
  "https://www.ft.com/technology-sector?format=rss",
  "https://www.ft.com/transport?format=rss",
  "https://www.ft.com/artificial-intelligence?format=rss",
  "https://www.ft.com/semiconductors?format=rss",

  # Bloomberg
  "https://feeds.bloomberg.com/news.rss",
  "https://feeds.bloomberg.com/industries/news.rss",
  "https://feeds.bloomberg.com/economics/news.rss",
  "https://feeds.bloomberg.com/technology/news.rss",

  # Nikkei Asia
  "https://asia.nikkei.com/rss/feed/nar",

  # New York Times
  "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
  "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
  "https://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml",
  "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
  "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
  "https://rss.nytimes.com/services/xml/rss/nyt/Jobs.xml",
  "https://rss.nytimes.com/services/xml/rss/nyt/Automobiles.xml",

  # The Economist
  "https://www.economist.com/international/rss.xml",

  # Washington Post
  # "https://feeds.washingtonpost.com/rss/business/technology",
  # "https://feeds.washingtonpost.com/rss/business",
  
  # Politico
  "https://rss.politico.com/defense.xml",
  "https://rss.politico.com/economy.xml",
  "https://rss.politico.com/energy.xml",
  "https://rss.politico.com/morningtrade.xml",
  "https://rss.politico.com/morningtransportation.xml",
  "https://rss.politico.com/morningenergy.xml",
  "https://rss.politico.com/morningtech.xml",

  # South China Morning Post
  "https://www.scmp.com/rss/91/feed",
  "https://www.scmp.com/rss/318198/feed", # China > Policies & Politics
  "https://www.scmp.com/rss/318421/feed", # China > Economy, Business > China Economy
  "https://www.scmp.com/rss/92/feed",     # Business > Business
  "https://www.scmp.com/rss/10/feed",     # Business > Companies
  "https://www.scmp.com/rss/12/feed",     # Business > Global Economy
  "https://www.scmp.com/rss/36/feed",     # Tech > Tech
  "https://www.scmp.com/rss/320663/feed", # Tech > China Tech
  "https://www.scmp.com/rss/318218/feed", # Tech > Enterprises
  "https://www.scmp.com/rss/318222/feed", # Tech > Innovation
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