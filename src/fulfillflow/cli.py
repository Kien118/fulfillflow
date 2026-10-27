import typer
from rich.console import Console

from fulfillflow import __version__

app = typer.Typer(
    name="fulfillflow",
    help="FulfillFlow data platform.",
    no_args_is_help=True,
)

console = Console()


@app.callback()
def main() -> None:
    """Run FulfillFlow commands."""


@app.command()
def version() -> None:
    """Print the installed FulfillFlow version."""
    console.print(f"FulfillFlow {__version__}")
