import json

def read_file():
    a = open("data.txt", "r")
    a.read()
    
def write_file(name: str, age: int):
    b = open("data.txt", "a")
    b.write(f"{name} - {age} yoshda\n")

name = input("name:")
age = input("age:")


write_file(name,age)