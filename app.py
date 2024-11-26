from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/.well-known/discord')
def discord_verification():
    return send_from_directory('.well-known', 'discord')

if __name__ == '__main__':
    app.run(debug=True)
