"""Simple application for the CI/CD final project."""


def greet(name):
    """Return a greeting for the supplied name."""
    if not name or not name.strip():
        return "Hello, World!"
    return f"Hello, {name.strip()}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("CI/CD Final Project"))
