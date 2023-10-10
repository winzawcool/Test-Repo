import sys
import requests
from os import rename
import math


def greet(who_to_greet):
    test = "Test"
    greeting = f"Hello, {who_to_greet}"
    return greeting


# print(sys.version)
print(sys.executable)
# print(greet('World'))
# print(greet('Corey'))
r = requests.get("https://google.com")
print(r.status_code)
