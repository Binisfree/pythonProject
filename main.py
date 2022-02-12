# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

class MyFirstClass:
    msg = 'The best way to predict the future is to invent it.'
    def __init__(self):
    def classMethod(self):
        print(MyFirstClass.msg + '\t- Alan Curtis Kay -')

mfc = MyFirstClass()

print(mfc.msg)
mfc.classMethod()