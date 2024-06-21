import functools
import inspect
import logging
 
logging.basicConfig(level = logging.INFO)

def dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        sig = inspect.signature(func)
        sigB = sig.bind(*args, **kwargs)
        paramInfo = {name: type(value).__name__ for name, value in sigB.arguments.items()}
        logging.info(f" {paramInfo}")

        return func(*args, **kwargs)
    return wrapper
 
@dec
def someFunction(n, m, o):
    return True
 
 
someFunction(5, 6, "asdf")