import brainfuck
def compress(code):
    # Compress the code.
    f = open('helloworld.cbf', 'wb')
    f.write(brainfuck.bf_compress(code))
    f.close()
def decompress():
    # Read the compressed code
    f = open('helloworld.cbf', 'rb')
    ret = brainfuck.bf_decompress(f.read())
    f.close()
    return ret
f = open('helloworld.bf', 'r')
fcon = f.read()
f.close()
compress(fcon)
x = decompress()
brainfuck.execute(x)
