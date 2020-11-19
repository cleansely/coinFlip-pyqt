from PyQt5.QtCore import qDebug, QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPushButton


class MyPushButton(QPushButton):
    def __init__(self, normal_img: str, press_img: str = ""):
        """自定义按钮

        :param normal_img: 默认加载图标
        :param press_img: 点击后图标
        """
        super(MyPushButton, self).__init__()
        self.normal_img = normal_img
        self.press_img = press_img

        # 允许点击
        self.setCheckable(True)

        # 设置按钮图标及样式
        pixmap = QPixmap()
        ret = pixmap.load(self.normal_img)
        if not ret:
            qDebug(f"{normal_img}加载图片失败!")
        self.setFixedSize(pixmap.size())
        self.setStyleSheet("QPushButton{border:0px;}")
        self.setIcon(QIcon(pixmap))
        self.setIconSize(pixmap.size())

    def zoom(self):
        self.zoom1()
        self.zoom2()

    def zoom1(self):
        animation = QPropertyAnimation(self, b"geometry", parent=self.parent())
        animation.setDuration(200)
        animation.setStartValue(QRect(self.x(), self.y(), self.width(), self.height()))
        animation.setEndValue(QRect(self.x(), self.y() + 10, self.width(), self.height()))
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start()

    def zoom2(self):
        animation = QPropertyAnimation(self, b"geometry", parent=self.parent())
        animation.setDuration(200)
        animation.setStartValue(QRect(self.x(), self.y() + 10, self.width(), self.height()))
        animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start()

    def mousePressEvent(self, e):
        """重写鼠标点击事件"""
        self.set_Icon(self.press_img)
        return super(MyPushButton, self).mousePressEvent(e)

    def mouseReleaseEvent(self, et):
        """重写鼠标释放事件"""
        self.set_Icon(self.normal_img)
        return super(MyPushButton, self).mouseReleaseEvent(et)

    def set_Icon(self, img):
        if img != "":
            pixmap = QPixmap()
            ret = pixmap.load(img)
            if not ret:
                qDebug(f"{img}加载图片失败")

            self.setFixedSize(pixmap.size())
            self.setStyleSheet("QPushButton{border:0px;}")
            self.setIcon(QIcon(pixmap))
            self.setIconSize(pixmap.size())
