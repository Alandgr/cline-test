"""Tests for hello.main module."""
import subprocess
import sys
from unittest.mock import patch

from hello.main import greet, main


def test_greet_default():
    """greet() with no argument returns 'Hello, World!'."""
    assert greet() == "Hello, World!"


def test_greet_custom_name():
    """greet(name) returns a personalized greeting."""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    """greet('') returns 'Hello, !'."""
    assert greet("") == "Hello, !"


def test_main_default(capsys):
    """main() prints the default greeting."""
    with patch("sys.argv", ["hello"]):
        main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def test_main_custom_name(capsys):
    """main() prints a personalized greeting when --name is given."""
    with patch("sys.argv", ["hello", "--name", "Alice"]):
        main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_module_execution():
    """Running the package as a module prints the default greeting."""
    result = subprocess.run(
        [sys.executable, "-m", "hello"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello, World!"


def test_module_execution_with_name():
    """Running the package with --name prints a personalized greeting."""
    result = subprocess.run(
        [sys.executable, "-m", "hello", "--name", "Alice"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello, Alice!"
