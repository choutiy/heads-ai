import pandas as pd

from Storage import utils


class Storage:
    def __init__(self, name):
        self.name = name
        self.path = "../Storage/Files/" + name + ".csv"
        self.df = pd.read_csv(self.path, index_col="id")
        self.dfByAuthor = self.df.groupby(by="author")

    def batchAddOrUpdate(self, recs):
        self.df = utils.toDf(recs).combine_first(self.df)
        self.df.to_csv(self.path, index_label="id", encoding='utf8')
        self.dfByAuthor = self.df.groupby(by="author")

    def getAllArticles(self):
        return utils.toRecs(self.df)

    def getArticlesByAuthor(self, author):
        if author not in self.dfByAuthor.groups.keys():
            return []
        articles = self.df.loc[self.dfByAuthor.groups.get(author)]
        return utils.toRecs(articles)

    def getAllAuthors(self):
        return self.dfByAuthor.groups.keys()
