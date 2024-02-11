from Controllers import generalScript

class Main:

    def __init__(self):
        pass

    def startParserCurrency(self):
        script = generalScript.GeneralScript();
        script.startScript()

if "__main__" == __name__:
    mainClass = Main()
    mainClass.startParserCurrency()

