import random


class Cell:
    def __init__(self, number=0, is_mine=False, is_open=False):
        self.number = number
        self.is_mine = is_mine  
        self.is_open = is_open 

    @property
    def is_mine(self):
        return self.__is_mine
    @is_mine.setter
    def is_mine(self, other):
        if type(other) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = other

    @property
    def is_open(self):
        return self.__is_open
    @is_open.setter
    def is_open(self, other):
        if type(other) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = other

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, other):
        if type(other) != int or not(0 <= other <= 8):
            raise ValueError("недопустимое значение атрибута")
        self.__number = other

    def __bool__(self):
        return not(self.__is_open)

class GamePole:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    INDX = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    @property
    def pole(self):
        return self.__pole_cells
    @pole.setter
    def pole(self, other):
        self.__pole_cells = self.__pole_cells

    def __init__(self, N, M, total_mines):
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.m)] for _ in range(self.n)]


      
    def init_pole(self):
        count_bombs = 0
        while count_bombs < self.total_mines:
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.m - 1)
            if self.__pole_cells[i][j].is_mine:
                continue  
            self.__pole_cells[i][j].is_mine = True
            count_bombs += 1

        for i in range(self.n):
            for j in range(self.m):
                if self.__pole_cells[i][j].is_mine:
                    self.__pole_cells[i][j] = Cell(0, True)
                else:
                    count = 0
                    for k, m in self.INDX:
                        if 0 <= i+k < self.n and 0 <= j+m < self.m and self.__pole_cells[i+k][j+m].is_mine:
                            count += 1
                    self.__pole_cells[i][j] = Cell(count)

    def show_pole(self):
        for rows in self.__pole_cells:
            for cell in rows:
                if cell.is_open:
                    if cell.is_mine:
                        print('*', end=' ')
                    else:
                        print(cell.number, end=' ')
                else:
                    print('#', end=' ')
            print()

    def open_cell(self, i, j):
        if type(i) != int or type(j) != int:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        if i > self.n-1 or j > self.m-1:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True


