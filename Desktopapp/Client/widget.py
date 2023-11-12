import sys
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtCore import Signal, Qt
from ui_form import Ui_Widget
from ui_dialog import Ui_Dialog
sys.path.append('C:\\Users\\Ricky\\Documents\\Local Programs\\Spout-1\\API')
from WeatherChecker import WeatherChecker
from sprinkler import post_handler, main
import requests
<<<<<<< Updated upstream
=======

index = int(0)
>>>>>>> Stashed changes

class CustomDialog(QDialog, Ui_Dialog):
    dataEntered = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.handle_ok_button)

    def handle_ok_button(self):
        data1 = self.lineEdit.text()
        data2 = self.lineEdit_2.text()

        if data1 and data2:
            self.dataEntered.emit(data1, data2)
            self.accept()

    def reset_dialog(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()

class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.newWindow.clicked.connect(self.show_popup)
        self.previousButton.clicked.connect(self.show_previous_page)
        self.nextButton.clicked.connect(self.show_next_page)

        self.dialog = CustomDialog()
        self.dialog.dataEntered.connect(self.handle_dialog_data)

        self.index = 0
        self.currentIndex = 0

    def show_popup(self):
        self.dialog.reset_dialog()
        self.dialog.exec()

    def handle_dialog_data(self, data1, data2):
        data = {'function': 'add', 'id': self.index, 'name': str(data1), 'period': '0', 'seed_type': 3}
        r1 = requests.post('http://172.23.112.1:12000', data)
        r2 = r1.content.decode('utf-8')
        print(r2)

<<<<<<< Updated upstream
        msg_box = QMessageBox()
        msg_box.setWindowTitle('Spout')
        msg_box.setText(r2)
        msg_box.exec()

        recommendation = "NULL"
=======
        data = {'function': 'add', 'id': index, 'name': str(data1), 'period': '0', 'seed_type': data2}

        r1 = requests.post('http://172.18.144.1:12000', data)

        print(r1.content.decode('utf-8'))

        reccomendation = "NULL"
>>>>>>> Stashed changes

        if WeatherChecker('ea2af1037f4540a4844235921231111') == True:
            recommendation = "Rest easy, it will rain soon"
        else:
            recommendation = "Your plants will appreciate being watered as usual"

        new_page = QWidget(self.stackedWidget)
        layout = QVBoxLayout(new_page)
        label1 = QLabel(f"Spout Connected: {data1}", new_page, alignment=Qt.AlignmentFlag.AlignTop)
        label2 = QLabel(f"Seed type: {data2}", new_page)
        label3 = QLabel("Status: Active", new_page)
        label4 = QLabel(f"{recommendation}", new_page, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        self.stackedWidget.addWidget(new_page)
        self.index += 1
        self.currentIndex += 1
        self.stackedWidget.setCurrentWidget(new_page)

    def show_previous_page(self):
        current_index = self.stackedWidget.currentIndex()
        total_pages = self.stackedWidget.count()

        if total_pages > 0:
            new_index = (current_index - 1) % total_pages
            self.stackedWidget.setCurrentIndex(new_index)

    def show_next_page(self):
        current_index = self.stackedWidget.currentIndex()
        total_pages = self.stackedWidget.count()

        if total_pages > 0:
            new_index = (current_index + 1) % total_pages
            self.stackedWidget.setCurrentIndex(new_index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
