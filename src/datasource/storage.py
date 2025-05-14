import threading
from uuid import UUID

from datasource.models.game import SourceGame


class GameStorage:

  def __init__(self):
    self.data: dict[UUID, SourceGame] = {}
    self._lock = threading.Lock()

  def save_game(self, current_game: SourceGame):
    with self._lock:
      self.data[current_game.game_id] = current_game

  def get_game(self, game_id: UUID) -> SourceGame:
    with self._lock:
      return self.data[game_id]
