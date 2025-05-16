import threading
from uuid import UUID

from datasource.models.game import SourceGame


class GameStorage:
  _instance = None
  _singleton_lock = threading.Lock()

  def __new__(cls):
    if cls._instance is None:
      with cls._singleton_lock:
        if cls._instance is None:
          cls._instance = super(GameStorage, cls).__new__(cls)
    return cls._instance

  def __init__(self):
    if hasattr(self, "_initialized") and self._initialized:
      return
    self._lock = threading.Lock()
    self.data: dict[UUID, SourceGame] = {}
    self._initialized = True

  def save_game(self, current_game: SourceGame):
    with self._lock:
      self.data[current_game.game_id] = current_game

  def get_game(self, game_id: UUID) -> SourceGame:
    with self._lock:
      return self.data[game_id]

  def get_all_games(self) -> dict:
    with self._lock:
      return self.data
