import telebot

class ControllerBot:

    bot = telebot.TeleBot("6840229618:AAGLrsyIOW9pNyJfy9cPDRkW9QvNXW5VsbM")
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls,*args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

    @bot.message_handler(content_types=['text'])
    def message_hendler(self):
        if self.text == "/start":
            ControllerBot.bot.send_message(self.from_user.id, "Hello")
        else:
            ControllerBot.bot.send_message(self.from_user.id, "Fuck off")


    def startBot(self):
        self.bot.polling(none_stop=True, interval=0)


