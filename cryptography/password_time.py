import time
import itertools

def crack_password(target):
    # chars = "0123456789"
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    # chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(target)
    
    print(f"Attempting to crack: {target}")
    start_time = time.time() 

    for guess in itertools.product(chars, repeat=length):
        guess_str = "".join(guess)
        
        if guess_str == target:
            end_time = time.time()
            duration = end_time - start_time
            print(f"Password cracked! Total time: {duration:.4f} seconds")
            return

crack_password("1234567")