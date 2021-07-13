import pandas as pd

from Storage import utils


class Storage:
    def __init__(self, name):
        self.name = name
        self.path = "Storage/Files/" + name + ".csv"
        self.df = pd.read_csv(self.path, index_col="id")

    def batchAddOrUpdate(self, recs):
        pass


