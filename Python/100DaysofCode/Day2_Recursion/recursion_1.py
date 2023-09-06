

def process(txt, i):
    if (i == len(txt)):
        return

    print(txt[i])

    return process(txt, i + 1)


print(process("Gokul", 0))