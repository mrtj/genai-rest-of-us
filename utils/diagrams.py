from . import mermaid

def rag(**kwargs):
    return mermaid(f"""
    graph LR
        question(Question) --> prompt(Prompt)
        question --> vector_store(Vector Store)
        vector_store -- Retrieved<br/>documents --> prompt(Prompt)
        prompt(Prompt) --> LLM
        LLM --> response(Response)
    """,
        height=kwargs.pop("height", 200),
        width=kwargs.pop("width", 800),
        **kwargs,
    )
