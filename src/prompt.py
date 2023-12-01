class Prompt():

    def __init__(self, message):
        self._message = message
        self._input = None

    def getMessage(self):
        return self._message
    
    def setMessage(self, newMessage):
        self._message = newMessage

    def getInput(self):
        return self._input
    
    def setInput(self, input):
        self._input = input
    
    def talk(self):
        answer = input(self.getMessage())
        self.setInput(answer)
        return self.getInput()
        