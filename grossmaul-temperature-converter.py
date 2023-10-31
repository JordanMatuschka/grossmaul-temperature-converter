from grossmaulplugin import GrossmaulPlugin

""" Simple automatic temperature helper """
class TemperatureConverterPlugin(GrossmaulPlugin):
    def __init__(self):
        self.OPERATORS = {'degrees C' : self.opToF, 'degrees c' : self.opToF, 'degrees F' : self.opToC, 'degrees f' : self.opToC}
        self.COMMANDS = { }
        self.PROCESSCOMMANDS = { }

    def FtoC(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        celsius = round(celsius, 1)
        return "(%s degrees fahrenheit is %.1f degrees celsius)" % (fahrenheit, celsius)

    def CtoF(self, celsius):
        fahrenheit = (celsius * 9) / 5 + 32
        fahrenheit = round(fahrenheit, 1)
        return "(%s degrees celsius is %.1f degrees fahrenheit)" % (celsius, fahrenheit)
        
    def opToC(self, message, sender, STATE, private=False):
        # check to see if the token before the operator exists and is numeric
        # example:
        # It's definitely November, a brisk 28 degrees F tonight
        if(len(message.split('degrees')) == 2):
            message = message.split('degrees')[0].rstrip()
            # It's definitely November, a brisk 28
            message = message.split(' ')[-1]
            # 28
            try:
                # isnumeric() doesn't account for negative numbers, so we try/catch
                fahrenheit = float(message)
                return self.FtoC(fahrenheit)
            except:
                return

    def opToF(self, message, sender, STATE, private=False):
        if(len(message.split('degrees')) == 2):
            message = message.split('degrees')[0].rstrip()
            message = message.split(' ')[-1]
            try:
                celsius = float(message)
                return self.CtoF(celsius)
            except:
                return
