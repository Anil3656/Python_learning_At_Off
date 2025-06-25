class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return  value

#List = [1,2,3,4,5,6,7]
List = [7,6,5,4,3,2,1]
rev = ReverseList(List)
for ele in rev:
    print(ele,end=" ")
