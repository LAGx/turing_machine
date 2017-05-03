import copy

allowSymbol = ('!','*','_' , 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

listValues = []
listStates = []
listMoves = []


class Value:
    type = "value"

    def __init__(self, name, length, elements, append = None):
        if(append == None):
            if not (length == len(elements)):
                print("ERROR: invalid lenth of value ")
            self.length = length

            for letter in name:
                isGoodWord = False
                for aw in allowSymbol:
                    if (letter == aw):
                        isGoodWord = True
                        break
                if not isGoodWord:
                    print("ERROR: unallow symbol in value name")
            self.name = name

            for word in elements:
                for letter in word:
                    isGoodWord = False
                    for aw in allowSymbol:
                        if (letter == aw):
                            isGoodWord = True
                            break
                    if not isGoodWord:
                        print("ERROR: unallow symbol in name in value")

            self.arr = elements
            for l in listValues:
                if (l.name == self.name):
                    print("ERROR: Redefinition of value " + self.name)
            listValues.append(self)
        else:
            self.arr = []
            for letter in name:
                isGoodWord = False
                for aw in allowSymbol:
                    if (letter == aw):
                        isGoodWord = True
                        break
                if not isGoodWord:
                    print("ERROR: unallow symbol in value name")
            self.name = name

            isWasOld = False
            for l in listValues:
                if(l.name == elements):
                    self.arr = copy.deepcopy(l.arr)

                    if not (length == l.length):
                       print("ERROR: invalid length for new modificaton value '" + name + "' and old '" + l.name  + "'")
                    isWasOld = True
            self.length = length

            if not isWasOld:
                print("ERROR: no such old value")

            for i in range(0, len(self.arr)):
                self.arr.insert(i, self.arr.pop(i) + append)

            for l in listValues:
                if(l.name == self.name):
                    print("ERROR: Redefinition of value " + self.name)
            listValues.append(self)


class State:
    type = "state"

    def __init__(self, name, length, elements, append = None):
        if(append == None):
            if not (length == len(elements)):
                print("ERROR: invalid lenth of state ")
            self.length = length

            for letter in name:
                isGoodWord = False
                for aw in allowSymbol:
                    if (letter == aw):
                        isGoodWord = True
                        break
                if not isGoodWord:
                    print("ERROR: unallow symbol in state name")
            self.name = name

            for word in elements:
                for letter in word:
                    isGoodWord = False
                    for aw in allowSymbol:
                        if (letter == aw):
                            isGoodWord = True
                            break
                    if not isGoodWord:
                        print("ERROR: unallow symbol in name in state")

            self.arr = elements
            for l in listStates:
                if (l.name == self.name):
                    print("ERROR: Redefinition of state " + self.name)
            listStates.append(self)
        else:
            self.arr = []
            for letter in name:
                isGoodWord = False
                for aw in allowSymbol:
                    if (letter == aw):
                        isGoodWord = True
                        break
                if not isGoodWord:
                    print("ERROR: unallow symbol in state name")
            self.name = name

            isWasOld = False
            for l in listStates:
                if(l.name == elements):
                    self.arr = copy.deepcopy(l.arr)

                    if not (length == l.length):
                       print("ERROR: invalid length for new modificaton state '" + name + "' and old '" + l.name  + "'")
                    isWasOld = True
            self.length = length

            if not isWasOld:
                print("ERROR: no such old state")

            for i in range(0, len(self.arr)):
                self.arr.insert(i, self.arr.pop(i) + append)

            for l in listStates:
                if(l.name == self.name):
                    print("ERROR: Redefinition of state " + self.name)
            listStates.append(self)


class Move:
    type = "move"
    allow = ["r", "l", "s"]

    def __init__(self, name,length, elements):

        for letter in name:
            isGoodWord = False
            for aw in allowSymbol:
                if (letter == aw):
                    isGoodWord = True
                    break
            if not isGoodWord:
                print("ERROR: unallow symbol in move name")
        self.name = name

        if not (length == len(elements)):
            print("ERROR: invalid lenth of move")
        if (length > 3):
            print("ERROR: too long move array")
        self.length = length


        for letter in elements:
            isGoodWord = False
            for aw in self.allow:
                if (letter == aw):
                    isGoodWord = True
                    break
            if not isGoodWord:
                print("ERROR: unallow symbol in name in move")
        self.arr = elements


        for l in listStates:
            if (l.name == self.name):
                print("ERROR: Redefinition of move " + self.name)
        listMoves.append(self)