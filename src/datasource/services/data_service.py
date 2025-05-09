from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from datasource.repositories.repository import GameRepository
from datasource.models.game import CurrentGame


class IGameService(ABC):

  @abstractmethod
  def save_current_game(self, game: CurrentGame) -> None:
    pass

  @abstractmethod
  def get_current_game(self, game_id: UUID) -> Optional[CurrentGame]:
    pass


class GameService(IGameService):

  def __init__(self, repository: GameRepository):
    self._repo = repository

  def save_current_game(self, game: CurrentGame) -> None:
    self._repo.save_game(game)

  def get_current_game(self, game_id: UUID) -> Optional[CurrentGame]:
    return self._repo.get_game(game_id)
