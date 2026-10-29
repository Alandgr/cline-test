"""Tests for hello.main module."""

from hello.main import greet


def test_greet_default():
    """greet() with no argument returns 'Hello, World!'."""
    assert greet() == "Hello, World!"


def test_greet_custom_name():
    """greet(name) returns a personalized greeting."""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    """greet('') returns 'Hello, !'."""
    assert greet("") == "Hello, !"
