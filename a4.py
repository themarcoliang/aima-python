# is_atom and is_letter are taken from assignment specifications
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def check_format(split_rule):
    if is_atom(split_rule[0]) == False:
        return False
    if split_rule[1] != "<--":
        return False
    for item in split_rule[2:]:
        # print("checking item", item)
        if item != "&" and not is_atom(item):
            return False
    return True

def load(rules, parameters):
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
        split_line = line.split()
        if check_format(split_line) == False:
            print("Error: {} is not a valid knowledge base".format(parameters[0]))
            rules = {}
            return
        else:
            head = split_line[0]
            items_to_append = []
            del split_line[0]
            del split_line[0]
            for item in split_line:
                if item == "&":
                    continue
                else:
                    items_to_append.append(item)
            rules[head] = items_to_append

def tell(true_atoms, parameters):
    for atom in parameters:
        if not is_atom(atom):
            print("Error: \"{}\" is not a valid atom".format(atom))
        if atom in true_atoms:
            print("Atom \"{}\" already known to be true".format(atom))
        else:
            true_atoms.append(atom)
            print("\"{}\" added to KB".format(atom))

def infer_all():
    print("infer_all")

def driver():
    loaded = False
    while(True):
        command = input("kb> ")
        if command == "":
            continue
        split_command = command.split()
        function = split_command[0]
        del split_command[0]
        if(function == "load"):
            loaded = True
            #reset heads and true_atoms since it's a new KB whenever load is called
            rules = {}
            true_atoms = []
            load(rules, split_command)
        elif(function == "tell"):
            if loaded == False:
                print("Error: No KB Loaded")
                continue
            tell(true_atoms, split_command)
        elif(function == "infer_all"):
            if loaded == False:
                print("Error: No KB Loaded")
                continue
            infer_all()
        else:
            print("Error: unknown command \"{}\"".format(function))
            continue

if __name__ == '__main__':
    driver()