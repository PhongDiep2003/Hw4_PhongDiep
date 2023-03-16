def double(anotherFunct):
    anotherFunct()
    def wrapperFunc():
      anotherFunct()
    print("Let's try that again!")
    return wrapperFunc

