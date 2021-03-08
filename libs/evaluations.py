#sys libs
import os, sys
import os.path

#tool libs
sys.path.insert(0, '..')
from db.connect import DB

sys.path.insert(0, '..')
from db.evaluations import Evaluations as DB_Evaluations

from libs.helpers import Helpers

# class for evaluations functions; mainly to read and write database content; the library is necessary to process indicators
class Evaluations:
    def __init__(self):
        self.data = []


#read from db

#helper to check for existing module entries in the evaluations table
    def getEvaluationModule(hash, evaluations_module):
        db = DB()
        rows = DB_Evaluations.getEvaluationModule(db.cursor, hash, evaluations_module)
        db.DBDisconnect()
        return rows

#helper to check for existing module and result entries in the evaluations table
    def getEvaluationModuleResult(hash, evaluations_module, evaluations_result):
        db = DB()
        rows = DB_Evaluations.getEvaluationModuleResult(db.cursor, hash, evaluations_module, evaluations_result)
        db.DBDisconnect()
        return rows

#read hashes with less than 53 evaluation results to select the unprocessed results and to check for missing values
    def getResultHashes():
        db = DB()
        rows = DB_Evaluations.getResultHashes(db.cursor)
        db.DBDisconnect()
        return rows

    def getResultHashesNoUpdate(number_indicators):
        db = DB()
        rows = DB_Evaluations.getResultHashesNoUpdate(db.cursor, number_indicators)
        db.DBDisconnect()
        return rows

    def getEvaluationsDate(hash, module):
        db = DB()
        rows = DB_Evaluations.getEvaluationsDate(db.cursor, hash, module)
        db.DBDisconnect()
        return rows


    def getResultstoClassify(indicators):
        db = DB()
        rows = DB_Evaluations.getResultstoClassify(db.cursor, indicators)
        db.DBDisconnect()
        return rows


    def getEvaluationsResults(hash):
        db = DB()
        rows = DB_Evaluations.getEvaluationsResults(db.cursor, hash)
        db.DBDisconnect()
        return rows


    def getClassificationResult(hash):
        db = DB()
        rows = DB_Evaluations.getClassificationResult(db.cursor, hash)
        db.DBDisconnect()
        return rows


#write to db

#insert indicators, results of url categories and plugins evaluations to the table
    def insertEvaluationResult(hash, module, value, today):
        db = DB()
        DB_Evaluations.insertEvaluationResult(db.cursor, hash, module, value, today)
        db.DBDisconnect()

#update evaulation results
    def UpdateEvaluationResult(value, date, hash, module):
        db = DB()
        DB_Evaluations.UpdateEvaluationResult(db.cursor, value, date, hash, module)
        db.DBDisconnect()

    def insertClassificationResult(hash, result, today):
        db = DB()
        DB_Evaluations.insertClassificationResult(db.cursor, hash, result, today)
        db.DBDisconnect()

#delete from db

#function to remove duplicates
    def deleteDuplicates():
        db = DB()
        rows = DB_Evaluations.deleteDuplicates(db.cursor)
        db.DBDisconnect()


    def deleteEvaluations(queries_id):
        pass

    def deleteClassifications(queries_id):
        pass