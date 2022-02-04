def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Yonatan", "lastname": "Mamani"}

    super_list = [
        {"firstname": "Yonatan", "lastname": "Mamani"},
        {"firstname": "Maria", "lastname": "Ruiz"},
        {"firstname": "Juan", "lastname": "Lopez"},
        {"firstname": "Oscar", "lastname": "Coco"},
        {"firstname": "Dana", "lastname": "Mamani"},

    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1. -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    print("...")
    for value in super_list:
        print(value['firstname'], "-", value['lastname'])


if __name__ == '__main__':
    run()