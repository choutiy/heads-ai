import yaml
from flask import Flask
from flask_restful import Resource, Api

from Crawler import techcrunch_crawler
from Storage import storage

app = Flask(__name__)
api = Api(app)
with open("../Config/techcrunch.yaml", "r") as f:
    config = yaml.safe_load(f)
tc = techcrunch_crawler.TechCrunchCrawler(
    config.get("name"),
    config.get("source_url"),
    storage.Storage(config.get("name"))
)
tc.parse()
print("Done with loading TC articles.")


# ArticleList
# shows a list of all articles
class ArticleList(Resource):
    def get(self):
        return tc.storage.getAllArticles()

    def put(self):
        raise NotImplementedError('POST not implemented for ArticleList')


# AuthorList
# shows a list of all authors
class AuthorList(Resource):
    def get(self):
        return tc.storage.getAllArticles()

    def put(self):
        raise NotImplementedError('POST not implemented for AuthorList')


# ArticleByAuthor
# shows a list of all articles by a given author
class ArticleByAuthor(Resource):
    def get(self, author):
        return tc.storage.getArticlesByAuthor(author)

    def put(self):
        raise NotImplementedError('POST not implemented for ArticleByAuthor')


api.add_resource(ArticleList, '/articles')
api.add_resource(AuthorList, '/authors')
api.add_resource(ArticleByAuthor, '/articles/<author>')

if __name__ == '__main__':
    app.run(debug=True)
