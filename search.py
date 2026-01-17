from db import engine
from sqlalchemy import text
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

def retrieve_context(question, top_k=5):
    query_embedding = embeddings.embed_query(question)

    sql = text(
        """
        SELECT content
        FROM sales_embeddings
        ORDER BY embedding <-> (:embedding)::vector
        LIMIT :k
        """
    )
    
    with engine.connect() as conn:
        rows = conn.execute(
            sql, {"embedding": query_embedding, "k": top_k}
        ).fetchall()

    return [r.content for r in rows]
