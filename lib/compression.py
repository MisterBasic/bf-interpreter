from lib.utils import *
# Super-simple compression algorithm that stores the instruction in
# the 3 most significant bits, and the amount in the other less significant
# bits.
# Instruction
# VVV      
# 101      01101
#          ^^^^^
#          Count
def bf_compress(instr):
    byte_array = []
    count = 0
    ci = ''
    for i in instr:
        if i == ci:
            count += 1
        else:
            inum = 0
            for d in BF_INSTRUCTION_SET:
                if i == d:
                    break
                inum += 1
            byte = inum << 5
            byte |= count + 1
            print(inum, count + 1, bin(byte))
            byte_array.append(byte)
            inum = 0
            count = 0
        ci = i
    return bytes(byte_array)
# Decompresses the bytes in the previous algorithm
def bf_decompress(byte_array):
    instr = []
    for byte in byte_array:
        inum = byte >> 5
        count = byte & ~(7 << 5)
        print(inum, count, bin(byte))
        for x in range(count):
            instr.append(BF_INSTRUCTION_SET[inum])
    return instr
