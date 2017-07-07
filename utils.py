import time

def wait_until(condition, timeout=10, raise_exception=True, msg=""):

    temp_time = time.time()
    while((time.time() - temp_time) < timeout):
        if condition():
            return True

        time.sleep(0.1)

        if raise_exception:
            raise TimeoutError('Condition not fullfiled')
        else:
            return False


