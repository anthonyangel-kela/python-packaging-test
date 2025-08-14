#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
#     "httpx",
#     "rich",
# ]
# ///

import random
import httpx
import typer
from rich import print

app = typer.Typer(help="Pokémon CLI powered by uv, Typer, and Rich.")


@app.command(help="Get a random Pokémon's details from the PokéAPI.")
def random_pokemon():
    MAX_POKEMON_ID = 1025
    pokemon_id = random.randint(1, MAX_POKEMON_ID)
    fetch_pokemon(pokemon_id)


@app.command(help="Get Pokémon details by name or ID. Example: get pikachu or get 25.")
def get(
    name_or_id: str = typer.Argument(
        ..., help="Pokémon name (e.g. 'pikachu') or ID (e.g. '25')."
    ),
):
    fetch_pokemon(name_or_id)


def fetch_pokemon(identifier):
    url = f"https://pokeapi.co/api/v2/pokemon/{identifier}"
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
    except httpx.RequestError as exc:
        print(f"[red]Request error:[/] {exc}")
        raise typer.Exit(1)
    except httpx.HTTPStatusError as exc:
        print(f"[red]HTTP error {exc.response.status_code}:[/] {exc.response.text}")
        raise typer.Exit(1)
    data = response.json()
    print(f"[bold green]Pokémon:[/] {data['name'].title()}")
    print(f"[bold]ID:[/] {data['id']}")
    print(f"[bold]Height:[/] {data['height']}")
    print(f"[bold]Weight:[/] {data['weight']}")
    print(f"[bold]Sprite:[/] {data['sprites']['front_default']}")


if __name__ == "__main__":
    app()
