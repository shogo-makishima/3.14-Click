from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFontDatabase
from .Notebooks import NotesList
from .Soft import ProgrammsList
from .Languages import LanguagesList


class Item(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__(Form)
        self.backgound = QtWidgets.QFrame(Form)
        self.backgound.setGeometry(QtCore.QRect(0, 100, 500, 150))
        self.backgound.setObjectName("backgound")
        self.backgound.setStyleSheet("#backgound {background-image: url(Images/button.jpg);}")

        self.image = QtWidgets.QLabel(self.backgound)
        self.image.setGeometry(QtCore.QRect(0, 0, 75, 75))
        self.image.move(25, 35)
        self.image.raise_()
        self.image.setText("")
        self.image.setObjectName("image")

        self.damage = QtWidgets.QLabel(self.backgound)
        self.damage.setGeometry(QtCore.QRect(326, 22, 97, 50))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(20)
        self.damage.setFont(font)
        self.damage.setStyleSheet("color: rgb(255, 255, 255);")
        self.damage.setAlignment(QtCore.Qt.AlignCenter)
        self.damage.setObjectName("label")

        self.level = QtWidgets.QLabel(self.backgound)
        self.level.setGeometry(QtCore.QRect(427, 22, 50, 50))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(30)
        self.level.setFont(font)
        self.level.setStyleSheet("color: rgb(255, 255, 255);")
        self.level.setAlignment(QtCore.Qt.AlignCenter)
        self.level.setObjectName("label_2")

        self.name = QtWidgets.QLabel(self.backgound)
        self.name.setGeometry(QtCore.QRect(104, 22, 194, 50))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(20)
        self.name.setFont(font)
        self.name.setStyleSheet("color: rgb(255, 255, 255);")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("label_3")

        self.price = QtWidgets.QLabel(self.backgound)
        self.price.setGeometry(QtCore.QRect(124, 96, 178, 30))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(15)
        self.price.setFont(font)
        self.price.setStyleSheet("color: rgb(255, 255, 255);")
        self.price.setAlignment(QtCore.Qt.AlignCenter)
        self.price.setObjectName("label_4")
        
        self.shop = QtWidgets.QPushButton(self.backgound)
        self.shop.setGeometry(QtCore.QRect(322, 96, 158, 30))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(25)
        self.shop.setFont(font)
        self.shop.setStyleSheet("color: rgb(0, 0, 0);")
        self.shop.setObjectName("pushButton")

        self.image.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.damage.setText(_translate("Form", "Damage"))
        self.level.setText(_translate("Form", "Level"))
        self.name.setText(_translate("Form", "Name"))
        self.price.setText(_translate("Form", "Price"))
        self.shop.setText(_translate("Form", "Shop"))

    def settingText(self, player, getType):
        if getType == "languages":
            lang = self.GetLanguage(player)

            if (player.stats["languages"][1] + 1 < len(LanguagesList.dictionaryLanguages[player.stats["languages"][0]].levelsKnow.keys())):
                self.name.setText(lang.name) # Имя
                self.price.setText(str(lang.levelsKnow[player.stats["languages"][1] + 1]["price"])) # Цена
                self.level.setText(f'{str(player.stats["languages"][1] + 1)}') # Уровень
                self.damage.setText(str(lang.levelsKnow[player.stats["languages"][1] + 1]["damage"])) # Урон
            elif (player.stats["languages"][1] + 1 == len(LanguagesList.dictionaryLanguages[player.stats["languages"][0]].levelsKnow.keys())):
                if (LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
                    lang = LanguagesList.dictionaryLanguages[LanguagesList.listLanguages[LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1]]
                    self.name.setText(lang.name) # Имя
                    self.price.setText(str(lang.levelsKnow[0]["price"])) # Цена
                    self.level.setText(str(0)) # Уровень
                    self.damage.setText(str(lang.levelsKnow[0]["damage"])) # Урон
                else:
                    self.name.setText(LanguagesList.listLanguages[-1]) # Имя
                    self.price.setText("M") # Цена
                    self.level.setText("M") # Уровень
                    self.damage.setText(str(lang.levelsKnow[player.stats["languages"][1]]["damage"])) # Урон
            else:
                self.name.setText(lang.name) # Имя
                self.price.setText(str(lang.levelsKnow[player.stats["languages"][1] + 1]["price"])) # Цена
                self.level.setText(str(0)) # Уровень
                self.damage.setText(str(lang.levelsKnow[player.stats["languages"][1]]["damage"])) # Урон
            self.image.setPixmap(QPixmap(LanguagesList.pictures_dict[lang.name]).scaled(75, 75))
        elif getType == "notes":
            note = self.GetNote(player)

            if (note.name != NotesList.listNotes[-1]):
                self.name.setText(note.name) # Имя
                self.price.setText(str(note.price)) # Цена
                self.level.setText('M') # Уровень
                self.damage.setText(str(note.damage)) # Урон
            else:
                self.name.setText(note.name) # Имя
                self.price.setText('M') # Цена
                self.level.setText('M') # Уровень
                self.damage.setText(str(note.damage)) # Урон
            self.image.setPixmap(QPixmap(NotesList.dictNotes[note.name]).scaled(75, 75))
        elif getType == "soft":
            soft = self.GetSoft(player)

            if (soft.name != player.stats["soft"]):
                self.name.setText(soft.name) # Имя
                self.price.setText(str(soft.price)) # Цена
                self.level.setText('M') # Уровень
                self.damage.setText(str(soft.damage)) # Урон
            else:
                self.name.setText(soft.name) # Имя
                self.price.setText('M') # Цена
                self.level.setText('M') # Уровень
                self.damage.setText(str(soft.damage)) # Урон

    def Setting(self, player, getType, func, money):
        try: self.shop.clicked.disconnect() 
        except Exception: pass
        self.UpdateImage(player, getType)
        self.shop.clicked.connect(lambda: self.UpdateSomeThing(player, getType, func, money))
        self.settingText(player, getType)

    def UpdateSomeThing(self, player, getType, func, money):
        if (getType == "languages"):
            player.UpdateLevelLanguage()
            self.image.setPixmap(QPixmap(LanguagesList.pictures_dict[self.GetLanguage(player).name]).scaled(75, 75))
        elif (getType == "notes"):
            player.BuyNewNotebook()
            self.image.setPixmap(QPixmap(NotesList.dictNotes[self.GetNote(player).name]).scaled(75, 75))
        elif (getType == "soft"):
            player.BuySoft()
        money.setText(str(player.stats["money"]))
        func(player)
        
        self.settingText(player, getType)
        
    def UpdateImage(self, player, getType):
        self.image.setPixmap(QPixmap())
        if (getType == "languages"):
            self.image.setPixmap(QPixmap(LanguagesList.pictures_dict[self.GetLanguage(player).name]).scaled(75, 75))
        elif (getType == "notes"):
            self.image.setPixmap(QPixmap(NotesList.dictNotes[self.GetNote(player).name]).scaled(75, 75))

    def GetLanguage(self, player):
        if (player.stats["languages"][1] + 1 <= len(LanguagesList.dictionaryLanguages[player.stats["languages"][0]].levelsKnow.keys())):
            return LanguagesList.dictionaryLanguages[player.stats["languages"][0]]
        if (LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
            if (LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1 < len(LanguagesList.listLanguages)):
                return LanguagesList.dictionaryLanguages[LanguagesList.listLanguages[LanguagesList.listLanguages.index(player.stats["languages"][0]) + 1]]
    
    def GetNote(self, player):
        num = NotesList.listNotes.index(player.stats["notebook"])

        if (num + 1 < len(NotesList.listNotes)):
            return NotesList.dictionaryNotes[NotesList.listNotes[num + 1]]
        else:
            return NotesList.dictionaryNotes[NotesList.listNotes[num]]
    
    def GetSoft(self, player):
        num = ProgrammsList.listSoft.index(player.stats["soft"])

        if (num + 1 < len(ProgrammsList.listSoft)):
            return ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num + 1]]
        else:
            return ProgrammsList.dictionarySoft[ProgrammsList.listSoft[num]]
