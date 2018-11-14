import sys

from conversation_processor import *
from modules.components.user import User
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QTextEdit,QGridLayout,QHBoxLayout
from PyQt5.QtGui import QTextCursor,QFont
import facerecogonition as fr


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.isFristMsg = True
        
        self.conversationHandler = Conversation_Processor()
        self.launch()
        self.login()
        self.initUI()
    def initUI(self):
        self.sendButton = QPushButton("Send")
        #self.sendButton.setFont(QFont("Roman times",20,QFont.Bold))
        self.voiceButton = QPushButton("Voice")
        #self.voiceButton.setFont(QFont("Roman times",20,QFont.Bold))
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.voiceButton)
        buttonLayout.addWidget(self.sendButton)
        self.textToSend = QTextEdit()
        self.textToSend .setFont(QFont("Roman times",20,QFont.Bold))
        #self.textToSend.setStyleSheet("color:red")
        self.msgArea = QTextEdit("Welcome! "+self.user+", this is virtual advisor!")
        #self.msgArea.setStyleSheet("color:red")
        self.msgArea .setFont(QFont("Roman times",20,QFont.Bold))
        self.grid = QGridLayout()
        self.grid.setSpacing(1)

        self.grid.addWidget(self.msgArea,0,0)
        self.grid.addWidget(self.textToSend,1,0,6,1)
        self.grid.addLayout(buttonLayout,7,0)

        self.msgArea.setReadOnly(True)
        self.sendButton.clicked.connect(self.send_button_pressed)
        #self.sendButton.keyPressEvent(self.send_button_pressed)
        self.voiceButton.clicked.connect(self.voice_button_pressed)
        
        self.setLayout(self.grid)
        self.setGeometry(300, 300,  618,1000)
        self.setWindowTitle('Vritual Advisor') 
        
        self.show()
    def launch(self):
        pass
    def send_button_pressed(self):
        if self.isFristMsg:
            self.msgArea.clear()
            self.isFristMsg = False
        
        raw_text = self.textToSend.toPlainText().rstrip('\n')
        if raw_text != "":
            self.msgArea.insertPlainText(self.user+":\n    "+self.textToSend.toPlainText()+"\n")
            reply = self.conversationHandler.process_message(raw_text)
            self.msgArea.insertPlainText("Advisor:\n    "+reply+"\n")
        self.msgArea.moveCursor(QTextCursor.End)

        self.textToSend.clear()
    def voice_button_pressed(self):
        pass
    def enter_button_pressed(self):
        pass
    def login(self):
        face = fr.read_face()
        self.user = fr.face_recognizer(face)
        
        u=User()
        f = open("email.txt", "r")
        f1 = f.read().splitlines()
        u.set_email_address(f1[0])
        u.set_email_password(f1[1])
        u.set_name(self.user)
        self.conversationHandler.assign_user_object(u)

    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
