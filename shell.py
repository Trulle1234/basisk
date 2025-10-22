import basisk

while True:
    text = input("basisk> ")
    result, error = basisk.ru1n(text)

    if error: print(error.as_string)
    else: print(result)