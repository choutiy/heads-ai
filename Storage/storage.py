import pandas as pd

from Storage import utils


class Storage:
    def __init__(self, name):
        self.name = name
        self.path = "Storage/Files/" + name + ".csv"
        self.df = pd.read_csv(self.path, index_col="id")

    def batchAddOrUpdate(self, recs):
        self.df = utils.toDf(recs).combine_first(self.df)
        self.df.to_csv(self.path, index_label="id")


