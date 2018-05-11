"""Logic Gates and Circuits"""


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.inputA = None
        self.inputB = None

    def getPinA(self):
        if self.inputA == None:
            return int(input('Enter Pin A input for the gate {} -->'.format(self.getLabel())))
        else:
            return self.inputA.getFrom().getOutput()


    def getPinB(self):
        if self.inputB == None:
            return int(input('Enter Pin B input for the gate {} -->'.format(self.getLabel())))
        else:
            return self.inputB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.inputA == None:
            self.inputA = source
        else:
            if self.inputB == None:
                self.inputB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")



class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self,n)

        self.input = None

    def getPin(self):
        if self.input == None:
            return int(input('Enter Pin input for the gate {} -->'.format(self.getLabel())))
        else:
            return self.input.getFrom().getOutput()

    def setNextPin(self, source):
        if self.input == None:
            self.input= source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")



class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a= self.getPinA()
        b = self.getPinB()

        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b==0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()

        if a == 0:
            return 1
        else:
            return 0

class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def performGateLogic(self):
        if super().performGateLogic() ==1:
            return 0
        else:
            return 1



class Connector:
    def __init__(self, fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate



def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


if __name__ == '__main__':
    main()

