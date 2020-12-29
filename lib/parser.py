from lib.utils import *

def execute(cmd: str, ret_outputs=False, input_query=[], wrapping=True):
    ret = ""
    iqi = 0
    data = {}
    p = 0
    indexes = {}
    i = 0
    commands = get_instructions_in_string(cmd)
    while not (i >= len(cmd)-1):
        if p not in data.keys():
            data[p] = 0
        c = commands[i]
        if c == ">":
            p += 1
        elif c == "<":
            p -= 1
        elif c == "+":
            data[p] += 1
        elif c == "-":
            data[p] -= 1
        elif c == '.':
            if ret_outputs:
                ret += chr(data[p])
            else:
                print(chr(data[p]), end='')
        elif c == ',':
            if len(input_query) > 0 and iqi < len(input_query):
                if type(input_query[iqi]) != int:
                    bf_error("Improper input values. Only integers allowed.")
                data[p] = input_query[iqi]
                iqi += 1
            else:
                x = input('$')
                data[p] = x[0]
        elif c == '[':
            x = get_closed_scope(commands, i)
            indexes[x] = i
            if data[p] == 0:
                i = x
        elif c == ']':
            if data[p] != 0:
                i = indexes[i]
        i += 1
    return data
