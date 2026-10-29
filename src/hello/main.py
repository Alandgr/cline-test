"""Hello world greeting module."""
import argparse


def greet(name: str = "World") -> str:
    """Return a greeting for the given name.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string in the form "Hello, {name}!".
    """
    return f"Hello, {name}!"


def main() -> None:
    """Parse arguments and print a greeting to stdout."""
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
