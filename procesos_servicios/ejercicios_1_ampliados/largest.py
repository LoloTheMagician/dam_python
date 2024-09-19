def largest_word():
    user_input: str = input("Lista: ")
    largest = ""
    for palabra in user_input.split():
        len_palabra = len(palabra)
        if len_palabra > len(largest):
            largest = palabra
    return largest


print(largest_word())
