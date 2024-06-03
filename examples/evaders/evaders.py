
# 
# @file mpge.py
# 
# @copyright This file is part of the "mpge" project and is distributed under
# "MIT" license.
# 
# @author joba14
# 


from mpge import Transform, Color, Game, Entity

import random


class Rocket(Entity):
	WIDTH: int = 50
	HEIGHT: int = 100

	def __init__(self, rows: list[int]) -> None:
		super().__init__()
		self._rows: list[int] = rows

	def create(self, game: Game) -> None:
		self._current_row: int = len(self._rows) // 2

		self.name = 'rocket'
		self.enabled = True
		self.transform = Transform(self._rows[self._current_row] + (Rocket.WIDTH // 2), game.get_screen_height() - Rocket.HEIGHT, Rocket.WIDTH, Rocket.HEIGHT)
		self.inputtable = True
		self.collidable = True

	def update(self, game: Game) -> None:
		self.transform.x = self._rows[self._current_row] + (Rocket.WIDTH // 2)
		game.draw_texture('./rocket.png', self.transform)

	def on_inputted(self, key: str) -> None:
		if key == 'left':
			if self._current_row > 0:
				self._current_row -= 1
		if key == 'right':
			if self._current_row < len(self._rows) - 1:
				self._current_row += 1

	def on_collided(self, other: Entity) -> None:
		if other.name == 'asteroid':
			exit(0)


class Asteroid(Entity):
	WIDTH: int = 100
	HEIGHT: int = 100

	def __init__(self, rows: list[int]) -> None:
		super().__init__()
		self._rows: list[int] = rows

	def create(self, game: Game) -> None:
		self.old_x: int = -1
		self.y_speed: int = 3

		self.name = 'asteroid'
		self.enabled = True
		self.transform = Transform(self.get_random_x(), -Asteroid.HEIGHT, Asteroid.WIDTH, Asteroid.HEIGHT)
		self.collidable = True

	def get_random_x(self) -> int:
		for i in range(0, 5):
			x: int = self._rows[random.randint(0, (len(self._rows) - 1))]
			if x != self.old_x:
				self.old_x = x
				if self.y_speed <= 8:
					self.y_speed += 1
				break
		return x

	def update(self, game: Game) -> None:
		if self.transform.y + self.transform.height < game.get_screen_width() + Asteroid.WIDTH:
			self.transform.y += self.y_speed
			game.draw_texture('./asteroid.png', self.transform)
		else:
			self.transform = Transform(self.get_random_x(), -Asteroid.HEIGHT, Asteroid.WIDTH, Asteroid.HEIGHT)

	def on_collided(self, other: Entity) -> None:
		if other.name == 'rocket':
			self.enabled = False


class MyGame(Game):
	def create(self):
		self._rows_count: int = 5
		self._rows: list[int] = [row * ((self.get_screen_width() - Asteroid.WIDTH) / (self._rows_count - 1)) for row in range(0, self._rows_count)]

		self.add_entity(Rocket(self._rows))
		self.add_entity(Asteroid(self._rows))
		self.add_entity(Asteroid(self._rows))
		self.add_entity(Asteroid(self._rows))

	def update(self):
		self.fill_screen(Color.black())


MyGame('my game', 600, 400)
