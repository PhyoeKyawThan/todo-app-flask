from sqlalchemy import create_engine, Table, Column, MetaData, String, Integer

engine = create_engine("mysql://root:Domak9090@127.0.0.1:3306/todoDatas")
metadata = MetaData()

#creating a database 
class DB:
    table = Table('todos_data', metadata,
                  Column('id', Integer ,primary_key=True),
                  Column('title', String(50) ,nullable=False),
                  Column('todo', String(255), nullable=False)
                  )
    conn = engine.connect()
    def __init__(self, title, todo) -> None:
        self.data: list = [
            {'title': self.title, 'todo': self.todo}
        ]
        self.conn.execute(self.table.insert(), self.data)
        self.conn.commit()
        self.conn.close()
    
    def delete(self, id):
        sle

