from typer import Typer, Option, Argument
from llm_evaluator import __version__


app = Typer(
    name="llm-evaluator",
    help="A flexible task evaluation client",
    no_args_is_help=True,
)


# TODO add commands here when defined


@app.callback()
def main(
    ctx: Typer.Context,
    version: bool = Option(
        False,
        "--version",
        "-v",
        help="Show the version of the LLM Evaluator.",
    ),
):
    """
    A flexible task evaluation client.
    """
    if version:
        ctx.exit(f"LLM Evaluator version: {__version__}")
