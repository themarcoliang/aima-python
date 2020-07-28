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
            print(line)
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
    for line in lines:
        print(line, end="")
    print("\n{} new rule(s) added".format(len(lines)))
    f.close()

def tell(rules, true_atoms, parameters):
    for atom in parameters:
        if not is_atom(atom):
            print("Error: \"{}\" is not a valid atom".format(atom))
        if atom in true_atoms:
            print("Atom \"{}\" already known to be true".format(atom))
        elif atom in rules.keys():
            print("Cannot tell {} to be true because it's a head atom".format(atom))
        else:
            true_atoms.add(atom)
            print("\"{}\" added to KB".format(atom))

def infer_all(rules, true_atoms):
    inferred_atoms = set()
    while True:
        length = len(inferred_atoms)
        for head, atoms in rules.items():
            combined_atoms = true_atoms|inferred_atoms
            if all(a in combined_atoms for a in atoms) and head not in combined_atoms:
                inferred_atoms.add(head)
        if len(inferred_atoms) == length:
            break
    print("Newly inferred atoms:")
    if(inferred_atoms == set()):
        print("None")
    else:
        print(inferred_atoms)
    print("Atoms already known to be true:")
    if(true_atoms == set()):
        print("None")
    else:
        print(true_atoms)
    return inferred_atoms|true_atoms

def driver():
    loaded = False
    print("\nAvailable Commands:")
    print("load <kb file> : loads the specified knowledge base file")
    print("tell <atom1> <atom2>... : tells the kb that the atoms are true")
    print("note that it's possible to tell an atom that does not exist in the kb!")
    print("infer_all: kb infers all possible atoms from given information")
    print("exit: exits program\n")
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
            true_atoms = set()
            load(rules, split_command)
        elif(function == "tell"):
            if loaded == False:
                print("Error: No KB Loaded")
                continue
            tell(rules, true_atoms, split_command)
        elif(function == "infer_all"):
            if loaded == False:
                print("Error: No KB Loaded")
                continue
            true_atoms = infer_all(rules, true_atoms)
        elif(function == "exit"):
            print("Program Terminating")
            return
        else:
            print("Error: unknown command \"{}\"".format(function))
            continue

if __name__ == '__main__':
    driver()