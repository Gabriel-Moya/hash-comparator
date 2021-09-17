import functions
import time

functions.set_original_hash()

while True:
    functions.check_hashs()
    time.sleep(10)
