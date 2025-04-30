from setuptools import setup, find_packages

setup(
    name="llm-evaluator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.15.2",
        "ollama>=0.4.8",
        "openai>=1.75.0",
        "beartype>=0.20.2",
    ],
    entry_points={
        "console_scripts": [
            "evaluate=llm_evaluator.cli.main:main",
        ],
    },
    author="",
    author_email="",
    description="A flexible task evaluation client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tenacke/llm-evaluator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.12",
)
