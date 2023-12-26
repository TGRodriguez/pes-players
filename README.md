# pes-players

# Installing the project

This project was build with [poetry](https://python-poetry.org/docs/) to manage dependencies.

Having poetry installed, run this command to install the dependencies:

```
poetry install
```

## Dev

To add new dependencies, you can run:

```
poetry add <dependency>
```

**NOTE**: Don't forget to commit all changes to `poetry.lock` and `pyproject.toml`! 

To activate the virtual environment run:

```
poetry shell
```

Then, you can run the app using:

```
python src/main.py
```

To run the formatter:

```
black [Options] path
```

To run the linter:

```
flakeheaven lint path
```

## Running locally

In addition to running it directly within poetry's virtual environment you can run the project with Docker:

* Create a `.env` file with the same environment variables as in `.example-env`

* Run `docker build -t pes-players .`

* Run `docker run -p PORT:PORT --env-file=.env pes-players`