#Decorators and *args
def capitalize_list(func):
    def wrapper(*args, **kwargs):
        capitalized_names = func(names)
        return capitalized_names
    return wrapper

#Lambda and Map Function
@capitalize_list
def capitalize_names(names):
    return list(map(lambda x: x.capitalize(), names))

#List Function
names = ["aiza", "tin", "angie"]
capital = capitalize_names(names)

#Applying the decorator
def greet(names):
	print(f"Hello, {names}!")

greet(capital)