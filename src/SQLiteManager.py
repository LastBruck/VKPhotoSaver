import sqlite3

class SqliteManager:
    def __init__(self, name=str, tablename=str):
        self.tablename = tablename
        self.__db = sqlite3.connect(name)
        self.__cur = self.__db.cursor()
        

    def create_table(self, fields=dict[str,str]):
        field_list = []
        for (val, type) in fields.items():
            dict = f"{val} {type} "
            field_list.append(dict)
            field = " , ".join(field_list)
        self.__cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.tablename} (
        ID INTEGER PRIMARY KEY,
        {field})""")


    def contains(self, checkfield=str, value=str|int|bytes):

        result = self.select([checkfield], checkfield, value)

        return len(result) > 0


    def insert(self, data=dict[str, str|int|bytes]):
        columns =[]
        values = []
        for (column, value) in data.items():
            columns.append(column)
            values.append(value)
                
        placeholders = ["?" for i in range(len(columns))]
        query = f'INSERT INTO {self.tablename} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
        self.__cur.execute(query, values)
        self.__db.commit()


    def select(self, columns=list[str], field=str|None, value=str|int|bytes|None):
        query = f'SELECT {", ".join(columns)} FROM {self.tablename}'
        if field is None or value is None:
            self.__cur.execute(query)

        else:
            query += f' WHERE {field} = ?'
            self.__cur.execute(query, (value,))

        return self.__cur.fetchall()


    def delete_table(self):
        self.__cur.execute(f'DROP TABLE IF EXISTS {self.tablename}')


    def delete(self,field=str|None, value=str|int|bytes|None):
        query = f'DELETE FROM {self.tablename}'
        if field is None or value is None:
            self.__cur.execute(query)

        else:
            query += f' WHERE {field} = ?'
            self.__cur.execute(query, (value,))
        self.__db.commit()
    
    
    def close(self):
        self.__db.close()

