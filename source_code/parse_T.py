import file_T
import variable
import os

def removeTabSpaceComments():
    mainFile = open("work\\" + file_T.fileToGenerate, "r")
    file = open("subfile", "w")

    isComment = False
    line_n = 0;
    while True:
        line_n += 1
        line = mainFile.readline()
        if not line: break
        line = line.replace(line, line[:-1:].replace('	', '').replace(' ', '')+"\n")
        line = line.lower()

        if not (line.find("/*") == -1):
            isComment = True
        if not (line.find("*/") == -1):
            isComment = False
            line = line.replace(line, "")

        if isComment:
            line = line.replace(line, "")

        if not (line.find("//") == -1):
            line = line[:line.find("//"):] + "\n"

        if line == "\n":
            line = line.replace(line, "")

        file.write(line)

    file.close()
    file = open("subfile", "r")
    mainFile.close()
    mainFile = open("work\\" + file_T.fileToGenerate, "w")

    mainFile.write(file.read())
    mainFile.close()
    file.close()


def checkSyntax():
    mainFile = open("work\\" + file_T.fileToGenerate, "r")

    line_n = 0
    isCheckHead = [False, False] #(1)isHead (2)isWasInit
    isCheckBody = [False, False] #(1)isBody (2)isWasInit

    isHeadBlock = False
    isBodyBlock = False

    initHead = False
    initBody = False
    while True:
        line_n += 1
        line = mainFile.readline()
        if not line: break
#checking [] {}
        if not (line.find("[") == -1):
            if isCheckHead[1]:
                print("ERROR: was one '[', error at line " + str(line_n))
            isCheckHead[0] = True
            isCheckHead[1] = True
            isHeadBlock = True
        if not (line.find("]") == -1):
            if not isCheckHead[1]:
                print("ERROR: wasn`t '[', error at line " + str(line_n))
            isCheckHead[0] = False
            isHeadBlock = False

        if not (line.find("{") == -1):
            if isCheckBody[1]:
                print("ERROR: was one '{', error at line " + str(line_n))
            isCheckBody[0] = True
            isCheckBody[1] = True
            isBodyBlock = True
        if not (line.find("}") == -1):
            if not isCheckBody[1]:
                print("ERROR: wasn`t '{', error at line " + str(line_n))
            isCheckBody[0] = False
            isBodyBlock = False

        if isHeadBlock and isBodyBlock:
            print("ERROR: head and body conflict at line " + str(line_n))


        if isHeadBlock and initHead:
            split = line[:-1:].split(":")
            if not (len(split) == 3):
                print("ERROR: bad array format at line " + str(line_n))

            if not (split[0] == variable.Value.type or split[0] == variable.Move.type or split[0] == variable.State.type):
                print("ERROR: bad variable type at line " + str(line_n))

            if not (split[1].isdigit()):
                print("ERROR: bad size of array at line " + str(line_n))

            if (split[2].find("+") == -1):
                if  (split[2].find("=") == -1 or split[2].find("(") == -1 or split[2].find(")") == -1):
                    print("ERROR: bad declaration of array at line " + str(line_n))

            #var = ((split[2].split("="))[1])[1:-1:].split(",")

        if isBodyBlock:
            if initBody:
                split = line[:-1:].split(":")
                if not (len(split) == 2):
                    print("ERROR: bad command format at line " + str(line_n))

                if not (len(split[0].split(",")) == 2):
                    print("ERROR: invalid arguments before ':' at line " + str(line_n))

                if not (len(split[1].split(",")) == 3):
                    print("ERROR: invalid arguments after ':' at line " + str(line_n))

            initBody = True


        initHead = True
    mainFile.close()

def loadArrays():

    mainFile = open("work\\" + file_T.fileToGenerate, "r")

    line_n = 0
    while True:
        line_n += 1
        line = mainFile.readline()[:-1:]
        if not line: break

        if(line.find("\"") == -1):
            if( line.split(":")[0] == variable.Value.type ):
                variable.Value(str((line.split(":")[2]).split("=")[0]), int(line.split(":")[1]), list(((line.split(":")[2]).split("=")[1])[1:-1:].split(",")))

            if( line.split(":")[0] == variable.State.type):
                variable.State(str((line.split(":")[2]).split("=")[0]), int(line.split(":")[1]), list(((line.split(":")[2]).split("=")[1])[1:-1:].split(",")))
        else:
            if (line.split(":")[0] == variable.Value.type):
                variable.Value(name = str((line.split(":")[2]).split("=")[0]), length = int(line.split(":")[1]), elements = str(line.split("=")[1].split("+")[0]), append = str((line.split("=")[1].split("+")[1])[1:-1:]))

            if (line.split(":")[0] == variable.State.type):
                variable.State(name = str((line.split(":")[2]).split("=")[0]), length = int(line.split(":")[1]), elements = str(line.split("=")[1].split("+")[0]), append = str((line.split("=")[1].split("+")[1])[1:-1:]))

        if(line.split(":")[0] == variable.Move.type):
            variable.Move(str((line.split(":")[2]).split("=")[0]), int(line.split(":")[1]), list(((line.split(":")[2]).split("=")[1])[1:-1:].split(",")))

    mainFile.close()


def generateCode():


    sourse = open("subfile", "r")
    final = open("work\\" + file_T.fileToGenerate, "w")
    line_n = 0
    while True:
        line_n += 1
        isStateArInCommand = [False, False]
        isValueArInCommand = [False, False]
        isMoveArInCommand = False
        line = sourse.readline()[:-1:]
        if not line: break

#get all info "is"
        for l in variable.listStates:
            if(l.name == line.split(":")[0].split(",")[0]):
                isStateArInCommand[0] = True
            if(l.name == line.split(":")[1].split(",")[0]):
                isStateArInCommand[1] = True

        for l in variable.listValues:
            if(l.name == line.split(":")[0].split(",")[1]):
                isValueArInCommand[0] = True
            if(l.name == line.split(":")[1].split(",")[1]):
                isValueArInCommand[1] = True

        for l in variable.listMoves:
            if(l.name == line.split(":")[1].split(",")[2]):
                isMoveArInCommand = True

        #print(isStateArInCommand, isValueArInCommand, isMoveArInCommand)
#identify operations

        if   isStateArInCommand[0] == False and isStateArInCommand[1] == False and isValueArInCommand[0] == False and isValueArInCommand[1] == False and isMoveArInCommand == False:#1
            final.write(line.replace("*", "") + "\n")
        elif isStateArInCommand[0] == True  and isStateArInCommand[1] == True  and isValueArInCommand[0] == False and isValueArInCommand[1] == False and isMoveArInCommand == False:#2
            obj1 = variable.State
            obj2 = variable.State
            for l in variable.listStates:
                if(l.name == line.split(":")[0].split(",")[0]):
                    obj1 = l
                if(l.name == line.split(":")[1].split(",")[0]):
                    obj2 = l
            if(obj1.length != obj2.length):
                print("ERROR: different length of states in line" + line_n)

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj1.length):
                command = obj1.arr[i] + "," + split[1] + ":" + obj2.arr[i] + "," + split[3] + "," + split[4] + "\n"
                command.replace("*", "")
                final.write(command)

        elif isStateArInCommand[0] == False and isStateArInCommand[1] == False and isValueArInCommand[0] == True  and isValueArInCommand[1] == True  and isMoveArInCommand == False:#3
            obj1 = variable.Value
            obj2 = variable.Value
            for l in variable.listValues:
                if (l.name == line.split(":")[0].split(",")[1]):
                    obj1 = l
                if (l.name == line.split(":")[1].split(",")[1]):
                    obj2 = l

            if(obj1.length != obj2.length):
                print("ERROR: different length of values in line" + line_n)

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj1.length):
                command = split[0] + "," + obj1.arr[i] + ":" + split[2] + "," + obj2.arr[i] + "," + split[4] + "\n"
                command.replace("*", "")
                final.write(command)

        elif isStateArInCommand[0] == False and isStateArInCommand[1] == False and isValueArInCommand[0] == False and isValueArInCommand[1] == False and isMoveArInCommand == True :#4
            obj = variable.Move
            for l in variable.listMoves:
                if (l.name == line.split(":")[1].split(",")[2]):
                    obj = l

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj.length):
                command = split[0] + "," + split[1] + ":" + split[2] + "," + split[3] + "," + obj.arr[i] + "\n"
                command.replace("*", "")
                final.write(command)

        elif isStateArInCommand[0] == True  and isStateArInCommand[1] == False and isValueArInCommand[0] == False and isValueArInCommand[1] == False and isMoveArInCommand == False:#5
            obj = variable.State
            for l in variable.listStates:
                if (l.name == line.split(":")[0].split(",")[0]):
                    obj = l

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj.length):
                command = obj.arr[i] + "," + split[1] + ":" + split[2] + "," + split[3] + "," + split[4] + "\n"
                command.replace("*", "")
                final.write(command)

        elif isStateArInCommand[0] == False and isStateArInCommand[1] == True  and isValueArInCommand[0] == False and isValueArInCommand[1] == False and isMoveArInCommand == False:#6
            obj = variable.State
            for l in variable.listStates:
                if (l.name == line.split(":")[1].split(",")[0]):
                    obj = l

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj.length):
                command = split[0] + "," + split[1] + ":" + obj.arr[i]+ "," + split[3] + "," + split[4] + "\n"
                command.replace("*", "")
                final.write(command)

        elif isStateArInCommand[0] == False and isStateArInCommand[1] == False and isValueArInCommand[0] == True  and isValueArInCommand[1] == False and isMoveArInCommand == False:#7
            obj = variable.Value
            for l in variable.listValues:
                if (l.name == line.split(":")[0].split(",")[1]):
                    obj = l

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj.length):
                command = split[0] + "," + obj.arr[i] + ":" + split[2] + "," + split[3] + "," + split[4] + "\n"
                command.replace("*", "")
                final.write(command)
        elif isStateArInCommand[0] == False and isStateArInCommand[1] == False and isValueArInCommand[0] == False and isValueArInCommand[1] == True  and isMoveArInCommand == False:#8
            obj = variable.Value
            for l in variable.listValues:
                if (l.name == line.split(":")[1].split(",")[1]):
                    obj = l

            split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
            for i in range(0, obj.length):
                command = split[0] + "," + split[1] + ":" + split[2] + "," + obj.arr[i] + "," + split[4] + "\n"
                command.replace("*", "")
                final.write(command)
        else:
            print("ERROR: bad using array in command!")




    sourse.close()
    final.close()
    os.remove("subfile")


def checkDoubleCommand():

    file = open("work\\" + file_T.fileToGenerate, "r")
    line_n = 0
    ls = []
    while True:
        line_n += 1
        line = file.readline()
        if not line: break

        curr = line.split(":")[0]

        if(ls.count(curr) > 0):
            print("ERROR: dublicate commands at line " + str(line_n))

        ls.append(curr)

    file.close()



def generateValidStates():
    gener = open("work\\" + file_T.fileToGenerate, "r")
    subfile = open("subfile", "w")
    subfile.write(gener.read())
    gener.close()
    subfile.close()

    gener = open("work\\" + file_T.fileToGenerate, "w")
    subfile = open("subfile", "r")

    found_states = [] #[name state, number]
    last_free_number = 1
    while True:
        line = subfile.readline()
        if not line: break

        split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
        first_state = line.split(":")[0].split(",")[0]
        wasFound = False
        if (first_state != "q0"):
            for f in found_states:
                if f[0] == first_state:
                    wasFound = True
                    break

            if not wasFound:
                found_states.append([first_state, last_free_number])
                line = "q"+ str(last_free_number) + "," + split[1] + ":" +split[2]+"," + split[3]+ "," + split[4]
                last_free_number += 1
            else:
                for f in found_states:
                    if(f[0] == first_state):
                        line = "q" + str(f[1]) + "," + split[1] + ":" +split[2]+"," + split[3]+ "," + split[4]
                        break


        split = line.split(":")[0].split(",") + line.split(":")[1].split(",")
        sec_state = line.split(":")[1].split(",")[0]
        wasFound = False
        if (sec_state != "q0" and sec_state != "!"):
            for f in found_states:
                if f[0] == sec_state:
                    wasFound = True
                    break

            if not wasFound:
                found_states.append([sec_state, last_free_number])
                line = split[0] + "," + split[1] + ":" +"q"+ str(last_free_number)+"," + split[3]+ "," + split[4]
                last_free_number += 1
            else:
                for f in found_states:
                    if(f[0] == sec_state):
                        line = split[0] + "," + split[1] + ":" +"q" + str(f[1])+"," + split[3]+ "," + split[4]
                        break

        if(last_free_number > 10000):
            print("ERROR: q<number>, number over 10000.")
            
        gener.write(line)

    gener.close()
    subfile.close()
    os.remove("subfile")

def convertToCMD():
    gener = open("work\\" + file_T.fileToGenerate, "r")
    subfile = open("subfile", "w")
    subfile.write(gener.read())
    gener.close()
    subfile.close()

    gener = open("work\\" + file_T.fileToGenerate, "w")
    subfile = open("subfile", "r")

    gener.write("{\\rtf1\\ansi\\ansicpg1251\deff0\deflang1049{\\fonttbl{\\f0\\fswiss\\fcharset0 Tahoma;}{\\f1\\fnil MS Sans Serif;}}\\viewkind4\\uc1\pard\lang1033\\f0\\fs20")
    while True:
        line = subfile.readline()
        if not line: break

        gener.write("\par " + line)


    gener.write("\par }")
    gener.close()
    subfile.close()
    os.remove("subfile")



















