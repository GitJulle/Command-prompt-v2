import time
import subprocess

lombo = False
long_ago = False
provisated = False

custom_commands = []
beta_commands = []

print("Command prompt 2.0 started.")
print()
while True:
    cmd = input("cmd: ")
    if cmd == "fried chicken":
        print("So you know what fried chicken is.")
        print("KFC sells fried chicken and they are a fast food brand.")
        print("KFC makes good food.")
    elif cmd == "lib":
        cmd = input("file/libraries: ")
        if cmd == "turbolated":
            print("Not supported yet!")
        elif cmd == "lombo":
            print("lombo pack loaded!")
            lombo = True
        elif cmd == "long ago":
            print("long ago package has now been activated")
            long_ago = True
        elif cmd == "provisated":
            print("provisated is in beta, do you want to load it anyway? Y/N")
            cmd = input(">")
            if cmd == "Y":
                provisated = True
            elif cmd == "N":
                print("ok")
            else:
                pass
    elif cmd == "command maker" and long_ago:
        print("Making a command. Try it!")
        name = input("name: ")
        action = input("output: ")
        custom_commands.append({"name": name, "action": action})
    elif cmd == "command maker v2" and long_ago and provisated:
        print("WARNING, This is still in alpha and maybe wont work as you expect it too.")
        name = input("name: ")
        action = input("action: ")
        if action == "write":
            string = input("text: ")
            beta_commands.append({"name": name, "action": action, "text": string})
        else:
            beta_commands.append({"name": name, "action": action})


    else:
        for i in custom_commands:
            if cmd == i["name"]:
                print(i["action"])
        for i in beta_commands:
            if cmd == i["name"]:
                if i["action"] == "write":
                    print(i["text"])
                elif i["action"] == "clear":
                    subprocess.run("cls", shell=True)
                    print("Command prompt 2.0 started.")
                    print()
                elif i["action"] == "annoy":
                    string = input()
                    print(string)
                elif i["action"] == "kill":
                    exit(0)
