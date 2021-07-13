import bs4 as bs4

from Crawler import crawler, record


class TechCrunchCrawler(crawler.Crawler):
    # TODO: add pagination
    def parse(self):
        soup = bs4.BeautifulSoup(self.cache.text, "html.parser")
        recs = []

        for tag in soup.findAll("item"):
            tag_title = tag.find("title")
            tag_content = tag.find("content:encoded")
            tag_author = tag.find("dc:creator")
            tag_post_id = tag.find("post-id")
            r = record.Record(title=tag_title.get_text().strip(), author=tag_author.get_text().strip(),
                              content=tag_content.get_text().strip(), external_id=tag_post_id.get_text().strip())
            recs.append(r)
        self.storage.batchAddOrUpdate(recs)
