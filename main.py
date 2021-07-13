import yaml

from Crawler import techcrunch_crawler
from Storage import storage

with open("Config/techcrunch.yaml", "r") as f:
    config = yaml.safe_load(f)
    tc = techcrunch_crawler.TechCrunchCrawler(
            config.get("name"),
            config.get("source_url"),
            storage.Storage(config.get("name"))
            )
    tc.parse()
    print("Done with loading TC articles.")
    print("\nTest getArticlesByAuthor:\n")

    for rec in tc.storage.getArticlesByAuthor("Catherine Shu"):
        print(rec)
    print("\nTest getAllArticles:\n")
    for rec in tc.storage.getAllArticles():
        print(rec)
    print("\nTest getAllAuthors:\n")
    for rec in tc.storage.getAllAuthors():
        print(rec)
