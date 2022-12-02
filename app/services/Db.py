import psycopg2

class Db:
    
    db = None
    
    def getConnection(self):
        return psycopg2.connect(dbname= self.dbname, user = self.user, password = self.pasw, host = self.host)
    
    def execute(self, sql, params = None):
        with self.getConnection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, params)
                
    def getData(self, sql, params = None):
        with self.getConnection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, params)
                data = curr.fetchall()
        return data
                
    def getFirst(self, sql, params = None):
        with self.getConnection() as conn:
            with conn.cursor() as curr:
                curr.execute(sql, params)
                data = curr.fetchone()
        return data
        
    
    def __init__(self, dbname, user, pasw, host = 'localhost') -> None:
        self.dbname = dbname
        self.user = user
        self.pasw = pasw
        self.host = host
        Db.db = self