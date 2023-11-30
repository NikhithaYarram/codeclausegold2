import time

def speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    print("You will be given a sentence to type. Type it as fast as you can once you are ready!")
    
    sentence = "The quick brown fox jumps over the lazy dog."
    
    input("Press Enter to start the test...")
    
    start_time = time.time()
    user_input = input(f"Type the following sentence: '{sentence}'\n")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = len(user_input.split())
    speed = words / elapsed_time * 60

    print(f"Your typing speed is {speed:.2f} words per minute.")

if __name__ == "__main__":
    speed_typing_test()
