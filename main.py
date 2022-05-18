from flask import Flask, render_template
import simple_websocket

app = Flask(__name__)


@app.route('/', websocket=True)
def home():
    return render_template('./index.html')


if __name__ == '__main__':
    app.run(debug=True)
