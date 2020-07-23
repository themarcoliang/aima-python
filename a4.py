def check_format(rule):
    return False

def load(parameters):
    if len(parameters) == 0:
        print("Error: missing file name")
        return
    if len(parameters) > 1:
        print("Error: program does not support loading multiple files")
        return
    try:
        f = open(parameters[0], "r")
    except:
        print("Error: failed to open file \"{}\"".format(parameters[0]))
        return
    lines = f.readlines()
    for line in lines:
        if check_format(line) == False:
            print("Error: {} is not a valid knowledge base".format(parameters[0]))
            return

def tell(parameters):
    print("tell")
    print(parameters)

def infer_all():
    print("infer_all")

def driver():
    while(True):
        command = input("kb> ")
        if command == "":
            continue
        split_command = command.split()
        function = split_command[0]
        del split_command[0]
        if(function == "load"):
            load(split_command)
        elif(function == "tell"):
            tell(split_command)
        elif(function == "infer_all"):
            infer_all()
        else:
            print("Error: unknown command \"{}\"".format(function))
            continue

if __name__ == '__main__':
    driver()