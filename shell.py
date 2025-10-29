import basisk

while True:
    text = input("basisk> ")
    result, error = basisk.run("<standardin>", text)

    if error: print(error.as_string())
    elif result: print(result)