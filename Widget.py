import sys
import PyQt5 as p
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout , QTableWidget, QPushButton,  QComboBox, QTableWidgetItem, QInputDialog
from process_git import ProcessGit


class GitWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.create_window()

    def create_window(self):
            self.showMaximized()
            self.setWindowTitle("GitUpdates")

            print("Window visible")
            self.show()
            self.show_dialog()

    def show_dialog(self):
        user,userOk = QInputDialog.getText(self,"Git User Name", "Enter user name")
        password, passOk = QInputDialog.getText(self.parent(), self.tr("Enter Password"), self.tr("Password:"),
        p.QtWidgets.QLineEdit.Password)

        if userOk and passOk:
              repos = ProcessGit.start_git(ProcessGit,user,password)
              self.repos = repos
              self.add_properties(repos)
              self.process_repos(repos)
              self.layout = QVBoxLayout()
              self.layout.addWidget(self.properties)
              button = QPushButton("Add Properties",self);
              button.clicked.connect(self.on_click)
              self.layout.addWidget(button)

              clear = QPushButton("clear", self);
              clear.clicked.connect(self.on_clear)
              self.layout.addWidget(clear)
              self.layout.addWidget(self.table)
              self.setLayout(self.layout)

    def on_clear(self):
        for i in range(1,self.colorCount()):
            self.table.removeColumn(i)
        self.layout.update()

    def on_click(self):
        print("button clicked")
       # self.table.clear(self);
        print(self.properties.currentText());
        self.add_columns(self.properties.currentText())
        #self.process_repos(self.repos)

    def add_columns(self, columnData):
        row = 0;
        column = self.table.columnCount()
        self.table.insertColumn(column)
        self.table.setItem(row, column, QTableWidgetItem(str.upper(str(columnData))))
        row += 1
        for repo in self.repos:
            value = str(getattr(repo, str(columnData.strip("_"))))
            self.table.setItem(row, column, QTableWidgetItem(str(value)))
            row += 1
        self.layout.update()

    def add_properties(self,repos):
        print("add properties")
        self.properties = QComboBox(self)
        count =0;
        for repo in repos :
            if count == 0:
                cnt = 0
                for prop, val in vars(repo).items():
                    self.properties.addItem(prop)
                    cnt +=1
                count =1


    def process_repos(self,repos):
        self.table = QTableWidget()
        self.table.setUpdatesEnabled(True)
        self.table.setRowCount(repos.totalCount)
        self.table.setColumnCount(1)
        self.table.setAutoScroll(True)
        self.table.setWindowTitle("Git Repositories")
        row = 0;
        column = 0;
        self.table.setItem(row,column, QTableWidgetItem(str.upper("Repository Name")))
        row +=1
        for repo in repos:
            self.table.setItem(row, column, QTableWidgetItem(repo.name))
            row +=1





    def closeEvent(self, event):
        print("Event called")


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = GitWindow()
    sys.exit(app.exec_())


