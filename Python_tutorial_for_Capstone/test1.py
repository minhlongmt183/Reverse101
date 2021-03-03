from capstone import *

# CODE = b"\x55\x48\x05\xb8\x13\x00\x00"
CODE = b"\x56\x34\x21\x34\xc2\x17\x01\x00" # for mips

# CS(hardware architecture and the hardware mode)
# md = Cs(CS_ARCH_X86, CS_MODE_64)
md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS64 + CS_MODE_LITTLE_ENDIAN)


# v1
for i in md.disasm(CODE, 0x4000):
    print("0x%x:\t %s \t %s" %(i.address, i.mnemonic, i.op_str))

# # v2
# for (address, size, mnemonic, op_str) in md.disasm_lite(CODE, 0x1000):
#     print("0x%x:\t %s \t %s" %(address, mnemonic, op_str))