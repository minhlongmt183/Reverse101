import gdb
import string


# change below settings to match your needs
## BEGIN OF SETTINGS ##

# external binaries, required for some commands
READELF      = "/usr/bin/readelf"
OBJDUMP      = "/usr/bin/objdump"
NASM         = "/usr/bin/nasm"
NDISASM      = "/usr/bin/ndisasm"

# PEDA global options
OPTIONS = {
    "badchars"  : ("", "bad characters to be filtered in payload/output, e.g: '\\x0a\\x00'"),
    "pattern"   : (1, "pattern type, 0 = basic, 1 = extended, 2 = maximum"),
    "p_charset" : ("", "custom charset for pattern_create"),
    "indent"    : (4, "number of ident spaces for output python payload, e.g: 0|4|8"),
    "ansicolor" : ("on", "enable/disable colorized output, e.g: on|off"),    
    "pagesize"  : (25, "number of lines to display per page, 0 = disable paging"),
    "session"   : ("peda-session-#FILENAME#.txt", "target file to save peda session"),
    "tracedepth": (0, "max depth for calls/instructions tracing, 0 means no limit"),
    "tracelog"  : ("peda-trace-#FILENAME#.txt", "target file to save tracecall output"),
    "crashlog"  : ("peda-crashdump-#FILENAME#.txt", "target file to save crash dump of fuzzing"),
    "snapshot"  : ("peda-snapshot-#FILENAME#.raw", "target file to save crash dump of fuzzing"),
    "autosave"  : ("on", "auto saving peda session, e.g: on|off"),
    "payload"   : ("peda-payload-#FILENAME#.txt", "target file to save output of payload command"),
    "context"   : ("register,code,stack", "context display setting, e.g: register, code, stack, all"),
    "clearscr"  : ("on", "clear screen for each context display"),
    "verbose"   : ("off", "show detail execution of commands, e.g: on|off"),
    "debug"     : ("off", "show detail error of peda commands, e.g: on|off"),
    "_teefd"    : ("", "internal use only for tracelog/crashlog writing")
}

class Option(object):
    """
    Class to access global options of PEDA commands and functions
    TODO: save/load option to/from file
    """
    options = OPTIONS.copy()
    def __init__(self):
        """option format: name = (value, 'help message')"""
        pass

    def get(name):
        """get option"""
        if name in Option.options:
            return Option.options[name][0]
        else:
            return None




def tmpfile(pref="peda-", is_binary_file=False):
    """Create and return a temporary file with custom prefix"""

    mode = 'w+b' if is_binary_file else 'w+'
    return tempfile.NamedTemporaryFile(mode=mode, prefix=pref)

def execute_redirect(gdb_command, silent=False):
 
    result = None
    #init redirection
    if silent:
        logfd = open(os.path.devnull, "r+")
    else:
        logfd = tmpfile()
    logname = logfd.name
    gdb.execute('set logging off') # prevent nested call
    gdb.execute('set height 0') # disable paging
    gdb.execute('set logging file %s' % logname)
    gdb.execute('set logging overwrite on')
    gdb.execute('set logging redirect on')
    gdb.execute('set logging on')
    try:
        gdb.execute(gdb_command)
        gdb.flush()
        gdb.execute('set logging off')
        if not silent:
            logfd.flush()
            result = logfd.read()
        logfd.close()
    except Exception as e:
        gdb.execute('set logging off') #to be sure
        if Option.get("debug") == "on":
            msg('Exception (%s): %s' % (gdb_command, e), "red")
            traceback.print_exc()
        logfd.close()
    if Option.get("verbose") == "on":
        msg(result)
    return result
 
 
class bp(gdb.Breakpoint):
    def stop(self):
        global encode, idx, check
        if idx % 2 == 0:
            x = execute_redirect("x/s $rax")
            encode = x.split(":")[0]
            check[int(idx / 2)] = int(encode, 16)
        idx += 1
        
 
 
bp("*0x5555555580d9")


 
def main():
    global encode, idx, check
    code = ["_"] * 0x22
    for j in range(0x22):
        for i in string.printable:
            code[j] = i
            if i == "\"" or i == "`" or i == "'" or i == "\\":
                code[j] = "\\" + i 

            idx = 0
            check = [-1]*0x23

            print("USING:",''.join(code) + '\n')
            gdb.execute("run < <(python -c \"print '" + ''.join(code) + "'\")")

            if check[j] == 0:
                break

main()