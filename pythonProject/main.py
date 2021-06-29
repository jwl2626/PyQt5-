import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QAbstractItemView, QMessageBox, QDataWidgetMapper)
from maininterf import QmyMainWidow

if __name__ == "__main__":  # 用于当前窗体测试
    app = QApplication(sys.argv)  # 创建GUI应用程序
    form = QmyMainWidow()  # 创建窗体
    form.show()
    sys.exit(app.exec_())
