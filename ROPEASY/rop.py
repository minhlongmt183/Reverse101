#!/usr/bin/env python3

from pwn import *
from pprint import pprint

elf = ELF("./rop_easy")
# print(elf)

pprint(elf.symbols)