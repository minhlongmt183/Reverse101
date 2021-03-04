import gdb

gdb.execute('b* 0x555555557050')
gdb.execute('run')

while (True):
    gdb.write (gdb.execute('x /i $pc', to_string=True).rstrip('\n'), gdb.STDOUT)
    gdb.execute('stepi', to_string=False)
    gdb.flush ()