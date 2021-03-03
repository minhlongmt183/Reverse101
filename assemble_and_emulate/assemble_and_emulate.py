from __future__ import print_function

# require for assembly
from keystone import *

# require for emulation
from unicorn import *
from unicorn.x86_const import *

# require for disassembly (for instruction trace during emulation)
from capstone import *


################################################################
CODE ="""
mov eax, 0
mov dword ptr [esp], 0x0AC8890A8
mov dword ptr [esp + 4], 0x0B9979C8A
mov dword ptr [esp + 8], 0X0FF989E93

loc_8048480:
    not byte ptr [esp + eax]
    inc eax
    cmp eax, 0xC
    jnz loc_8048480
"""

### setup capstone disassembler
md = Cs(CS_ARCH_X86, CS_MODE_32)

### compile code
ks = Ks(KS_ARCH_X86, KS_MODE_32)

print("compiling...")
