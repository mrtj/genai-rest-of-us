from typing import Literal
import os, getpass
import base64
from IPython.display import Image, display  # type: ignore

from dotenv import load_dotenv

load_dotenv()

def ensure_openai_api_key():
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key:")

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
