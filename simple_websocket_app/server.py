from flask import Flask, request, redirect, render_template, url_for
import simple_websocket

app = Flask(__name__)


@app.route('/echo', websocket=True)
def echo():
    ws = simple_websocket.Server(request.environ)
    if ws.connected:
        msg = ws.receive()
        print(msg)
        print('IT worked. Connection successful!')
        ws.close()
    return redirect(url_for('home'))

    # ws.send('Hello there!!!')
    try:
        while True:
            msg = ws.receive()
            print(msg)
    except simple_websocket.ConnectionClosed:
        pass
    return ''


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run', methods=["GET", "POST"])
def handleData():
    # if request.method == 'POST':
    #     msg = request.args['msg']
    #     print(f'Message received: {msg}')
    #     return 'data received successfully!'
    # return 'method was not post'
    pass


if __name__ == '__main__':
    app.run(debug=True)
