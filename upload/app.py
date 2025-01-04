from flask import Flask, send_file, request, jsonify
import random

app = Flask(__name__)

# Game logic
def get_result(user_choice):
    youdict = {"Snake": 1, "Water": -1, "Gun": 0}
    reversedict = {1: "Snake", -1: "Water", 0: "Gun"}

    # User and computer choices
    you = youdict[user_choice]
    computer = random.choice([-1, 1, 0])
    computer_choice = reversedict[computer]

    # Determine result
    if computer == you:
        result = "It's a tie!"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        result = "You win!!"
    else:
        result = "You lose!!"

    return {"user_choice": user_choice, "computer_choice": computer_choice, "result": result}

@app.route('/')
def index():
    return send_file('D:/PYTHON/HARRY/PROJECTS/SNAKE_WATER_GUNGAME/upload/index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    result = get_result(user_choice)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
