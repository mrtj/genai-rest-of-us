from typing import Literal
import base64
from IPython.display import Image, display

def mermaid(
    graph: str,
    width: int = 500,
    height: int = 500,
    theme: Literal["light", "dark"] = "dark",
    background_color: str = "!transparent",
    verbose: bool = False,
):
    graph = "%%{init: {'theme':'" + theme + "'} }%%\n" + graph
    graph_bytes = graph.encode("ascii")
    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    url = "https://mermaid.ink/svg/" + base64_string
    if background_color is not None:
        url += f"?bgColor={background_color}"
    if verbose:
        print(url)
    display(Image(url=url, width=width, height=height))


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
