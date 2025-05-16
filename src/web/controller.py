from flask import Flask, request, redirect, url_for, render_template
from web.models.game import WebGame
from di.Container import Container
from web.web_mapper import WebMapper
from datasource.data_mapper import SourceMapper
from uuid import UUID

app = Flask(__name__, template_folder='templates')

# game = WebGame()
di_game = Container()
web_mapper = WebMapper()
source_mapper = SourceMapper()
games_by_id: dict[str, WebGame] = {}


@app.route('/game/<game_id>', methods=['GET', 'POST'], endpoint='game')
def game_la(game_id):
  game_id = UUID(game_id)

  game = web_mapper.from_domain_to_web(
      source_mapper.from_storage_to_domain(
          di_game.game_data_service.get_current_game(game_id)))

  if request.method == 'POST':
    row = int(request.form['row'])
    col = int(request.form['col'])
    if game.game_board.cells[row][col] == 0:
      web_mapper.from_web_to_domain(game).make_move(row, col,
                                                    game.game_board.PLAYER_X)
      ai_move = di_game.domain.get_next_move(
          web_mapper.from_web_to_domain(game))
      if ai_move is not None:
        row_ai, col_ai = ai_move
        web_mapper.from_web_to_domain(game).make_move(row_ai, col_ai,
                                                      game.game_board.PLAYER_O)

  return render_template('board.html',
                         board=game.game_board.cells,
                         game_id=game.game_id)


@app.route('/')
def start_game():
  return render_template('navigation_bar.html')


@app.route("/new_game")
def new_game():
  game = WebGame()
  di_game.game_data_service.save_current_game(
      source_mapper.from_domain_to_storage(web_mapper.from_web_to_domain(game)))
  return redirect(url_for('game', game_id=game.game_id))


@app.route("/all_game")
def all_game():
  games = di_game.game_data_service.get_all_games()
  return render_template('all_games.html', games=games.keys())


def get_local_ip():
  import socket
  return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
  print(f"Сервер доступен по адресу: http://{get_local_ip()}:5000")
