import zlib

import pandas as pd

from Crawler import record


def toRec(article, id):
    return record.Record(title=article.title, author=article.author,
                         content=str(zlib.decompress(article.content)),
                         id=id)


def toRecs(df):
    return [toRec(article, id) for id, article in df.iterrows()]


def toDf(recs):
    return pd.DataFrame(
        {"id": [rec.internal_id for rec in recs],
         "author": [rec.author for rec in recs],
         "title": [rec.title for rec in recs],
         "content": [zlib.compress(rec.content.encode()) for rec in recs]
         }).set_index("id")