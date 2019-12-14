class ReadBigFile:
    def __init__(self):
        self.filename = "lesson26/convertcsv.csv"

    def __iter__(self):
        with open(self.filename) as file:
            yield from file


for line in ReadBigFile():
    print(line)