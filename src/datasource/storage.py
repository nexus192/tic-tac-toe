import threading
from uuid import UUID

from datasource.models.game import CurrentGame


class GameStorage:

  def __init__(self):
    self.data: dict[UUID, CurrentGame] = {}
    self._lock = threading.Lock()

  def save_game(self, current_game: CurrentGame):
    with self._lock:
      self.data[current_game.game_id] = current_game

  def get_game(self, game_id: UUID) -> CurrentGame:
    with self._lock:
      return self.data[game_id]
