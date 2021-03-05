# from angr import * 
import angr
import claripy 


project = angr.Project('rop_easy', main_opts={"base_addr":0}, auto_load_libs=False)

main = 0x3050
good = 0x4004
bad =  0x4016

state = project.factory.entry_state(addr=main)
#state = project.factory.entry_state(args = ["jack", flag_string])

sim_mgr = project.factory.simulation_manager(state)

sim_mgr.explore(find = good, avoid = bad)

result = sim_mgr.found[0]

for i in range(3):
    print(result.posix.dumps(i))