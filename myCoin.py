from PyQt5.QtCore import qDebug, QTimer
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPushButton


class MyCoin(QPushButton):
    def __init__(self, but_img):
        super().__init__()
        self.pos_x = None
        self.pos_y = None
        self.flag = True
        self.min = 1
        self.max = 8
        self.isAnimation = False
        self.isWin = False

        pixmap = QPixmap()
        ret = pixmap.load(but_img)
        if not ret:
            qDebug(f"{but_img}加载失败")

        self.setFixedSize(pixmap.width(), pixmap.height())
        self.setStyleSheet("QPushButton{border:0px;}")
        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size())

        # 监听正面翻转的信号槽
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.timer1_slot)
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.timer2_slot)

    def change_flag(self):
        if self.flag:
            self.timer1.start(30)
            self.isAnimation = True
            self.flag = 0
        else:
            self.timer2.start(30)
            self.isAnimation = True
            self.flag = 1


    def timer1_slot(self):
        pixmap = QPixmap()
        img = f"res/Coin000{str(self.min)}.png"
        self.min += 1
        ret = pixmap.load(img)
        if not ret:
            qDebug("图像加载失败")
        self.setFixedSize(pixmap.width(), pixmap.height())
        self.setStyleSheet("QPushButton{border:0px;}")
        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size())
        if self.min > self.max:
            self.min = 1
            self.isAnimation = False
            self.timer1.stop()


    def timer2_slot(self):
        pixmap = QPixmap()
        img = f"res/Coin000{str(self.max)}.png"
        self.max -= 1
        pixmap.load(img)
        self.setFixedSize(pixmap.width(), pixmap.height())
        self.setStyleSheet("QPushButton{border:0px;}")
        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size())
        if self.min > self.max:
            self.max = 8
            self.isAnimation = False
            self.timer2.stop()

    def mousePressEvent(self, e):
        if self.isAnimation or self.isWin:
            return
        else:
            return super(MyCoin, self).mousePressEvent(e)