import sys
import sqlite3
from PyQt5.QtWidgets import *
from ui_fantasy import Ui_MainWindow
import database

# Initialize database
database.create_tables()
database.insert_players()
database.insert_match_data()


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Variables
        self.points = 1000
        self.selected = []
        self.team_name = ""

        # Menu actions
        self.ui.actionNew_Team.triggered.connect(self.new_team)
        self.ui.actionSave_Team.triggered.connect(self.save_team)
        self.ui.actionEvaluate_Team.triggered.connect(self.evaluate)

        # Double click events
        self.ui.listAvailable.itemDoubleClicked.connect(self.add_player)
        self.ui.listSelected.itemDoubleClicked.connect(self.remove_player)

        # Radio buttons
        self.ui.radioBAT.toggled.connect(lambda: self.load_players("BAT"))
        self.ui.radioBOWL.toggled.connect(lambda: self.load_players("BOWL"))
        self.ui.radioALL.toggled.connect(lambda: self.load_players("ALL"))
        self.ui.radioWK.toggled.connect(lambda: self.load_players("WK"))

        # Initially disable
        self.disable_ui()

    # ---------------- DISABLE UI ----------------
    def disable_ui(self):
        self.ui.listAvailable.setEnabled(False)
        self.ui.listSelected.setEnabled(False)

    def enable_ui(self):
        self.ui.listAvailable.setEnabled(True)
        self.ui.listSelected.setEnabled(True)

    # ---------------- NEW TEAM ----------------
    def new_team(self):
        name, ok = QInputDialog.getText(self, "Team", "Enter Team Name")
        if ok and name:
            self.team_name = name
            self.ui.labelTeamName.setText(name)
            self.enable_ui()
            self.load_players("BAT")

    # ---------------- LOAD PLAYERS ----------------
    def load_players(self, category):
        self.ui.listAvailable.clear()

        conn = sqlite3.connect("fantasy.db")
        cur = conn.cursor()
        cur.execute("SELECT name FROM players WHERE category=?", (category,))
        data = cur.fetchall()
        conn.close()

        for p in data:
            if p[0] not in self.selected:
                self.ui.listAvailable.addItem(p[0])

    # ---------------- ADD PLAYER ----------------
    def add_player(self):
        item = self.ui.listAvailable.currentItem()
        if not item:
            return

        player = item.text()

        conn = sqlite3.connect("fantasy.db")
        cur = conn.cursor()
        cur.execute("SELECT value FROM players WHERE name=?", (player,))
        value = cur.fetchone()[0]
        conn.close()

        if self.points < value:
            QMessageBox.warning(self, "Error", "Not enough points")
            return

        self.points -= value
        self.selected.append(player)

        self.ui.listSelected.addItem(player)
        self.ui.listAvailable.takeItem(self.ui.listAvailable.row(item))

        self.update_points()

    # ---------------- REMOVE PLAYER ----------------
    def remove_player(self):
        item = self.ui.listSelected.currentItem()
        if not item:
            return

        player = item.text()

        conn = sqlite3.connect("fantasy.db")
        cur = conn.cursor()
        cur.execute("SELECT value FROM players WHERE name=?", (player,))
        value = cur.fetchone()[0]
        conn.close()

        self.points += value
        self.selected.remove(player)

        self.ui.listAvailable.addItem(player)
        self.ui.listSelected.takeItem(self.ui.listSelected.row(item))

        self.update_points()

    # ---------------- UPDATE POINTS ----------------
    def update_points(self):
        self.ui.labelPointsAvailable.setText(f"Points Available: {self.points}")
        self.ui.labelPointsUsed.setText(f"Points Used: {1000 - self.points}")

    # ---------------- SAVE TEAM ----------------
    def save_team(self):
        if not self.team_name:
            QMessageBox.warning(self, "Error", "Create team first")
            return

        conn = sqlite3.connect("fantasy.db")
        cur = conn.cursor()

        for p in self.selected:
            cur.execute("INSERT INTO teams VALUES (?,?)", (self.team_name, p))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "Success", "Team Saved")

    # ---------------- EVALUATE ----------------
    def evaluate(self):
        score = 0

        conn = sqlite3.connect("fantasy.db")
        cur = conn.cursor()

        for p in self.selected:
            cur.execute("SELECT runs, wickets, catches FROM match WHERE player=?", (p,))
            data = cur.fetchone()

            if data:
                r, w, c = data
                score += r + (w * 10) + (c * 5)

        conn.close()

        QMessageBox.information(self, "Score", f"Total Score: {score}")


# ---------------- RUN APP ----------------
app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())