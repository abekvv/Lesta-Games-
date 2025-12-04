# task1.py

def isEven(value):
    return (value & 1) == 0

if __name__ == "__main__":
    print("Число 4 четное:", isEven(4))
    print("Число 5 четное:", isEven(5))
