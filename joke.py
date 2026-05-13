from pyjokes import get_joke

def tell_joke():
    joke = get_joke()
    print(joke)


print("Here's a joke for you:")
tell_joke()