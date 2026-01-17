import json
import math
import pandas as pd
from db import engine
from sqlalchemy import text
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

def clean(obj):
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
    return obj

def ingest_data(path):
    df = pd.read_csv(path, dtype=str, low_memory=False)

    stmt = text(
        """
        INSERT INTO sales_embeddings (content, embedding, metadata)
        VALUES (:content, :embedding, :metadata)
        """
    )

    count=0
    with engine.begin() as conn:
        for _, row in df.iterrows():
            count += 1
            row_dict = {k: clean(v) for k, v in row.to_dict().items()}
            content = " | ".join([f"{k}: {v}" for k, v in row_dict.items()])
            embedding = embeddings.embed_query(content)
            print("Ingesting...", content)
            conn.execute(stmt, {
                "content": content,
                "embedding": embedding,
                "metadata": json.dumps(row_dict)
            })
            if count > 50:
                break

    return df
