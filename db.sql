CREATE DATABASE retail;

CREATE EXTENSION vector;

CREATE TABLE sales_embeddings (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536),
    metadata JSONB
);

CREATE INDEX sales_embedding_idx
ON sales_embeddings
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);