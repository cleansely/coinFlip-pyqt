from PyQt5 import QtCore
from PyQt5.QtCore import qDebug, QTimer
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel

from myPushButton import MyPushButton
from playScene import PlayScene


class ChooseLevelScene(QMainWindow):
    _choose_scene_back = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 窗口大小
        self.setFixedSize(320, 588)
        # 图标及标题
        self.setWindowIcon(QIcon("res/Coin0001.png"))
        self.setWindowTitle("选择关卡")
        # 菜单栏
        start_menu = self.menuBar().addMenu("开始")
        quit_action = start_menu.addAction("退出")
        quit_action.triggered.connect(self.close)
        # 返回按钮
        close_btn = MyPushButton("res/BackButton.png", "res/BackButtonSelected.png")
        close_btn.setParent(self)
        close_btn.move(self.width() - close_btn.width(), self.height() - close_btn.height())
        close_btn.clicked.connect(self.close_btn)
        # 关卡选择按钮
        for i in range(20):
            menu_btn = MyPushButton("res/LevelIcon.png")
            menu_btn.setParent(self)
            menu_btn.move(25 + (i % 4) * 70, 130 + (i // 4) * 70)
            menu_btn.index = i
            menu_btn.clicked.connect(self.choose_btn)

            # 显示按钮上的文字
            label = QLabel()
            label.setParent(self)
            label.setFixedSize(menu_btn.width(), menu_btn.height())
            label.setText(str(i + 1))
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.move(25 + (i % 4) * 70, 130 + (i // 4) * 70)
            label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 背景图
        pix = QPixmap()
        ret = pix.load("res/OtherSceneBg.png")
        if not ret:
            qDebug(f"选择关卡背景图加载失败")
        painter.drawPixmap(0, 0, self.width(), self.height(), pix)
        # 标题图
        ret = pix.load("res/Title.png")
        if not ret:
            qDebug(f"logo图加载失败")
        painter.drawPixmap((self.width() - pix.width()) * 0.5, 30, pix.width(), pix.height(), pix)
        painter.end()

    def close_btn(self):
        self.hide()
        self._choose_scene_back.emit()

    def close_btn_event(self):
        QTimer.singleShot(500, self.close_btn)

    def choose_btn(self):
        self.hide()
        self.p_cene = PlayScene(self.sender().index+1)
        self.p_cene.setGeometry(self.geometry())
        self.p_cene.show()
        # 监听选择关卡的返回信号
        self.p_cene._play_scene_back.connect(self.show)

    # def show(self) -> None:
    #     self.setGeometry(self.p_cene().geometry())
    #     super(ChooseLevelScene, self).show()