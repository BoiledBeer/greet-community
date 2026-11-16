"""Greeting tools for the community."""


def greet(name: str) -> str:
    """Return a greeting; use "world" for a blank name."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
