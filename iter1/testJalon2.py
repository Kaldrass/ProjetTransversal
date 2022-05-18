from move import forward, backward, left, right, read
import time

# read()
var = forward()
print(var)

while True:
    if var == b'Ok0000\n\r':
        #         time.sleep(2)
        var = forward()
# left()
# right()
