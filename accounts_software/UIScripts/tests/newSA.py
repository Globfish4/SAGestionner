import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Données de la courbe
    temps = [0, 1, 2, 3, 4, 5]
    valeurs = [0, 20, 30, 15, 10, 25]

    # Création de la scène
    scene = QGraphicsScene()

    # Création de la figure Matplotlib
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot(temps, valeurs, color='red')

    # Création du canevas de la figure Matplotlib
    canvas = FigureCanvas(fig)
    canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Ajout du canevas à la scène
    scene.addWidget(canvas)

    # Création de la vue
    view = QGraphicsView(scene)
    view.setWindowTitle("Courbe dans QGraphicsScene")
    view.show()

    sys.exit(app.exec_())
