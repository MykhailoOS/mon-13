# class Scale:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def __getattr__(self, item):
#         if item == "balance":
#             return "Немає доступу!"
#         raise AttributeError
#
#     def __setattr__(self, key, value):
#         if key == "balance":
#             if isinstance(value, str):
#                 raise TypeError("must be str")
#
#             if not value:
#                 raise ValueError("can't be null")
#         return "Can't change!"
#
#     def __str__(self):
#         return f'{self.balance}'
#
# x = Scale("123")
# print(x.balance)
#
# # x.my_attribute = "выф"
#
#

class UserException(Exception):

    def __str__(self):
        return "no exist user"

class UserChangeError(Exception):

    def __str__(self):
        return "you have no root premission to do that"
# task2

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def first_name(self):
        return f"user {self.first_name}"

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError()
        if not len(value):
            raise ValueError()
        raise UserChangeError()
    # def __getattr__(self, item):
    #     if item == "first_name":
    #         return f"user {self.first_name}"
    #     elif item == "last_name":
    #         return f"{self.last_name}"
    #     raise UserException
    #
    # def __setattr__(self, key, value):
    #     if key == "first_name":
    #         if not isinstance(value, str):
    #             raise TypeError
    #         if not value:
    #             raise ValueError
    #
    #     if key == "last_name":
    #         if not isinstance(value, str):
    #             raise TypeError
    #         if not value:
    #             raise ValueError
    #
    #     raise UserChangeError

user1 = User("Anton", "Antonov")
print(user1.last_name)
# user1.first_name = ""