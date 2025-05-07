from uuid import UUID, uuid4
from .board import Board


class Game:

  def __init__(self):
    self.game_id: UUID = uuid4()
    self.board = Board()
    self.move_history: list[tuple[int, int]] = []
    self.current_player: int = Board.PLAYER_X
