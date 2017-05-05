# -*- coding: utf-8 -*-
"""
mvc.py

My first attempts with OOP and Design Patterns (here MVC) in Python
Code from here: http://kennison.name/files/zopestore/uploads/python/DesignPatternsInPython_ver0.1.pdf

@author Tset Noitamotua (tset.no@gmail.com)
@version 2017-05-05
"""


import sqlite3 as lite
#import types
# import sys

class DefectModel:
    """
    The DefectModel class describes model of a defect.
    """
    def get_defect_list(self, component):
        query = "SELECT Id FROM Defects WHERE Component = '%s'" % component
        defect_list = self._dbselect(query)
        list = []
        for row in defect_list:
            list.append(row[0])
        return list

    def get_summary(self, id):
        query = "SELECT Summary FROM Defects WHERE Id = '%d'" % id
        summary = self._dbselect(query)
        for row in summary:
            return row[0]

    def _dbselect(self, query):
        con = lite.connect('TMS.db')
        cur = con.cursor()
        results = cur.execute(query)
        con.commit()
        #cur.close()
        return results

class DefectView:
    def summary(self, summary, defectid):
        print("#### Defect Summary for defect# %d####\n%s" % (defectid,summary))
    def defectList(self, list, category):
        print("#### Defect List for %s ####\n" % category)
        for defect in list:
            print(defect)

class Controller:
    def __init__(self):
        pass

    def getDefectSummary(self, defectid):
        model = DefectModel()
        view = DefectView()
        summary_data = model.get_summary(defectid)
        return view.summary(summary_data, defectid)

    def getDefectList(self, component):
        model = DefectModel()
        view = DefectView()
        defectlist_data = model.get_defect_list(component)
        return view.defectList(defectlist_data, component)
