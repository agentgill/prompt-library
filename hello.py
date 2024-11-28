import typer

app = typer.Typer(name="prompt-library")


@app.command()
def hello():
    print("Hello from prompt-library!")


if __name__ == "__main__":
    app()
