from uuid import UUID
from typing import Optional
from datasource.storage import GameStorage
from datasource.models.game import SourceGame


class GameRepository:

  def __init__(self, storage: GameStorage):
    self._storage = storage

  def save_game(self, game: SourceGame) -> None:
    self._storage.save_game(game)

  def get_game(self, game_id: UUID) -> Optional[SourceGame]:
    return self._storage.get_game(game_id)
