import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Classes.Item import Item
from Classes.Player import Player

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 800)

        self.player = Player()

        butn = Item(self)
        butn.Setting(self.player, "languages")

        self.update()
 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

