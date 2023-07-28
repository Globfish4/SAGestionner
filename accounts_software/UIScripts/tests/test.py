import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QScrollArea, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollArea avec barre de défilement")
        self.setGeometry(100, 100, 400, 300)

        # Création du widget principal et du layout vertical
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Création du QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Création du widget contenant les QLabel
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        # Layout vertical pour le contenu
        content_layout = QVBoxLayout(content_widget)

        # Ajout des QLabel avec un texte quelconque
        for i in range(30):
            label = QLabel(f"Texte {i+1}")
            content_layout.addWidget(label)

        # Ajout du QScrollArea au layout principal
        layout.addWidget(scroll_area)

        # Définition du widget principal comme widget central de la fenêtre
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
