while(True):
    command = input("kb> ")
    split_command = command.split()
    function = split_command[0]
    if(function == "load"):
        print("load")
    elif(function == "tell"):
        print("tell")
    elif(function == "infer_all"):
        print("infer_all")
    else:
        print("Error: unknown command \"{}\"".format(function))
        continue