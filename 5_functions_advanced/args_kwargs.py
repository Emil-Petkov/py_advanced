# ll = [4, 3, 2, 1]
# a, b, c, d = ll
#
# a = ll[0]
# b = ll[1]
# c = ll[2]
# d = ll[3]
#
# print(a, b, c, d)  # 4 3 2 1
#
# k, f, *e = ll
#
# print(k, f)  # 4 3
# print(k, f, e)  # 4 3 [2, 1]
# print(k, e, f)  # 4 [2, 1] 3


########################################################################

# def test(args):
#     print(args)
#
#
# test(1, 2, 3)  # TypeError: test() takes 1 positional argument but 3 were given
# test("Emil", "Nadezhda", "Ivan")  # TypeError: test() takes 1 positional argument but 3 were given
# test(3.14, 8, 9)  # TypeError: test() takes 1 positional argument but 3 were given
#
# test({a: 1, b: 2, c: 3})  # {4: 1, 3: 2, 2: 3} -> one argument
# test([1, 2, 3])  # [1, 2, 3]-> one argument
# test((1, 2, 3))  # (1, 2, 3)-> one argument

###################################################################################

def test_args(*args):
    print(args)


test_args(1, 2, 3)  # (1, 2, 3)
test_args("Emil", "Nadezhda", "Ivan")  # ('Emil', 'Nadezhda', 'Ivan')
test_args(3.14, 8, 9)  # (3.14, 8, 9)


###################################################################################

# def test_kwargs(**kwargs):
#     print(kwargs)
#
#
# test_kwargs(name="Emil", age=100)  # {'name': 'Emil', 'age': 100}
# test_kwargs(x="17", y=23)  # {'x': '17', 'y': 23}
# test_kwargs(numbers=[1, 2, 3, 4, 5], text="Hello")  # {'numbers': [1, 2, 3, 4, 5], 'text': 'Hello'}

########################################


def test_kwargs(**kwargs):
    if "age" not in kwargs:  # optional parameters
        kwargs["age"] = None

    print(kwargs)


test_kwargs(name="Emil", age=100)  # {'name': 'Emil', 'age': 100}
test_kwargs(x="17", y=23)  # {'x': '17', 'y': 23, 'age': None} <----
test_kwargs(numbers=[1, 2, 3, 4, 5], text="Hello")  # {'numbers': [1, 2, 3, 4, 5], 'text': 'Hello', 'age': None} <----


################################################################
def test_args_kwargs(*args, **kwargs):
    print("___________")
    print(args)
    print(kwargs)
    print("___________")


test_args_kwargs(1, 2, 3, 4, 5)
# ___________
# (1, 2, 3, 4, 5) <--- args
# {} <--- kwargs
# ___________

test_args_kwargs(x=1, y=2, z=3)
# ___________
# () <--- args
# {'x': 1, 'y': 2, 'z': 3} <--- kwargs
# ___________

test_args_kwargs(1, 2, 3, hello="World")
# ___________
# (1, 2, 3) <--- args
# {'hello': 'World'} <--- kwargs
# ___________

test_args_kwargs(aaa={"a": {"x": 1, "y": 2, "z": 3}})
# ___________
# () <--- args
# {'aaa': {'a': {'x': 1, 'y': 2, 'z': 3}}} <--- kwargs
# ___________

test_args_kwargs()
# This is a valid case
# ___________
# () <--- args
# {} <--- kwargs
# ___________
