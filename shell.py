import basisk

while True:
    text = input("basisk> ")
    if text.strip() == "":
        continue

    result, error = basisk.run("<standardin>", text)

    if error:
        print(error.as_string())