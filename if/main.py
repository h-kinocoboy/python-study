class Spam:
    def __init__(self):
        self.checkVal(0)
        self.checkVal(1)
    def checkVal(self, val):
        if val > 0:
            print('val > 0 check')
            print('{}'.format(val > 0))

            print('val == 0 check')
            print('{}'.format(val==0))
        elif val == 0:
            print('val == 0 check')
            print('{}'.format(val == 0))
Spam()