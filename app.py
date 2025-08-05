from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    step = data.get("step")
    choice = data.get("choice", "").lower()

    if step == 1:
        if choice == "":
            return jsonify(
                result="Your mission is to find the treasure.",
                question="Which side do you wanna go?",
                choices=["left", "right"],
                gameOver=False
            )
        if choice == "right":
            return jsonify(result="YOU FELL INTO A HOLE. GAME OVER", gameOver=True)
        elif choice == "left":
            return jsonify(
                result="YOU ARE SAFE. MAKE YOUR NEXT CHOICE!",
                question="You see a river. What would you do?",
                choices=["swim", "wait"],
                gameOver=False
            )
        else:
            return jsonify(result="Invalid choice. Try 'left' or 'right'.", gameOver=False)

    elif step == 2:
        if choice == "swim":
            return jsonify(result="ATTACKED BY TROUT! GAME OVER", gameOver=True)
        elif choice == "wait":
            return jsonify(
                result="A BOAT HAS COME. YOU ARE SAFE. MAKE YOUR NEXT CHOICE!",
                question="You see three doors. Which one will you enter?",
                choices=["red", "blue", "yellow"],
                gameOver=False
            )
        else:
            return jsonify(result="Invalid choice. Try 'swim' or 'wait'.", gameOver=False)

    elif step == 3:
        if choice == "red":
            return jsonify(result="BURNED BY FIRE. GAME OVER", gameOver=True)
        elif choice == "blue":
            return jsonify(result="EATEN BY BEASTS. GAME OVER", gameOver=True)
        elif choice == "yellow":
            return jsonify(
                result="YOU FOUND THE TREASURE!!!!! YOU WIN!!!!",
                question="Say 'yes' to open the treasure box.",
                choices=["yes"],
                gameOver=False,
                win=True
            )
        else:
            return jsonify(result="Invalid choice. Try 'red', 'blue', or 'yellow'.", gameOver=False)

    elif step == 4:
        if choice == "yes":
            treasure_art = r"""_.--.
                    _.-'_:-'||       
                _.-'_.-::::'||     
           _.-:'_.-::::::'  ||   
         .'`-.-:::::::'     ||    
        /.'`;|:::::::'      ||_  
       ||   ||::::::'     _.;._'-._  
       ||   ||:::::'  _.-!oo @.!-._'-. 
       \'.  ||:::::.-!()oo @!()@.-'_.| 
        '.'-;|:.-'.&$@.& ()$%-'o.'\U|| 
          `>'-.!@%()@'@_%-'_.-o _.|'|| 
           ||-._'-.@.-'_.-' _.-o  |'|| 
           ||=[ '-._.-\U/.-'    o |'|| 
           || '-.]=|| |'|      o  |'|| 
           ||      || |'|        _| '; 
           ||      || |'|    _.-'_.-' 
           |'-._   || |'|_.-'_.-'       
        jgs '-._'-.|| |' `_.-'          
                '-.||_/.-'"""
            return jsonify(result=treasure_art, gameOver=True)
        else:
            return jsonify(result="You didn't open the treasure. GAME OVER", gameOver=True)

    return jsonify(result="Unknown step.", gameOver=True)

if __name__ == '__main__':
    app.run(debug=True)

