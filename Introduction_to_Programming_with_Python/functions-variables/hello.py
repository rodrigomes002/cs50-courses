# Ask user for their name
name = input("what's your name? ")

# Remove whitespace from str and capitalise user's name
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")


# Say hello to user
# print(f"hello, {first} {last}")

def hello(to):
    print("hello", to)


hello(name)
