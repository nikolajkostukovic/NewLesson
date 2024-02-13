from Controllers import generalScript
from Controllers import controllerBot

class Main:

    def __init__(self):
        pass

    def startParserCurrency(self):
        script = generalScript.GeneralScript();
        script.startScript()
        bot = controllerBot.ControllerBot()
        bot.startBot()

if "__main__" == __name__:
    mainClass = Main()
    mainClass.startParserCurrency()













