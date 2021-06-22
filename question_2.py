# A program that turns text into camelcase

# 1b (level 1)
def to_camel_case(text):
    words = text.split(" ")
    camel_string = ""

    for word in words:
        camel_string += word.capitalize()
    
    return camel_string


# print(to_camel_case("hello world"))
# print(to_camel_case("My stRinG"))
print("Regular to camel:", to_camel_case("This iS a tEsT stRing"))



# 2b (level 2)

camel_string = to_camel_case("This iS a tEsT stRing")

def camel_to_snake(camel):
    snake = ""
    space = False

    for letter in camel:
        if letter.isupper():
            snake += "_"
            snake += letter.lower()
        elif letter == " ":
            print("Wrong format, dude! try again!")
            space = True
            break
        else:
            snake += letter
    
    if not space:
        return snake[1::]
    else:
        return "That's a no go, dude. No snakes here..."


print("Camel to snake:", camel_to_snake(camel_string))
# print(camel_to_snake('hey there')) # for testing wrong input