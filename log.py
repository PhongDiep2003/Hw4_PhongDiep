import time
def timestamp(anotherFunct):
    def wrapperFunc():
        print(time.ctime())
        anotherFunct()
    return wrapperFunc

