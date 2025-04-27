from setuptools import setup, find_packages

setup(
    name="daily_news_ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
      "feedparser",
      "certifi",
      "requests",
      "torch",
      "transformers",
      "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "daily_news_ai=daily_news_ai.main:main",
        ],
    },
)