
# 
# @file mpge.py
# 
# @copyright This file is part of the "mpge" project and is distributed under
# "MIT" license.
# 
# @author joba14
# 


from mpge import Transform, Color, Game, Entity


class Cell:
	WIDTH: int = 100
	HEIGHT: int = 100

	def __init__(self, index: int, x: int, y: int) -> None:
		super().__init__()
		self.index: int = index
		self.x: int = x
		self.y: int = y
		self.symbol: str | None = None


class GameManager(Entity):
	def create(self, game: Game) -> None:
		self.name = 'game manager'
		self.enabled = True
		self.inputtable = True

		self._cells: list[Cell] = []
		for index in range(0, 9):
			self._cells.append(Cell(index, index % 3, index // 3))

		self._current_player: str = 'X'
		self._at_least_one_move_was_done: bool = False
		self._is_it_a_draw: bool = False
		self._is_finished: bool = False

	def update(self, game: Game) -> None:
		if self._is_finished:
			if not self._is_it_a_draw:
				winner: str = 'O' if self._current_player == 'X' else 'X'
				text: str = f'Player {winner} has won!'
			else:
				text: str = f'It\'s a draw...'
			game.draw_text(text, Transform(game.get_screen_width() / 2 - 100, game.get_screen_height() / 2 - 20, 200, 40), Color.black())
			return

		for cell in self._cells:
			transform: Transform = Transform(cell.x * Cell.WIDTH, cell.y * Cell.HEIGHT, Cell.WIDTH, Cell.HEIGHT)
			if cell.symbol == 'X':
				game.draw_texture('./X.png', transform)
			elif cell.symbol == 'O':
				game.draw_texture('./O.png', transform)
			else:
				transform.width /= 4
				transform.height /= 4
				transform.x += transform.width * 1.5
				transform.y += transform.height * 1.5
				game.draw_text(f'{cell.index + 1}', transform, Color.black())

		if not self._at_least_one_move_was_done:
			return
		
		if  (self._cells[1].symbol is not None and (self._cells[0].symbol == self._cells[1].symbol and self._cells[1].symbol == self._cells[2].symbol)) or \
			(self._cells[4].symbol is not None and (self._cells[3].symbol == self._cells[4].symbol and self._cells[4].symbol == self._cells[5].symbol)) or \
			(self._cells[7].symbol is not None and (self._cells[6].symbol == self._cells[7].symbol and self._cells[7].symbol == self._cells[8].symbol)):
			self._is_finished = True

		if  (self._cells[3].symbol is not None and (self._cells[0].symbol == self._cells[3].symbol and self._cells[3].symbol == self._cells[6].symbol)) or \
			(self._cells[4].symbol is not None and (self._cells[1].symbol == self._cells[4].symbol and self._cells[4].symbol == self._cells[7].symbol)) or \
			(self._cells[5].symbol is not None and (self._cells[2].symbol == self._cells[5].symbol and self._cells[5].symbol == self._cells[8].symbol)):
			self._is_finished = True

		if  (self._cells[4].symbol is not None and (self._cells[0].symbol == self._cells[4].symbol and self._cells[4].symbol == self._cells[8].symbol)) or \
			(self._cells[4].symbol is not None and (self._cells[6].symbol == self._cells[4].symbol and self._cells[4].symbol == self._cells[2].symbol)):
			self._is_finished = True

		all_not_empty: bool = True
		for cell in self._cells:
			if cell.symbol is None:
				all_not_empty = False
				return
			
		if all_not_empty:
			self._is_it_a_draw = True
			self._is_finished = True

	def on_inputted(self, key: str) -> None:
		if self._is_finished:
			return

		if key == '1' or key == '2' or key == '3' or key == '4' or key == '5' or key == '6' or key == '7' or key == '8' or key == '9':
			self._at_least_one_move_was_done = True
			index: int = int(key)
			cell: Cell = self._cells[index - 1]
			if cell.symbol is None:
				cell.symbol = self._current_player
				if self._current_player == 'X':
					self._current_player = 'O'
				else:
					self._current_player = 'X'


class TicTacToe(Game):
	def create(self):
		self.add_entity(GameManager())

	def update(self):
		self.fill_screen(Color.white())


TicTacToe('tic tac toe', 600, 600)
