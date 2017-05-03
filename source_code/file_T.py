import time

configFile = "config.txt"
fileToload = "TuringMachine.txt"
fileToGenerate = "turing_onishenko.cmd"


def readSettings():
    global fileToload, fileToGenerate
    try:
        file = open("work\\" + configFile, "r")
    except IOError as e:
        print("Error: no config.txt file. Generating new one...")
        new_file = open("work\\" + configFile, "w")
        new_file.write("FileToLoad:" + fileToload + "\n")
        new_file.write("FileToGenerate:" +fileToGenerate)
    else:
        fileToload = file.readline()[11:-1:]
        fileToGenerate = file.readline()[15::]


def loadFile():
    global fileToload, fileToGenerate
    mainFile = open("work\\" + fileToGenerate, "w")
    mainFile.close()
    mainFile = open("work\\" + fileToGenerate, "r+")
    try:
        uploadFile = open("work\\" + fileToload, "r")
    except IOError as e:
        print("ERROR: no " + fileToload + " to load.")
        time.sleep(3000)
    else:
        mainFile.write(uploadFile.read())
        uploadFile.close()
    mainFile.close()

def prepearFilesToGenerateCode():
    old = open("work\\" + fileToGenerate, "r")

    clean = open("subfile", "w")

    isClearing = True
    while True:
        line = old.readline()
        if not line: break

        if(line.find("}") != -1):
            continue

        if(line.find("{") != -1):
            isClearing = False
            continue
        if not isClearing:
            clean.write(line)

    old.close()
    clean.close()

    old = open("work\\" + fileToGenerate, "w")
    old.close()

