class Soma:
    def __init__(self, *args):
        self.args = args

    def calcula(self):
        return sum(self.args)


if __name__ == "__main__":
    print(Soma(20, 30).calcula())
    print(Soma(40, 50).calcula())
    print(Soma(30, 50, 60, 900).calcula())
    print(Soma(40, 70, 80, 1000).calcula())