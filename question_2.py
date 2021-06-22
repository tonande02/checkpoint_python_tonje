# A program that turns text into camelcase

def to_camel_case(text):
    words = text.split(" ")
    camel_string = ""

    for word in words:
        camel_string += word.capitalize()
    
    return camel_string


print(to_camel_case("hello world"))
print(to_camel_case("My stRinG"))
print(to_camel_case("This iS aS tEsT stRing"))