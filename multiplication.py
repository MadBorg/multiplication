import numpy as np

def game():
    while True:
        correct = False
        a = np.random.randint(2,10)
        b = np.random.randint(2,10)
        ab = a*b
        while not correct:
            test = int(input(f" {a} * {b} = "))
            correct = ab == test
            if not correct:
                print("That is wrong")
        print("correct! ")
        


def main():
    game()
        
if __name__ == "__main__":
    main()