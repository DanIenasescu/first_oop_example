class AClass:
    class_attribute1 = 0
    class_attribute2 = 1

    def __init__(self, atr1, atr2):
        self.inst_atr1 = atr1
        self.inst_atr2 = atr2

    @staticmethod
    def addition(param1, param2):
        return param1 + param2

    def inst_addition(self):
        return self.inst_atr1 + self.inst_atr2


if __name__ == "__main__":
    # print(AClass.class_attribute1)
    # print("The second attribute of the class is: {}".format(AClass.class_attribute2))
    # AClass.class_attribute2 = 4
    # print("The second attribute of the class is: {}".format(AClass.class_attribute2))
    instance_of_class = AClass(11, 12)
    # print("The sum of the instance's attributes is: {}".format(instance_of_class.inst_addition()))
    print(instance_of_class.inst_atr1)
    print(AClass.addition(13, 14))

