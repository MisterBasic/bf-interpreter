BF_INSTRUCTION_SET = [
    '>', '<', '+', '-', '.', ',', '[', ']'
]
def bf_error(msg):
    print("ERROR:", msg)
def get_closed_scope(cmd, idx):
    d = False
    x = 0
    inner = 0
    while not d:
        if idx + x >= len(cmd) - 1:
            bf_error("scope not closed.")
            return 0
        y = cmd[idx+x]
        if y not in BF_INSTRUCTION_SET:
            continue
        elif y == '[':
            inner += 1
        elif y == ']':
            inner -= 1
        if inner == 0:
            d = True
        elif y in BF_INSTRUCTION_SET:
            x+=1
        else:
            continue
    return idx + x
def get_instructions_in_string(string):
    i = []
    for c in string:
        if c in BF_INSTRUCTION_SET:
            i.append(c)
    return i
def wrap(i):
    return i %= 255
