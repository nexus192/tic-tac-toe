from abc import ABC, abstractmethod
from typing import Optional, Tuple
from domain.models.game import Game


class IGameService(ABC):

  @abstractmethod
  def get_next_move(self, game: 'Game') -> Tuple[int, int]:
    pass

  @abstractmethod
  def validate_board(self, game: 'Game', new_board: list[list[int]]) -> bool:
    pass

  @abstractmethod
  def is_game_over(self, game: 'Game') -> Tuple[bool, Optional[int]]:
    pass
