from uuid import UUID, uuid4
from .board import Board


class WebGame:

  def __init__(self):
    self.game_id: UUID = uuid4()
    self.game_board = Board()
