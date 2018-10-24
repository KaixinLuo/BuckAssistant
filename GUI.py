import sys
from facerecogonition import *
from conversation_processor import *
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QTextEdit,QGridLayout,QHBoxLayout
from PyQt5.QtCore import Qt

class Application(QWidget):
    def __init__(self):
        super().__init__()

        face = read_face()
        self.user = face_recognizer(face)
        self.conversationHandler = Conversation_Processor()
        self.initUI()
    def initUI(self):
        self.sendButton = QPushButton("Send")
        self.voiceButton = QPushButton("Voice")
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.voiceButton)
        buttonLayout.addWidget(self.sendButton)
        self.textToSend = QTextEdit()
        self.msgArea = QTextEdit()
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.msgArea,0,0)
        self.grid.addWidget(self.textToSend,1,0,6,1)
        self.grid.addLayout(buttonLayout,7,0)

        self.msgArea.setReadOnly(True)
        self.sendButton.clicked.connect(self.send_button_pressed)
        

        self.setLayout(self.grid)
        self.setGeometry(300, 300, 1000, 618)
        self.setWindowTitle('Buttons') 
        self.show()

    def send_button_pressed(self):
        raw_text = self.textToSend.toPlainText()
        if raw_text != "":
            self.msgArea.insertPlainText(self.user+":\n    "+self.textToSend.toPlainText()+"\n")
            reply = self.conversationHandler.process_message(raw_text)
            self.msgArea.insertPlainText("Advisor:\n    "+reply+"\n")

        self.textToSend.clear()
    def voice_button_pressed(self):
        pass
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
