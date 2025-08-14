#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx
import random


def main() -> None:
    MAX_POKEMON_ID = 1025
    pokemon_id = random.randint(1, MAX_POKEMON_ID)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = httpx.get(url)
    response.raise_for_status()
    data = response.json()
    print(f"Random Pokémon: {data['name'].title()}")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")
    print(f"Sprite: {data['sprites']['front_default']}")


if __name__ == "__main__":
    main()
