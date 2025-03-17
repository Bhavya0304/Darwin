from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
import sys
from PyQt5.QtCore import QSize


class ChatbotIcon(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup (hidden by default)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("Darwin Chatbot")
        self.setGeometry(1000, 600, 300, 400)  # Bottom-right positioning
        self.setStyleSheet("background-color: rgba(0, 0, 0, 180); border-radius: 15px;")

        # Chat label
        self.label = QLabel("Chatbot Window", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 200, 50)
        self.label.setStyleSheet("color: white; font-size: 18px;")

        # Close button
        self.close_button = QPushButton("Close", self)
        self.close_button.setGeometry(100, 300, 100, 40)
        self.close_button.setStyleSheet("background-color: red; color: white; border-radius: 10px;")
        self.close_button.clicked.connect(self.hide)


class ChatbotButton(QWidget):
    def __init__(self):
        super().__init__()

        # Get screen size to position the chatbot button at the bottom-right
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen.width() - 80, screen.height() - 80, 300, 300)

        self.setFixedSize(300, 300)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Main chatbot button
        self.chatbot_btn = QPushButton(self)
        self.chatbot_btn.setGeometry(0, 0, 60, 60)
        self.chatbot_btn.setIcon(QIcon("./darwin-sm.png"))  # Set Darwin Icon
        self.chatbot_btn.setIconSize(QSize(50, 50))
        self.chatbot_btn.setStyleSheet("border-radius: 30px; background-color: #444;")
        self.chatbot_btn.clicked.connect(self.toggle_menu)

        # Image button (Hidden initially)
        self.image_btn = QPushButton(self)
        self.image_btn.setGeometry(0, 0, 50, 50)
        self.image_btn.setIcon(QIcon("./darwin-sm.png"))  # Replace with an actual image icon
        self.image_btn.setIconSize(QSize(40, 40))
        self.image_btn.setStyleSheet("border-radius: 25px; background-color: #888;")
        self.image_btn.hide()
        self.image_btn.clicked.connect(lambda: print("Image Clicked"))

        # Chat button (Hidden initially)
        self.chat_btn = QPushButton(self)
        self.chat_btn.setGeometry(0, 0, 50, 50)
        self.chat_btn.setIcon(QIcon("./darwin-sm.png"))  # Replace with an actual chat icon
        self.chat_btn.setIconSize(QSize(40, 40))
        self.chat_btn.setStyleSheet("border-radius: 25px; background-color: #888;")
        self.chat_btn.hide()
        self.chat_btn.clicked.connect(self.show_chat)

        # Chat window instance
        self.chat_window = ChatbotIcon()

        # Animation objects
        self.image_animation = QPropertyAnimation(self.image_btn, b"pos")
        self.chat_animation = QPropertyAnimation(self.chat_btn, b"pos")

        # Set initial position
        self.is_expanded = False

    def toggle_menu(self):
        if self.is_expanded:
            self.hide_buttons()
        else:
            self.show_buttons()
        self.is_expanded = not self.is_expanded

    def show_buttons(self):
        self.image_btn.show()
        self.chat_btn.show()

        # Animate buttons expanding outward
        self.image_animation.setDuration(300)
        self.image_animation.setStartValue(QPoint(0, 0))
        self.image_animation.setEndValue(QPoint(-60, -10))  # Move left
        self.image_animation.setEasingCurve(QEasingCurve.OutQuad)
        self.image_animation.start()

        self.chat_animation.setDuration(300)
        self.chat_animation.setStartValue(QPoint(0, 0))
        self.chat_animation.setEndValue(QPoint(0, -60))  # Move up
        self.chat_animation.setEasingCurve(QEasingCurve.OutQuad)
        self.chat_animation.start()

    def hide_buttons(self):
        # Animate buttons collapsing
        self.image_animation.setDuration(300)
        self.image_animation.setStartValue(QPoint(-60, -10))
        self.image_animation.setEndValue(QPoint(0, 0))
        self.image_animation.setEasingCurve(QEasingCurve.InQuad)
        self.image_animation.start()

        self.chat_animation.setDuration(300)
        self.chat_animation.setStartValue(QPoint(0, -60))
        self.chat_animation.setEndValue(QPoint(0, 0))
        self.chat_animation.setEasingCurve(QEasingCurve.InQuad)
        self.chat_animation.start()

        # Hide buttons after animation
        self.image_animation.finished.connect(self.image_btn.hide)
        self.chat_animation.finished.connect(self.chat_btn.hide)

    def show_chat(self):
        self.chat_window.move(self.x() - 240, self.y() - 320)  # Position above chatbot button
        self.chat_window.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)

    chatbot_button = ChatbotButton()
    chatbot_button.show()

    sys.exit(App.exec_())
