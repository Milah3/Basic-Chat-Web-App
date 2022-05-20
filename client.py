import simple_websocket


def main():
    ws = simple_websocket.Client('ws://localhost:5000/echo')
    try:
        # while True:
        # print('do something here!')
        #send msg to server

        ws.send('Hey, its working!!!')
    except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
        ws.close()
    return 'client main working!'


# @app.route('/run', methods=["GET", "POST"])
# def run():
#     # receive msg and send it to server!
#     try:
#         while True:
#             if request.method == 'POST':
#                 msg = request.form['msg']
#                 ws.send(msg)
#                 print(f'message sent to server: {msg}')
#                 # MORE TO DO HERE!!
#                 return 'message sent to server'
#     except (KeyboardInterrupt, EOFError, simple_websocket.ConnectionClosed):
#         ws.close()

if __name__ == '__main__':
    main()
