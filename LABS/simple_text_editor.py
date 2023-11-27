import sys


class CustomStack:
    def __init__(self):
        self.text = ""
        self.stack = []

    def insert(self, value):
        self.text += value
        self.stack.append(self.text)

    def delete(self, value):
        self.text = self.text[:-value]
        self.stack.append(self.text)

    def get(self, index):
        if 0 <= index < len(self.text):
            return self.text[index]
        return None  # Return None if the index is out of bounds

    def undo(self):
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.text = self.stack[-1]
            else:
                self.text = ""


text1 = CustomStack()
string = input()
Arr = string.split(",")

for i in Arr:
    if i[0] == "1":
        cmd, val = i.split(" ")
        text1.insert(val)
    elif i[0] == "2":
        cmd, val = i.split(" ")
        text1.delete(int(val))
    elif i[0] == "3":
        cmd, val = i.split(" ")
        result = text1.get(int(val) - 1)
        print(result)
    elif i[0] == "4":
        text1.undo()
