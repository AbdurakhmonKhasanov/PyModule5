from task import hello, function1, function2

a = [hello, function1, function2]
for i in a:
    i.delay()
print(10)