from sqlalchemy import create_engine, Table, Column, MetaData, String, Integer, select

engine = create_engine("mysql://root:Domak9090@127.0.0.1:3306/todoDatas")
metadata = MetaData()

#creating a database 
class DB:
    
    def __init__(self) -> None:
        self.table = Table('todos_data', metadata,
                  Column('id', Integer ,primary_key=True),
                  Column('title', String(50) ,nullable=False),
                  Column('todo', String(255), nullable=False)
                  )
        metadata.create_all(engine)
        
    def insert(self, data: list)->str:
        conn = engine.connect()
        conn.execute(self.table.insert(), data)
        conn.commit()
        conn.close()
        return 'Successfully Insert datas'
    
    def delete(self, id)->str:
        conn = engine.connect()
        conn.execute(self.table.delete().where(self.table.c.id == id))
        conn.commit()
        conn.close()
        return f'Deleted'

    def update(self, id: int, column_name: str, update_data: str)-> str:
        conn = engine.connect()
        if(column_name == 'title'):
            conn.execute(self.table.update().where(self.table.c.id == id).values(title=update_data))
        elif(column_name == 'todo'):
            conn.execute(self.table.update().where(self.table.c.id == id).values(todo=update_data))
        else:
            return 'Something worng with column name'
        conn.commit()
        conn.close()
        return "Updated Successful!"
    
    def todo_lists(self)->list:
        conn = engine.connect()
        datas = conn.execute(select(self.table))
        return datas
    def __repr__(self) -> str:
        return 'successfully commit'

if __name__ == '__main__':
    db = DB()
    for data in db.todo_lists():
        print(data)
    