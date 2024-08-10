

import  mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hojimurad",
  database ="base"
)


cursor = mydb.cursor()

def Create_table():
    query = ("""create table if not exists Human(
        id integer auto_increment primary key,
        full_name varchar(255),
        position varchar(255),
        salary int
    )
    
""")
    try:

        cursor.execute(query)

    except:
        print("Jadval yaratishda xatolik")

    return  True


def MalumotYoz(full_name:str,position:str,salary:int):


    inser_query = f"""
    
    insert into Human(full_name,position,salary) values('{full_name}','{position}',{salary})
    
    """

    try:
        cursor.execute(inser_query)
        mydb.commit()
    except:
        print("Insert bolimida xatolik")

    return  True

def malumotOqish():

    query = "select * from Human"
    cursor.execute(query)
    data  = cursor.fetchall()
    return data

