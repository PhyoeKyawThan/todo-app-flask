from sqlalchemy import create_engine, Table, Column, MetaData, String, Integer

engine = create_engine("mysql://root:Domak9090@127.0.0.1:3306/todoDatas")
metadata = MetaData()

#creating a database 
class DB:
    
    def __init__(self) -> None:
        self.table = Table('todos_data', metadata,
                  Column('id', Integer ,primary_key=True),
                  Column('title', String(50) ,nullable=False),
                  Column('todo', String(255), nullable=False)
                  , autoload_with=engine)
        
    def insert(self, data):
        conn = engine.connect()
        conn.execute(self.table.insert(), data)
        conn.commit()
        conn.close()
        return 'Successfully Insert datas'
    
    def delete(self, id):
        conn = engine.connect()
        conn.execute(self.table.delete().where(self.table.c.id == id))
        conn.commit()
        conn.close()
        return f'Deleted'

    def __repr__(self) -> str:
        return 'successfully commit'

if __name__ == '__main__':
    db = DB()
    print(db.delete(3))