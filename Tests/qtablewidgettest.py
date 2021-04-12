from PyQt5.QtWidgets import QTableWidgetItem
import datetime

        data = [('John', datetime.datetime(2019, 5, 5, 0, 54), datetime.datetime(2019, 5, 26, 22, 51, 36)),
        ('Rex', datetime.datetime(2019, 5, 26, 22, 51, 36), datetime.datetime(2019, 6, 15, 10, 22, 48)),
        ('Watson', datetime.datetime(2019, 6, 15, 10, 22, 48), datetime.datetime(2019, 7, 8, 13, 33, 36)),
        ('Manila', datetime.datetime(2019, 7, 8, 13, 33, 36), datetime.datetime(2019, 7, 29, 6, 18)),
        ('Pete', datetime.datetime(2019, 7, 29, 6, 18), datetime.datetime(2019, 8, 6, 18, 50, 24)),
        ('Mathew', datetime.datetime(2019, 8, 6, 18, 50, 24), datetime.datetime(2019, 8, 31, 3, 14, 24))]

        numrows = len(data)  # 6 rows in your example
        numcols = len(data[0])  # 3 columns in your example

        # Set colums and rows in QTableWidget
        self.tableWidget.setColumnCount(numcols)
        self.tableWidget.setRowCount(numrows)

        # Loops to add values into QTableWidget
        for row in range(numrows):
            for column in range(numcols):
                # Check if value datatime, if True convert to string
                if isinstance(data[row][column], datetime.datetime):
                    self.tableWidget.setItem(row, column, QTableWidgetItem((data[row][column].strftime('%d/%m/%Y %H:%M:%S'))))
                else:
                    self.tableWidget.setItem(row, column, QTableWidgetItem((data[row][column])))