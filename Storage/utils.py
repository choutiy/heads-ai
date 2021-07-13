import zlib

import pandas as pd


def toDf(recs):
    return pd.DataFrame(
        {"id": [rec.internal_id for rec in recs],
         "author": [rec.author for rec in recs],
         "title": [rec.title for rec in recs],
         "content": [zlib.compress(rec.content.encode()) for rec in recs]
         }).set_index("id")