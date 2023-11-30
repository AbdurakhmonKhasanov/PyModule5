from celery import Celery
import time
app = Celery('hello', broker='redis://localhost:6379/0')

@app.task
def hello():
    print("hello started ")
    time.sleep(20)
    return 'hello finish '

@app.task
def function1():
    print("hello started ")
    time.sleep(20)
    return 'hello finish '

def function2():
    print("hello started ")
    time.sleep(20)
    return 'hello finish '
