from capstone import *

class Program:
    def __init__(self):
        raw_bytes =open('crackme.i', 'rb').read()[8:]
        self.code = [int.from_bytes(raw_bytes[i:i+4], byteorder='little') for i in range(0, len(raw_bytes), 4)]
        
        md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS64 + CS_MODE_LITTLE_ENDIAN)

        for mips in self.code:
            for i in md.disasm(mips, 0x1000):
                print("%x: \t%s\t%s" %(i.address, i.mnemonic, i.op_str))


program =Program()
