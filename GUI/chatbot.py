from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = "Glad to know that you're doing " + user_message + "!"
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run()
