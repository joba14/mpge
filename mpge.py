
# 
# @file mpge.py
# 
# @copyright This file is part of the "mpge" project and is distributed under
# "MIT" license.
# 
# @author joba14
# 


import pygame
import sys


class Transform:
	'''
	Transform defines position (x, y) and size (width, height).
	'''
	def __init__(self, x: int, y: int, width: int, height: int) -> None:
		self.x: int = x
		self.y: int = y
		self.width: int = width
		self.height: int = height

	def to_tuple(self) -> tuple[int]:
		'''
		Convert Transform object into a tuple of (x, y, width, height)
		'''
		return (self.x, self.y, self.width, self.height)


class Color:
	'''
	Transform defines a visible color (alpha is always set to 255).
	'''
	def __init__(self, r: int, g: int, b: int) -> None:
		self.r: int = r
		self.g: int = g
		self.b: int = b

	def to_tuple(self) -> tuple[int]:
		'''
		Convert Color object into a tuple of (r, g, b)
		'''
		return (self.r, self.g, self.b)

	@staticmethod
	def black() -> 'Color':
		'''
		Create black Color.
		'''
		return Color(0, 0, 0)

	@staticmethod
	def red() -> 'Color':
		'''
		Create red Color.
		'''
		return Color(255, 0, 0)
	
	@staticmethod
	def green() -> 'Color':
		'''
		Create green Color.
		'''
		return Color(0, 255, 0)
	
	@staticmethod
	def blue() -> 'Color':
		'''
		Create blue Color.
		'''
		return Color(0, 0, 255)

	@staticmethod
	def white() -> 'Color':
		'''
		Create white Color.
		'''
		return Color(255, 255, 255)


class Game:
	def __init__(self, title: str, width: int, height: int) -> None:
		pygame.init()
		pygame.font.init()
		pygame.display.set_caption(title)

		self._screen: pygame.Surface = pygame.display.set_mode((width, height))
		self._clock: pygame.time.Clock = pygame.time.Clock()
		self._font = pygame.font.SysFont(None, 36)

		self._entities: list = []
		self._textures: dict = {}
		self._running: bool = True

		self._run()

	def add_entity(self, entity: 'Entity') -> None:
		'''
		Add entity to the entities list.
		All entities, that are added to this list, get updated in the main program loop.
		'''
		self._entities.append(entity)

	def _run(self) -> None:
		self.create()
		for entity in self._entities:
			entity.create(self)

		while self._running:
			self.update()
			for entity in self._entities:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self._running = False
					elif event.type == pygame.KEYDOWN:
						if entity.inputtable:
							entity.on_inputted(self._map_pygame_key_to_str_key(event.key))

				entity.update(self)

				if entity.collidable:
					for other_entity in self._entities:
						if entity is other_entity:
							continue
						if other_entity.collidable:
							entity_rect: pygame.Rect = pygame.Rect(entity.transform.x, entity.transform.y, entity.transform.width, entity.transform.height)
							other_entity_rect: pygame.Rect = pygame.Rect(other_entity.transform.x, other_entity.transform.y, other_entity.transform.width, other_entity.transform.height)
							if entity_rect.colliderect(other_entity_rect):
								entity.on_collided(other_entity)
								other_entity.on_collided(entity)

			pygame.display.flip()
			self._clock.tick(60)

		pygame.quit()
		sys.exit()

	def create(self) -> None:
		pass

	def update(self) -> None:
		pass

	def get_screen_width(self) -> int:
		return self._screen.get_size()[0]
	
	def get_screen_height(self) -> int:
		return self._screen.get_size()[1]

	def fill_screen(self, color: Color) -> None:
		self._screen.fill(color.to_tuple())

	def draw_square(self, transform: Transform, color: Color) -> None:
		pygame.draw.rect(self._screen, color.to_tuple(), transform.to_tuple())

	def draw_texture(self, path: str, transform: Transform) -> None:
		'''
		Draw a texture. Note, that it accepts a path to a texture.
		If provided path of a texture is not loaded yet, it will load the texture. Otherwise, it will just use already-loaded texure.
		'''
		if path not in self._textures:
			self._textures[path] = pygame.image.load(path)

		texture = self._textures[path]
		texture: pygame.Surface = pygame.transform.scale(texture, (transform.width, transform.height))
		self._screen.blit(texture, (transform.x, transform.y))

	def draw_text(self, text: str, transform: Transform, color: Color):
		texture: pygame.Surface = self._font.render(text, True, color.to_tuple())
		texture = pygame.transform.scale(texture, (transform.width, transform.height))
		self._screen.blit(texture, (transform.x, transform.y))

	def _map_pygame_key_to_str_key(self, pygame_key: int) -> bool:
		key_map: dict = {
			pygame.K_LEFT: 'left',
			pygame.K_RIGHT: 'right',
			pygame.K_UP: 'up',
			pygame.K_DOWN: 'down',
			pygame.K_a: 'a',
			pygame.K_b: 'b',
			pygame.K_c: 'c',
			pygame.K_d: 'd',
			pygame.K_e: 'e',
			pygame.K_f: 'f',
			pygame.K_g: 'g',
			pygame.K_h: 'h',
			pygame.K_i: 'i',
			pygame.K_j: 'j',
			pygame.K_k: 'k',
			pygame.K_l: 'l',
			pygame.K_m: 'm',
			pygame.K_n: 'n',
			pygame.K_o: 'o',
			pygame.K_p: 'p',
			pygame.K_q: 'q',
			pygame.K_r: 'r',
			pygame.K_s: 's',
			pygame.K_t: 't',
			pygame.K_u: 'u',
			pygame.K_v: 'v',
			pygame.K_w: 'w',
			pygame.K_x: 'x',
			pygame.K_y: 'y',
			pygame.K_z: 'z',
			pygame.K_1: '1',
			pygame.K_2: '2',
			pygame.K_3: '3',
			pygame.K_4: '4',
			pygame.K_5: '5',
			pygame.K_6: '6',
			pygame.K_7: '7',
			pygame.K_8: '8',
			pygame.K_9: '9',
			pygame.K_0: '0',
			pygame.K_SPACE: 'space',
			# Add other key mappings as needed
		}
		key = key_map.get(pygame_key)
		return key


class Entity:
	def __init__(self) -> None:
		self.name: str = 'none'
		self.enabled: bool = False
		self.transform: Transform = Transform(0, 0, 0, 0)
		self.inputtable: bool = False
		self.collidable: bool = False

	def create(self, game: 'Game') -> None:
		pass

	def update(self, game: 'Game') -> None:
		pass

	def on_inputted(self, key: str) -> None:
		pass

	def on_collided(self, other: 'Entity') -> None:
		pass
