from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from os import path
from PyQt5.uic import loadUiType
import sqlite3
import time
import os
def resource_path(relative_path):
    '''Get absolute path to resource, works for dev and for PyInstaller'''
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

FORM_CLASS, _ = loadUiType(resource_path('main.ui'))

class Main(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.NAVIGATE()

    def Handle_Buttons(self):
        self.refresh_button.clicked.connect(self.GET_DATA)
        self.search_button_inventory_details.clicked.connect(self.SEARCH_DATA)
        self.add_edit_inventory.clicked.connect(self.ADD_INVENTORY)
        self.delete_edit_inventory.clicked.connect(self.DELETE_INVENTORY)
        self.check_button_inventory_management.clicked.connect(self.CHECK_LEVEL)
        self.last_entry_edit_inventory.clicked.connect(self.LAST_ENTRY)
        self.first_entry_edit_inventory.clicked.connect(self.FIRST_ENTRY)
        self.next_entry_edit_inventory.clicked.connect(self.NEXT_ENTRY)
        self.previous_entry_edit_inventory.clicked.connect(self.PREVIOUS_ENTRY)
        self.update_edit_inventory.clicked.connect(self.UPDATE_INVENTORY)

    def UPDATE_INVENTORY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        id_ref = self.id_edit_inventory.text()
        reference = self.reference_edit_inventory.text()
        part_name = self.part_name_edit_inventory.text()
        min_area = self.min_area_edit_inventory.text()
        max_area = self.max_area_edit_inventory.text()
        num_holes = self.num_holes_edit_inventory.text()
        min_dia = self.min_dia_edit_inventory.text()
        max_dia = self.max_dia_edit_inventory.text()
        count = self.count_edit_inventory.value()

        c.execute("UPDATE parts_table SET ID=?, REFERENCE=?, PartName=?, MinArea=?, MaxArea=?, NumberOfHoles=?, MinDiameter=?, MaxDiameter=?, Count=? WHERE ID=?", 
        (id_ref,reference,part_name,min_area,max_area,num_holes,min_dia,max_dia,count,id_ref))
        conn.commit()
        conn.close()
        QMessageBox.about(self, "Success", "Record Updated")
        self.GET_DATA()

    def PREVIOUS_ENTRY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        id_ref = self.id_edit_inventory.text()
        if id_ref=='1' or None:
            id_ref='2'
        result = c.execute("SELECT * FROM parts_table WHERE ID<?  ORDER BY ID DESC LIMIT 1", (id_ref,))
        result = c.fetchone()
        self.id_edit_inventory.setText(str(result[0]))
        self.reference_edit_inventory.setText(str(result[1]))
        self.part_name_edit_inventory.setText(str(result[2]))
        self.min_area_edit_inventory.setText(str(result[3]))
        self.max_area_edit_inventory.setText(str(result[4]))
        self.num_holes_edit_inventory.setText(str(result[5]))
        self.min_dia_edit_inventory.setText(str(result[6]))
        self.max_dia_edit_inventory.setText(str(result[7]))
        self.count_edit_inventory.setValue(result[8])

        conn.close()

    def NEXT_ENTRY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        c1 = conn.cursor()
        id_ref = self.id_edit_inventory.text()
        max_id = c1.execute("SELECT MAX(ID) FROM parts_table").fetchone()[0]
        if id_ref == str(max_id) or None:
            id_ref = str(int(max_id)-1)
        result = c.execute("SELECT * FROM parts_table WHERE ID>?  ORDER BY ID ASC LIMIT 1", (id_ref,))
        result = c.fetchone()
        self.id_edit_inventory.setText(str(result[0]))
        self.reference_edit_inventory.setText(str(result[1]))
        self.part_name_edit_inventory.setText(str(result[2]))
        self.min_area_edit_inventory.setText(str(result[3]))
        self.max_area_edit_inventory.setText(str(result[4]))
        self.num_holes_edit_inventory.setText(str(result[5]))
        self.min_dia_edit_inventory.setText(str(result[6]))
        self.max_dia_edit_inventory.setText(str(result[7]))
        self.count_edit_inventory.setValue(result[8])

        conn.close()

    def FIRST_ENTRY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        result = c.execute("SELECT * FROM parts_table ORDER BY ID ASC LIMIT 1")
        result = c.fetchone()
        self.id_edit_inventory.setText(str(result[0]))
        self.reference_edit_inventory.setText(str(result[1]))
        self.part_name_edit_inventory.setText(str(result[2]))
        self.min_area_edit_inventory.setText(str(result[3]))
        self.max_area_edit_inventory.setText(str(result[4]))
        self.num_holes_edit_inventory.setText(str(result[5]))
        self.min_dia_edit_inventory.setText(str(result[6]))
        self.max_dia_edit_inventory.setText(str(result[7]))
        self.count_edit_inventory.setValue(result[8])

        conn.close()

    def LAST_ENTRY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        result = c.execute("SELECT * FROM parts_table ORDER BY ID DESC LIMIT 1")
        result = c.fetchone()
        self.id_edit_inventory.setText(str(result[0]))
        self.reference_edit_inventory.setText(str(result[1]))
        self.part_name_edit_inventory.setText(str(result[2]))
        self.min_area_edit_inventory.setText(str(result[3]))
        self.max_area_edit_inventory.setText(str(result[4]))
        self.num_holes_edit_inventory.setText(str(result[5]))
        self.min_dia_edit_inventory.setText(str(result[6]))
        self.max_dia_edit_inventory.setText(str(result[7]))
        self.count_edit_inventory.setValue(result[8])

        conn.close()

    def NAVIGATE(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        result = c.execute("SELECT * FROM parts_table")
        result = c.fetchone()
        self.id_edit_inventory.setText(str(result[0]))
        self.reference_edit_inventory.setText(str(result[1]))
        self.part_name_edit_inventory.setText(str(result[2]))
        self.min_area_edit_inventory.setText(str(result[3]))
        self.max_area_edit_inventory.setText(str(result[4]))
        self.num_holes_edit_inventory.setText(str(result[5]))
        self.min_dia_edit_inventory.setText(str(result[6]))
        self.max_dia_edit_inventory.setText(str(result[7]))
        self.count_edit_inventory.setValue(result[8])

        conn.close()

    def CHECK_LEVEL(self):
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        result2 = c.execute("SELECT Reference, PartName, Count FROM parts_table ORDER BY Count ASC LIMIT 5")
        self.table_inventory_statistics.setRowCount(0)
        for row_count, row_data in enumerate(result2):
            self.table_inventory_statistics.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.table_inventory_statistics.setItem(row_count, column_count, QTableWidgetItem(str(data)))

    def DELETE_INVENTORY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        reference_filter = self.id_edit_inventory.text()
        c.execute("DELETE FROM parts_table WHERE ID=?", (reference_filter,))
        conn.commit()
        conn.close()
        QMessageBox.about(self, "Success", "Part Deleted")
        self.GET_DATA()
        self.id_edit_inventory.setText("")
        self.reference_edit_inventory.setText("")
        self.part_name_edit_inventory.setText("")
        self.min_area_edit_inventory.setText("")
        self.max_area_edit_inventory.setText("")
        self.num_holes_edit_inventory.setText("")
        self.min_dia_edit_inventory.setText("")
        self.max_dia_edit_inventory.setText("")
        self.count_edit_inventory.setValue(0)
        self.GET_DATA()
    
    def ADD_INVENTORY(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        c1 = conn.cursor()
        c2 = conn.cursor()
        part_reference = self.reference_edit_inventory.text() or 0
        part_name = self.part_name_edit_inventory.text() or 'None'
        part_min_area = self.min_area_edit_inventory.text() or 0
        part_max_area = self.max_area_edit_inventory.text() or 0
        part_num_holes = self.num_holes_edit_inventory.text() or 0
        part_min_dia = self.min_dia_edit_inventory.text() or 0
        part_max_dia = self.max_dia_edit_inventory.text() or 0
        part_count = self.count_edit_inventory.text() or 0

        c.execute("INSERT INTO parts_table (Reference, PartName, MinArea, MaxArea, NumberOfHoles, MinDiameter, MaxDiameter, Count) VALUES (?,?,?,?,?,?,?,?)", 
        (part_reference, part_name, part_min_area, part_max_area, part_num_holes, part_min_dia, part_max_dia, part_count))
    
        conn.commit()
        max_id = c1.execute("SELECT MAX(ID) FROM parts_table").fetchone()[0]
        result = c2.execute("SELECT * FROM parts_table WHERE ID=?", (max_id,)).fetchone()
        self.id_edit_inventory.setText(str(result[0]))
        self.reference_edit_inventory.setText(str(result[1]))
        self.part_name_edit_inventory.setText(str(result[2]))
        self.min_area_edit_inventory.setText(str(result[3]))
        self.max_area_edit_inventory.setText(str(result[4]))
        self.num_holes_edit_inventory.setText(str(result[5]))
        self.min_dia_edit_inventory.setText(str(result[6]))
        self.max_dia_edit_inventory.setText(str(result[7]))
        self.count_edit_inventory.setValue(result[8])
        QMessageBox.about(self, "Success", "Part Added")
        conn.close()
        self.GET_DATA()

    def GET_DATA(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        c1 = conn.cursor()
        c2 = conn.cursor()
        c3 = conn.cursor()
        c4 = conn.cursor()
        result = c.execute("SELECT * FROM parts_table")
        self.table_inventory_details.setRowCount(0)

        for row_count, row_data in enumerate(result):
            self.table_inventory_details.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.table_inventory_details.setItem(row_count, column_count, QTableWidgetItem(str(data)))

        number_reference_query = "SELECT COUNT(DISTINCT Reference) FROM parts_table"
        number_parts_query = "SELECT COUNT(DISTINCT PartName) FROM parts_table"
        min_diameter_query = "SELECT MIN(MinDiameter), Reference FROM parts_table"
        max_diameter_query = "SELECT MAX(MaxDiameter), Reference FROM parts_table"

        number_reference = c1.execute(number_reference_query)
        number_parts = c2.execute(number_parts_query)
        min_hole = c3.execute(min_diameter_query).fetchone()
        max_hole = c4.execute(max_diameter_query).fetchone()

        self.label_num_ref_inventory_statistics.setText(str(number_reference.fetchone()[0]))
        self.label_num_parts_inventory_statistics.setText(str(number_parts.fetchone()[0]))
        self.label_min_holes_inventory_statistics.setText(str(min_hole[0]))
        self.label_max_holes_inventory_statistics.setText(str(max_hole[0]))
        self.label_min_holes_1_inventory_statistics.setText(str(min_hole[1]))
        self.label_max_holes_1_inventory_statistics.setText(str(max_hole[1]))

        conn.close()
    
    def SEARCH_DATA(self):
        # Connect to sqlite3 and populate our GUI table with data
        conn = sqlite3.connect(resource_path('parts.db'))
        c = conn.cursor()
        number_filter = int(self.count_level_filter_inventory_details.text())
        result = c.execute("SELECT * FROM parts_table WHERE Count<=?", (number_filter,))
        self.table_inventory_details.setRowCount(0)

        for row_count, row_data in enumerate(result):
            self.table_inventory_details.insertRow(row_count)
            for column_count, data in enumerate(row_data):
                self.table_inventory_details.setItem(row_count, column_count, QTableWidgetItem(str(data)))
        conn.close()
        

def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()