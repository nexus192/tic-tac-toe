from flask import Flask, request, redirect, url_for, render_template
from web.models.game import WebGame
from di.Container import Container
from web.web_mapper import WebMapper

app = Flask(__name__, template_folder='templates')

game = WebGame()
di_game = Container()
mapper = WebMapper()


@app.route('/game/<game_id>', methods=['GET', 'POST'], endpoint='game')
def game_la(game_id):
  if request.method == 'POST':
    row = int(request.form['row'])
    col = int(request.form['col'])
    mapper.from_web_to_domain(game).make_move(row, col)

  return render_template('board.html',
                         board=game.game_board.cells,
                         game_id=game.game_id)


@app.route('/')
def start_game():
  return render_template('init.html')


@app.route("/reset")
def reset():
  return redirect(url_for('game', game_id=game.game_id))


def get_local_ip():
  import socket
  return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
  print(f"Сервер доступен по адресу: http://{get_local_ip()}:5000")
