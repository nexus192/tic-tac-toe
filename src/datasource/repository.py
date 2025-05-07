from uuid import UUID
from typing import Optional
from .storage import GameStorage
from .models.game import CurrentGame


class GameRepository:

  def __init__(self, storage: GameStorage):
    self._storage = storage

  def save_game(self, game: CurrentGame) -> None:
    self._storage.save_game(game)

  def get_game(self, game_id: UUID) -> Optional[CurrentGame]:
    return self._storage.get_game(game_id)
