
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge)](./license.md)
![Language Support](https://img.shields.io/badge/languages-Python-brightgreen.svg?style=for-the-badge)


# MPGE: Minimalist Python Game Engine
MPGE is a lightweight game engine built on top of Pygame. It provides basic structures and functionalities to create simple 2D games.

## Table of Contents
- [Features](#features)
- [API](#api)
	- [Transform](#transform)
	- [Color](#color)
	- [Game](#game)
	- [Entity](#entity)
- [Examples](#examples)
- [License](#license)


## Features
- Basic game loop management
- Entity system for managing game objects
- Transform class for position and size management
- Color class for handling colors
- Basic collision detection
- Texture and text rendering

[(to the top)](#mpge-minimalist-python-game-engine)


## API
### Transform
Defines the position (x, y) and size (width, height) of an object. Here is the API of the Transform:
#### Methods
- `__init__(self, x: int, y: int, width: int, height: int) -> None`
- `to_tuple(self) -> tuple[int]`

### Color
Defines a visible color. Here is the API of the Color:
- `__init__(self, r: int, g: int, b: int) -> None`
- `to_tuple(self) -> tuple[int]`
- `@staticmethod black() -> 'Color'`
- `@staticmethod red() -> 'Color'`
- `@staticmethod green() -> 'Color'`
- `@staticmethod blue() -> 'Color'`
- `@staticmethod white() -> 'Color'`

### Game
The main game class that initializes and runs the game loop. Here is the API of the Game:
#### Methods
- `__init__(self, title: str, width: int, height: int) -> None`
- `add_entity(self, entity: 'Entity') -> None`
- `create(self) -> None`
- `update(self) -> None`
- `get_screen_width(self) -> int`
- `get_screen_height(self) -> int`
- `fill_screen(self, color: Color) -> None`
- `draw_square(self, transform: Transform, color: Color) -> None`
- `draw_texture(self, path: str, transform: Transform) -> None`
- `draw_text(self, text: str, transform: Transform, color: Color)`

### Entity
Base class for all game entities. Here is the API of the Entity:
#### Methods
- `__init__(self) -> None`
- `create(self, game: 'Game') -> None`
- `update(self, game: 'Game') -> None`
- `on_inputted(self, key: str) -> None`
- `on_collided(self, other: 'Entity') -> None`

[(to the top)](#mpge-minimalist-python-game-engine)


## Examples
Example games and projects can be founf in the [examples directory](./examples/).

[(to the top)](#mpge-minimalist-python-game-engine)


## License
The MPGE project is released under the MIT license. Users and contributors are required to review and comply with the license terms specified in the [license.md file](./license.md). The license outlines the permitted usage, distribution, and intellectual property rights associated with the MPGE project.

Please refer to the [license.md file](./license.md) for more details. By using, modifying, or distributing the MPGE project, you agree to be bound by the terms and conditions of the license.

[(to the top)](#mpge-minimalist-python-game-engine)
