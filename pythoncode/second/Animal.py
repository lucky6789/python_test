import yaml


class Animal:

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 定义叫方法
    def shouting(self):
        print("会叫")

    # 定义跑方法
    def running(self):
        print("会跑")


class Cat(Animal):
    def __init__(self, name, color, age, sex, hair="short_hair"):
        super().__init__(name, color, age, sex)
        self.hair = hair

    # 定义会捉老鼠方法
    def catching_mice(self):
        print("会捉老鼠")

    # 复写父类Animal的叫方法
    def shouting(self):
        print("喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, sex, hair="long_hair"):
        super().__init__(name, color, age, sex)
        self.hair = hair

    # 定义会看家方法
    def looking_after_home(self):
        print("会看家")

    # 复写符类Animal的叫方法
    def running(self):
        print("汪汪叫")


if __name__ == "__main__":
    with open("config.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        print(data)


    cat_data = data["cat"]
    cat = Cat(cat_data["name"], cat_data["color"], cat_data["age"], cat_data["sex"], cat_data["hair"])
    print("猫猫的姓名，颜色，年龄，性别，毛发:", cat.name, cat.color, cat.age, cat.sex, cat.hair)
    cat.catching_mice()

    dog_data = data["dog"]
    dog = Dog(dog_data["name"], dog_data["color"], dog_data["age"], dog_data["sex"], dog_data["hair"])
    print("狗狗的姓名，颜色，年龄，性别，毛发", dog.name, dog.color, dog.age, dog.sex, dog.hair)
    dog.looking_after_home()