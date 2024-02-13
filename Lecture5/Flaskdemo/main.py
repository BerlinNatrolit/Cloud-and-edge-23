from flask import Flask, redirect, render_template, request

app = Flask(__name__)

games = [
    {"name": "Half-Life 2", "metascore": 96},
    {"name": "GTA V", "metascore": 96},
    {"name": "Baldurs gate 3", "metascore": 96},
    {"name": "Mass Effect 2", "metascore": 94},
    {"name": "Dwarf Fortress", "metascore": 93},
    {"name": "The Sims", "metascore": 92},
    {"name": "Ride to hell: Retribution", "metascore": 16}
]

@app.route('/')
def home():
    return render_template("index.html", games=games)

@app.route('/remove/<int:game>', methods=["GET"])
def remove(game):
    games.pop(game)
    return redirect('/')

@app.route('/add', methods=["POST"])
def add():
    game_title = request.form["title"]
    score = request.form["metascore"]
    new_game = {"name": game_title, "metascore": score}
    games.append(new_game)
    return redirect('/')

@app.route('/info')
def info():
    game_index = int(request.args["game"])
    return render_template("game.html", 
                           title = games[game_index]["name"], 
                           metascore = games[game_index]["metascore"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)