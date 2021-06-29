## 单继承方法，能更好的进行界面与逻辑的分离
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import (QApplication, QMainWindow,QActionGroup,
                 QLabel, QProgressBar, QSpinBox, QFontComboBox)
from mainGui import Ui_mainGUI
class QmyMainWidow(QMainWindow):
    def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui = Ui_mainGUI()        #创建UI对象
      self.ui.setupUi(self)      #构造UI界面



    #把excle的数据导入数据库并且刷新
    #def daorushuju(self):



if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWidow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())