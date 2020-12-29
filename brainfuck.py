from lib.parser import execute
from lib.compression import bf_compress, bf_decompress
# "Hello World!" program in BF
# ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

def test():
    x = get_instructions_in_string("+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>+.")
    print(x)
    y = bf_compress(x)
    print(y)
    z = bf_decompress(y)
    print(z)

if __name__=='__main__':
    while True:
        i = input('>>> ')
        if i[0] == '#':
            f = open(i[1:] + ".bf", 'r')
            execute(f.read())
        else:
            execute(i)
