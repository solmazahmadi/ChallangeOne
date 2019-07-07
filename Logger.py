import time
import math


def logger(file_name):
    def log_decorater(fn):
          def inner1(*args, **kwargs):
              begin = time.time()
              res = fn(*args, **kwargs)
              text=open("text","W+")
              for num in range(10):
                    file.write(str(factorial())
                    file.write(",")
                    file.write("\n")
              file.close()
              end = time.time()
              return(res)
          return inner1
    return log_decorater

@ logger("text")
def factorial(num):
    print(math.factorial(num))

factorial(10)


