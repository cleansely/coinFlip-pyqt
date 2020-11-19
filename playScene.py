from PyQt5 import QtCore
from PyQt5.QtCore import qDebug, QTimer, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel

from data_config import DataConfig
from myCoin import MyCoin
from myPushButton import MyPushButton


class PlayScene(QMainWindow):
    _play_scene_back = QtCore.pyqtSignal()

    def __init__(self, index):
        super().__init__()
        self.index = index
        self.isWin = True
        self.init_ui()

    def init_ui(self):
        # 窗口大小
        self.setFixedSize(320, 588)
        # 图标及标题
        self.setWindowIcon(QIcon("res/Coin0001.png"))
        self.setWindowTitle("翻金币")
        # 菜单栏
        start_menu = self.menuBar().addMenu("开始")
        quit_action = start_menu.addAction("退出")
        quit_action.triggered.connect(self.close)
        # 返回按钮
        close_btn = MyPushButton("res/BackButton.png", "res/BackButtonSelected.png")
        close_btn.setParent(self)
        close_btn.move(self.width() - close_btn.width(), self.height() - close_btn.height())
        close_btn.clicked.connect(self.close_btn_event)
        # 当前关卡标题
        label = QLabel()
        label.setParent(self)
        font = QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        label.setFont(font)
        label.setText(f"Leavel: {self.index}")
        label.setGeometry(30, self.height() - 50, 120, 50)
        # 金币按钮
        data_array = DataConfig().array_map
        self.coin_btn = [[None for _ in range(4)]for _ in range(4)]
        for i in range(4):
            for j in range(4):
                label = QLabel()
                label.setParent(self)
                label.setPixmap(QPixmap("res/BoardNode.png"))
                label.setGeometry(0, 0, 50, 50)
                label.move(57 + i * 50, 200 + j * 50)

                self.game_array = data_array[self.index+1]
                if self.game_array[i][j]:
                    img = "res/Coin0001.png"
                else:
                    img = "res/Coin0008.png"
                coin = MyCoin(img)
                coin.setParent(self)
                coin.move(59 + i * 50, 204 + j * 50)
                coin.pos_x = i
                coin.pos_y = j
                coin.flag = self.game_array[i][j]
                self.coin_btn[i][j] = coin
                coin.clicked.connect(self.coin_click)
        # 胜利图片
        tmp_pix = QPixmap("res/LevelCompletedDialogBg.png")
        self.win_label = QLabel()
        self.win_label.setGeometry(0,0,tmp_pix.width(), tmp_pix.height())
        self.win_label.setPixmap(tmp_pix)
        self.win_label.setParent(self)
        self.win_label.move((self.width()-tmp_pix.width())*0.5,-tmp_pix.height())

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 背景图
        pix = QPixmap()
        ret = pix.load("res/PlayLevelSceneBg.png")
        if not ret:
            qDebug(f"选择关卡背景图加载失败")
        painter.drawPixmap(0, 0, self.width(), self.height(), pix)
        # 标题图
        ret = pix.load("res/Title.png")
        if not ret:
            qDebug(f"logo图加载失败")
        pix = pix.scaled(pix.width() * 0.5, pix.height() * 0.5)
        painter.drawPixmap(10, 30, pix.width(), pix.height(), pix)
        painter.end()

    def close_btn(self):
        self.hide()
        self._play_scene_back.emit()

    def close_btn_event(self):
        QTimer.singleShot(500, self.close_btn)

    def coin_click(self):
        self.sender().change_flag()
        self.game_array[self.sender().pos_x][self.sender().pos_y] = 0 if self.game_array[self.sender().pos_x][
            self.sender().pos_y] else 1
        coin = self.sender()
        QTimer.singleShot(300, lambda :self.other_coin_flip(coin.pos_x, coin.pos_y))

    def other_coin_flip(self, x, y):
        if x + 1 <= 3:
            self.coin_btn[x+1][y].change_flag()
            self.game_array[x+1][y] = 0 if self.game_array[x+1][y] else 1
        if x - 1 >=0:
            self.coin_btn[x-1][y].change_flag()
            self.game_array[x-1][y] = 0 if self.game_array[x-1][y] else 1
        if y+1 <= 3:
            self.coin_btn[x][y+1].change_flag()
            self.game_array[x][y+1] = 0 if self.game_array[x][y+1] else 1
        if y-1 >=0:
            self.coin_btn[x][y-1].change_flag()
            self.game_array[x][y-1] = 0 if self.game_array[x][y-1] else 1

        self.isWin = True
        for i in range(4):
            for j in range(4):
                if not self.coin_btn[i][j].flag:
                    self.isWin = False
                    break

        if self.isWin:
            for i in range(4):
                for j in range(4):
                    self.coin_btn[i][j].isWin = True
            animation = QPropertyAnimation(self.win_label, b"geometry", parent=self)
            animation.setDuration(1000)
            animation.setStartValue(QRect(self.win_label.x(), self.win_label.y(), self.win_label.width(), self.win_label.height()))
            animation.setEndValue(QRect(self.win_label.x(), self.win_label.y()+114, self.win_label.width(), self.win_label.height()))
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation.start()
