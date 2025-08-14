
# Python App Examples with uv

This repository demonstrates four ways to run Python apps using [uv](https://docs.astral.sh/uv/):

## 1. uv Script
- Directory: `uv-script`
- Example: Standalone script with uv shebang and inline dependencies.
- Run:
	```sh
	cd uv-script
	./pokemon.py
	```

## 2. uv Project
- Directory: `uv-project`
- Example: Python project managed by uv with `pyproject.toml`.
- Run:
	```sh
	cd uv-project
	uv run main.py
	```

## 3. CLI via uv Script
- Directory: `cli-uv-script`
- Example: Typer CLI as a uv script with shebang and inline dependencies.
- Run:
	```sh
	cd cli-uv-script
	./pokemon_cli.py --help
	./pokemon_cli.py random-pokemon
	./pokemon_cli.py get pikachu
	```

## 4. CLI via uv Project
- Directory: `cli-uv-project`
- Example: Typer CLI as a uv project with `pyproject.toml` and entry point.
- Run:
	```sh
	cd cli-uv-project
	uv run pokemon-cli get pikachu
	uv run pokemon-cli random-pokemon
	uv run pokemon-cli --help
	```


	### Publishing & Installing the CLI Package



	You can install the `cli-uv-project` CLI tool globally using `uv tool install` once it is published to a package index (such as PyPI or a private index).

	```sh
	uv tool install cli-uv-project
	# Now you can run:
	pokemon-cli get pikachu
	pokemon-cli random-pokemon
	pokemon-cli --help
	```

	Replace `cli-uv-project` with your published package name if different.

	#### CLI Autocompletion

	The CLI tool supports autocompletion for shells (e.g., bash, zsh, fish). To enable autocompletion, run:

	```sh
	pokemon-cli --install-completion
	```

	Follow the instructions printed to your shell to activate completion.


---

## Comparison Table: Pros & Cons

| Approach            | Usability                          | Portability (No Python Setup) | Extensibility                | Testability                  |
|---------------------|------------------------------------|-------------------------------|------------------------------|------------------------------|
| **uv Script**       | Easiest for single-file scripts; run directly with shebang | High (uv handles env, no manual Python needed) | Limited (harder to scale to multi-file/project) | Low (testing inline or with manual setup) |
| **uv Project**      | Good for apps with multiple files; standard project structure | High (uv manages env, dependencies, Python)    | High (easy to add modules, dependencies)        | High (supports test directories, tools)   |
| **CLI via uv Script** | Simple CLI, quick prototyping; run directly | High (uv handles env, no manual Python needed) | Moderate (can add commands, but single file)    | Low (testing inline or with manual setup) |
| **CLI via uv Project** | Best for production CLI tools; installable entry points | High (uv manages env, dependencies, Python)    | High (easy to extend, add commands, package)    | High (supports test directories, tools)   |

**Notes:**
- All uv approaches are highly portable and do not require a complicated local Python setup; uv manages everything.
- For extensibility and testability, prefer the project-based approaches.
- For quick scripts or prototyping, script-based approaches are fastest.
