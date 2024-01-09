class MyClass:
    # a simple class
    def __init__(self, argument1: int, argument2: int):
        self.arg1 = argument1
        self.arg2 = argument2

    def method1(self):
        print("printing the first argument of the instance: {}".format(self.arg1))

    def method2(self, a):
        print("printing the first argument of the instance: {}".format(self.arg1))
        print("printing the argument passed to the method: {}".format(a))


if __name__ == "__main__":
    instance = MyClass(1, 2)
    instance.method1()
    instance.method2(2)
