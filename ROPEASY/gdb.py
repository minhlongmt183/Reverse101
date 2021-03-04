class TraceAsm(gdb.Command):
    def __init__(self):
        super().__init__(
            'trace-asm',
            gdb.COMMAND_BREAKPOINTS,
            gdb.COMPLETE_NONE,
            False
        )
    def invoke(self, argument, from_tty):
        argv = gdb.string_to_argv(argument)
        if argv:
            gdb.write('Does not take any arguments.\n')
        else:
            done = False
            thread = gdb.inferiors()[0].threads()[0]
            last_path = None
            last_line = None
            with open('trace.tmp', 'w') as f:
                while thread.is_valid():
                    frame = gdb.selected_frame()
                    sal = frame.find_sal()
                    symtab = sal.symtab
                    if symtab:
                        path = symtab.fullname()
                        line = sal.line
                    else:
                        path = None
                        line = None
                    if path != last_path:
                        f.write("path {}{}".format(path, os.linesep))
                        last_path = path
                    if line != last_line:
                        f.write("line {}{}".format(line, os.linesep))
                        last_line = line
                    pc = frame.pc()
                    f.write("{} {} {}".format(hex(pc), frame.architecture().disassemble(pc)[0]['asm'], os.linesep))
                    gdb.execute('si', to_string=True)
TraceAsm()