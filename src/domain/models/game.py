from uuid import UUID, uuid4
from .board import Board


class Game:

  def __init__(self, game_id: UUID):
    self.game_id: UUID = game_id
    self.board = Board()
    self.move_history: list[tuple[int, list[int, int]]] = []
    self.current_player: int = Board.PLAYER_X

  def make_move(self, row: int, col: int, player: int):
    self.board.set_cell(row, col, player)
    self.move_history.append((player, [row, col]))
    return self.board.cells
