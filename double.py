def double(anotherFunct):
    def wrapperFunc():
      anotherFunct()
      print("Let's try that again!")
      anotherFunct()
    return wrapperFunc

