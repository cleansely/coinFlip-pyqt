from PyQt5.QtCore import qDebug, QTimer
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow

from chooseLevelScene import ChooseLevelScene
from myPushButton import MyPushButton


class MainScene(QMainWindow):
    def __init__(self):
        super().__init__()
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
        # 开始按钮
        start_btn = MyPushButton("res/MenuSceneStartButton.png")
        start_btn.setParent(self)
        start_btn.move(int((self.width() - start_btn.width()) * 0.5), int(self.height() * 0.7))
        # 监听开始按钮点击事件,动画及切换页面
        start_btn.clicked[bool].connect(lambda: self.btn_zoom(start_btn))
        # 选择关卡
        self.choose_scene = ChooseLevelScene()
        # 监听选择关卡的返回信号
        self.choose_scene._choose_scene_back.connect(self.show)
        # 显示
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # 背景图
        pix = QPixmap()
        ret = pix.load("res/PlayLevelSceneBg.png")
        if not ret:
            qDebug(f"背景图加载失败")
        painter.drawPixmap(0, 0, self.width(), self.height(), pix)
        # 标题图
        ret = pix.load("res/Title.png")
        if not ret:
            qDebug(f"logo图加载失败")
        pix = pix.scaled(pix.width() * 0.5, pix.height() * 0.5)
        painter.drawPixmap(10, 30, pix.width(), pix.height(), pix)
        painter.end()

    def btn_zoom(self, btn):
        # 点击动画
        btn.zoom1()
        btn.zoom2()
        # 进入选择关卡界面
        QTimer.singleShot(500, self.choose_scene_show)

    def choose_scene_show(self):
        self.hide()
        self.choose_scene.setGeometry(self.geometry())
        self.choose_scene.show()

    def show(self) -> None:
        self.setGeometry(self.choose_scene.geometry())
        super(MainScene, self).show()
