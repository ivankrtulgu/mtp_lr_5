import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView

class MovieTable(QWidget):
    def __init__(self):
        super().__init__()
        self.initInterface()
        self.load_data()

    def initInterface(self):
        self.setGeometry(150, 150, 600, 300)
        self.setWindowTitle("Фильмы")

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(0)

        self.table.setHorizontalHeaderLabels(["Название", "Год", "Режиссёр"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout.addWidget(self.table)
        self.setLayout(layout)

    def load_data(self):
        movies = [
            ["Челюсти", "1975", "Стивен Спилберг"],
            ["Звёздные войны. Эпизод 3: Месть ситхов", "2005", "Джордж Лукас"],
            ["Властелин колец: Братство кольца", "2001", "Питер Джексон"],
            ["Джанго освобождённый", "2012", "Квентин Тарантино"]
        ]

        self.table.setRowCount(len(movies))

        for row, movie in enumerate(movies):
            for col, value in enumerate(movie):
                item = QTableWidgetItem(value)
                self.table.setItem(row, col, item)

app = QApplication(sys.argv)
window = MovieTable()
window.show()
sys.exit(app.exec_())
