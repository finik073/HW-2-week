def hello_user():
    while True:
        try:
            ask_user = input('Как дела?  ')
        except KeyboardInterrupt:
            print('Пока!')
            break
    
if __name__ == "__main__":
    hello_user()
