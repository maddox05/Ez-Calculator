class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multi(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

    def sub(self):
        return self.x - self.y


if __name__ == "__main__":
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
    except:
        print("error, thats prob not a number lol")
    obj = calculator(x, y)
    answer = int(input("Choose 1 to Add, 2 to multiply, 3 to divide, 4 to subtract: "))
    if answer == 1:
        print(obj.add())
    elif answer == 2:
        print(obj.multi())
    elif answer == 3:
        print(obj.div())
    elif answer == 4:
        print(obj.sub())
    else:
        print("error")

