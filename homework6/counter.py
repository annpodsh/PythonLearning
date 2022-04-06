"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    class DecoratedClass(cls):
        i = 0

        def __init__(self):
            super().__init__()
            DecoratedClass.i += 1

        @classmethod
        def get_created_instances(cls) -> int:
            return DecoratedClass.i

        @classmethod
        def reset_instances_counter(cls) -> int:
            temp = DecoratedClass.i
            DecoratedClass.i = 0
            return temp

    return DecoratedClass


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
