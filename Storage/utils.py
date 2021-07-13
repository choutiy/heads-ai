import pandas as pd


def toDf(recs):
    return pd.DataFrame(
        {"title": [rec.title for rec in recs],
         "content": [rec.title for rec in recs],
         "author": [rec.title for rec in recs],
         "id": [rec.internal_id for rec in recs]}).set_index("id")