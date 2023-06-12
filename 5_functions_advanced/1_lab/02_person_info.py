def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"

# person1 = {
#     "name": "Emil",
#     "town": "Sofia",
#     "age": 31
# }
# person2 = {
#     "name": "Nadezhda",
#     "town": "Sofia",
#     "age": 63
# }
# person3 = {
#     "name": "Ivancho",
#     "town": "Rakita village",
#     "age": 78
# }
#
# print(get_info(**person1))  # This is Emil from Sofia and he is 31 years old
# print(get_info(**person2))  # This is Nadezhda from Sofia and he is 63 years old
# print(get_info(**person3))  # This is Ivancho from Rakita village and he is 78 years old

#########################################################################################################

# def get_info(**kwargs):
#     name = kwargs["name"]
#     town = kwargs["town"]
#     age = kwargs["age"]
#     return f"This is {name} from {town} and he is {age} years old"
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

#########################################################################################################

# def get_info(**kwargs):
#     name = kwargs.get('name')
#     town = kwargs.get('town')
#     age = kwargs.get('age')

#     return f"This is {name} from {town} and he is {age} years old"


# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
