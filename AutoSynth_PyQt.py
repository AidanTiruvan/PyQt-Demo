# Import modules
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtGui import QPixmap
import pyqtgraph as pg
from PyQt5 import QtWidgets

# Main Window
class AutoSynth(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AutoSynth')
        self.setGeometry(100, 100, 800, 500)

        # Main layout
        main_layout = QVBoxLayout()

        # Non-functioning buttons and user controls
        self.add_reagent_button = QPushButton('Add Reagents', self)
        self.run_reaction_button = QPushButton('Run Reaction', self)
        self.run_graph_button = QPushButton('Display Graph', self)
        main_layout.addWidget(self.add_reagent_button)
        main_layout.addWidget(self.run_reaction_button)
        main_layout.addWidget(self.run_graph_button)

        # Progress bar for reactors/experiment 
        self.reactor1_progress = QProgressBar(self)
        self.reactor1_progress.setValue(50)  # Progress values of the experiment 
        main_layout.addWidget(self.reactor1_progress)

        # Experiment materials used and user log
        self.workup_label = QLabel("Process name: ", self)
        self.solvent_label = QLabel("Solvents used: ", self)
        self.extraction_label = QLabel("Extraction solvent:", self)
        
        main_layout.addWidget(self.workup_label)
        main_layout.addWidget(self.solvent_label)
        main_layout.addWidget(self.extraction_label)

        # Added graph functionality although it isn't connected to button use yet
        self.plot_graph = pg.PlotWidget()
        main_layout.addWidget(self.plot_graph)
        self.plot_graph.setBackground("black")
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [14, 18, 22, 29, 20, 15, 30, 31, 32, 33]
        self.plot_graph.plot(time, temperature)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

# Show main app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    chem_app = AutoSynth()
    chem_app.show()
    sys.exit(app.exec_())
