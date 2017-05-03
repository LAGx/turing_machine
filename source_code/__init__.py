import parse_T
import file_T
import variable

print("-Reading settings...")
file_T.readSettings()
print("-Load file...")
file_T.loadFile()


print("-Removeing space and tabs...")
parse_T.removeTabSpaceComments()
print("-Checking syntax...")
parse_T.checkSyntax()


print("-Load data to flash memory...")
parse_T.loadArrays()


print("-Prepear files to generate mt code...")
file_T.prepearFilesToGenerateCode()


print("-Generating mt code...")
parse_T.generateCode()
print("-Checking for double comands...")
parse_T.checkDoubleCommand()
print("-Generating good q<number> states")
parse_T.generateValidStates()

if file_T.fileToGenerate.find(".cmd") != -1:
    print("-Converting to .cmd onishenko format...")
    parse_T.convertToCMD()
else:
    print("WARNING: code was not generate to .cmd onishenko format")

print("-Generate done!")
