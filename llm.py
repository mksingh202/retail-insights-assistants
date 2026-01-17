from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

def answer_with_context(question, context):
    context_block = "\n".join(context)

    prompt = f"""
        You are a retail data analyst.

        Use ONLY the context below to answer.
        If insufficient data, say so clearly.

        Context:
        {context_block}

        Question:
        {question}

        Answer in clear, business-friendly language.
    """

    return llm.invoke(prompt).content
