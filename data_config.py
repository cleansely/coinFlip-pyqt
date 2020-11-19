from PyQt5.QtCore import QObject


class DataConfig(QObject):
    def __init__(self):
        super(DataConfig, self).__init__()
        self.array_map = {}
        self.init_data()

    def init_data(self):
        vecotr = [[1, 1, 1, 1],
                  [1, 1, 0, 1],
                  [1, 0, 0, 0],
                  [1, 1, 0, 1]]
        self.array_map[1] = vecotr
        vecotr = [[1, 0, 1, 1],
                  [0, 0, 1, 1],
                  [1, 1, 0, 0],
                  [1, 1, 0, 1]]
        self.array_map[2] = vecotr
        vecotr = [[0, 0, 0, 0],
                  [0, 1, 1, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0]]
        self.array_map[3] = vecotr
        vecotr = [[0, 1, 1, 1],
                  [1, 0, 0, 1],
                  [1, 0, 1, 1],
                  [1, 1, 1, 1]]
        self.array_map[4] = vecotr
        vecotr = [[1, 0, 0, 1],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [1, 0, 0, 1]]
        self.array_map[5] = vecotr
        vecotr = [[1, 0, 0, 1],
                  [0, 1, 1, 0],
                  [0, 1, 1, 0],
                  [1, 0, 0, 1]]
        self.array_map[6] = vecotr
        vecotr = [[0, 1, 1, 1],
                  [1, 0, 1, 1],
                  [1, 1, 0, 1],
                  [1, 1, 1, 0]]
        self.array_map[7] = vecotr
        vecotr = [[0, 1, 0, 1],
                  [1, 0, 0, 0],
                  [0, 0, 0, 1],
                  [1, 0, 1, 0]]
        self.array_map[8] = vecotr
        vecotr = [[1, 0, 1, 0],
                  [1, 0, 1, 0],
                  [0, 0, 1, 0],
                  [1, 0, 0, 1]]
        self.array_map[9] = vecotr
        vecotr = [[1, 0, 1, 1],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1],
                  [1, 1, 0, 1]]
        self.array_map[10] = vecotr
        vecotr = [[0, 1, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 0, 1],
                  [0, 1, 1, 0]]
        self.array_map[11] = vecotr
        vecotr = [[0, 1, 1, 0],
                  [0, 0, 0, 0],
                  [1, 1, 1, 1],
                  [0, 0, 0, 0]]
        self.array_map[12] = vecotr
        vecotr = [[0, 1, 1, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 1, 1, 0]]
        self.array_map[13] = vecotr
        vecotr = [[1, 0, 1, 1],
                  [0, 1, 0, 1],
                  [1, 0, 1, 0],
                  [1, 1, 0, 1]]
        self.array_map[14] = vecotr
        vecotr = [[0, 1, 0, 1],
                  [1, 0, 0, 0],
                  [1, 0, 0, 0],
                  [0, 1, 0, 1]]
        self.array_map[15] = vecotr
        vecotr = [[0, 1, 1, 0],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1],
                  [0, 1, 1, 0]]
        self.array_map[16] = vecotr
        vecotr = [[0, 1, 1, 1],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [1, 1, 1, 0]]
        self.array_map[17] = vecotr
        vecotr = [[0, 0, 0, 1],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0],
                  [1, 0, 0, 0]]
        self.array_map[18] = vecotr
        vecotr = [[0, 1, 0, 0],
                  [0, 1, 1, 0],
                  [0, 0, 1, 1],
                  [0, 0, 0, 0]]
        self.array_map[19] = vecotr
        vecotr = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        self.array_map[20] = vecotr
