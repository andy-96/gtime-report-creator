from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QWidget, QPushButton, QLineEdit, QHBoxLayout
from bot import GTimeReportBot


class Window(QDialog):
  def __init__(self, parent=None):
    super(Window, self).__init__(parent)
    
    layout = QHBoxLayout()

    self.year = QLineEdit()
    self.week = QLineEdit()
    self.pb = QPushButton('Check')

    layout.addWidget(QLabel('Jahr'))
    layout.addWidget(self.year)
    layout.addWidget(QLabel('KW'))
    layout.addWidget(self.week)
    layout.addWidget(self.pb)
    self.setLayout(layout)
    self.pb.clicked.connect(self.button_click)
    self.setWindowTitle("Report")
  
  def button_click(self):
    year = self.year.text()
    week = self.week.text()
    GTimeReportBot().autoBot(year, week)
    return True

app = QApplication([])
window = Window()
window.show()
app.exec_()