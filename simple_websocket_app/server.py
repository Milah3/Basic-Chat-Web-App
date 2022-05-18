from flask import Flask, render_template, request
import simple_websocket

app = Flask(__name__)


@app.route('/server', websocket=True)
def home():
    ws = simple_websocket.Server(request.environ)

    try:
        while True:
            msg = ws.receive()
            ws.send(msg)
    except simple_websocket.ConnectionClosed:
        pass
    return ''


if __name__ == '__main__':
    app.run()

    # return render_template('index.html')
