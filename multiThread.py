import threading


def initiate(function):
    x = threading.Thread(target=function)
    x.setDaemon(True)
    x.start()
