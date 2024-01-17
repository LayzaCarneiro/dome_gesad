import sqlite3

class AnalyticsEngine:
    def __init__(self, AC):
        super().__init__()
        # self.__IC = IC
        self.__AC = AC
        self.__TDB = None
        
    def __executeSqlCmd(self, sqlCmd):
        if self.__TDB is None:
            self.__TDB = sqlite3.connect(self.__AC.getTransactionDB_path(), check_same_thread=False)
        result = self.__TDB.cursor().execute(sqlCmd)
        self.__TDB.commit()

        return result
    
    def media(self, table, row):
        sql_cmd = "SELECT AVG(" + row + ") AS media_pontuacao FROM managedsys_web_" + table
        cursor = self.__executeSqlCmd(sql_cmd)
        resultado = cursor.fetchone()
        
        return resultado[0]
        
# Funções para retornar valores como média, maior valor, menor valor de uma tabela
# Receber mensagem do user como "get media of students" or "get highest value" --> Fazer a parte de NLP 
# Depois transformar esse NLP para comando SQL 
# Retornar valor desejado