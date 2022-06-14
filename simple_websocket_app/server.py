import threading
from flask import Flask, request, redirect, render_template, url_for
import simple_websocket
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
# CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, )


@app.route('/echo', websocket=True)
# @cross_origin()
def echo():
    ws = simple_websocket.Server(request.environ)
    # user = data.username
    try:
        while True:
            msg = ws.receive()
            if 'new_user' in msg:
                username = msg.replace('new_user ', '')
                print(username, 'has joined the chat')
                msg = 'new_user'
            # data = [msg, username]
            else:
                print(msg)

            ws.send({'msg': msg, 'user': username})
    except simple_websocket.ConnectionClosed:
        print('socket connection closed!')
        # pass
    except Exception as e:
        print('ERROR:', e)
        pass
    return ''


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t

if __name__ == '__main__':
    app.run(debug=True)
