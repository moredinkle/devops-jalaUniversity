import virtualbox
vbox = virtualbox.VirtualBox()

def list():
    print("Available machines:\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))

def start(name):
    session = virtualbox.Session()
    machine = vbox.find_machine(name)
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()
    print("machine running")


def checkMachine(name,action):
    aux = name.split()
    if(aux[1] in machines):
        if(action == "start"): start(aux[1])
        elif(action == "shutdown"): shutdown(aux[1])
    else: print("machine not found")


def shutdown(name):
    global vbox
    vm = vbox.find_machine(name)
    session = vm.create_session()
    session.console.power_down()
    print("machine off")

def create(name):
    global vbox
    m = vbox.create_machine("",name,['/'],"Linux",'forceOverwrite=0')
    vbox.register_machine(m)

def delete(name):
    vm = vbox.find_machine(name)
    vm.remove(delete=True)


txt = """----vmcli----
available commands:
 + list
 + start *vm_name*
 + shutdown *vm_name*
 + create *vm_name*
 + delete *vm_name*
 + help
 + exit"""

print(txt)
machines = []
for m in vbox.machines:
    machines.append(m.name)


while(True):
    print("\n")
    cmd = input()
    if(cmd == "list"): list()
    elif("start" in cmd): checkMachine(cmd, "start")
    elif("shutdown" in cmd): checkMachine(cmd, "shutdown")
    elif("create" in cmd): create(cmd.split()[1])
    elif("delete" in cmd): delete(cmd.split()[1])
    elif(cmd == "exit"): break
    elif(cmd == "help"): print(txt)