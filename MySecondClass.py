class MySecondClass:

    class_argument = 200

    def __init__(self, a, b):
        self.arg1 = a
        self.arg2 = b
    __doc__ = "this is the class' description"

    @classmethod
    def print_first_argument_cls_met(cls):
        print(cls.class_argument)
        print("this is class")

    @staticmethod
    def print_first_argument_stt_met(a, b, c):
        print("this is static")
        return a + b + c


if __name__ == "__main__":
    my_instance = MySecondClass(1, 2)
    print(my_instance.class_argument)
    print(MySecondClass.class_argument)
    MySecondClass.class_argument = 300
    MySecondClass.print_first_argument_cls_met()
    print(MySecondClass.print_first_argument_stt_met(1, 2, 3))
    print(MySecondClass.__doc__)

