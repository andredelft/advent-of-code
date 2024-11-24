from setuptools import setup

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="advent-of-code",
    version="0.1.0",
    py_modules=["cli"],
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "prepare=cli:prepare",
            "test-sol=cli:test",  # We can't use `test`
            "solve=cli:solve",
            "submit=cli:submit",
        ]
    },
)
