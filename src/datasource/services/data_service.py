from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from datasource.repositories.repository import GameRepository
from datasource.models.game import SourceGame


class IGameService(ABC):

  @abstractmethod
  def save_current_game(self, game: SourceGame) -> None:
    pass

  @abstractmethod
  def get_current_game(self, game_id: UUID) -> Optional[SourceGame]:
    pass

  def get_all_games(self) -> dict[any]:
    pass


class GameDataService(IGameService):

  def __init__(self, repository: GameRepository):
    self._repo = repository

  def save_current_game(self, game: SourceGame) -> None:
    self._repo.save_game(game)

  def get_current_game(self, game_id: UUID) -> Optional[SourceGame]:
    return self._repo.get_game(game_id)

  def get_all_games(self) -> dict[any]:
    return self._repo.get_all_games()
