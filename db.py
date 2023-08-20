import sqlite3 as sql
import pandas as pd  

def db_connection ():
    try:
        return sql.connect(database= 'test.db')
    except:
        print ('Соединение не установлено')

def db_query (table:str, cur):
    qu = f"""SELECT id FROM {table}"""
    if table == 'user':
        query = pd.read_sql("""select                           
                                "name"||\' \'||surname||\' \'||patronimic|| ' | подразделение: '|| unit.unit_name   as fio
                            , user.id
                            from user 
                            join unit on unit.id = user.unit""", con=cur)

    elif table := any(['server_num','arm']):
        query = pd.read_sql(qu, con=cur)
    return query

def db_ (table:str, cur):
    if table == 'server_num':
        fr = pd.read_sql("""SELECT 
                                id as 'Номер серверной'
                                , "№ розетки"
                                ,"№ порта розетки"
                                , "№ порта на патчпанели"
                                , "Длина"
                            FROM server_num
                        """, con=cur)

    elif table == 'arm':
        fr = pd.read_sql("""SELECT 
                                id as 'Номер АРМ'
                                , arm_name as 'Имя АРМ'
                                , ip_arm as 'IP адрес АРМ'
                                , mac_arm as 'MAC адрес АРМ'
                            FROM arm
                        """, con=cur)

    elif table == 'accounting':
        fr = pd.read_sql("""SELECT 
                                sn."№ розетки"
                                , sn."№ порта розетки"
                                , sn."№ порта на патчпанели"
                                , sn."Длина"
                                , u."name" || ' ' || u.surname || ' ' || u.patronimic as 'ФИО'
                                , unit.unit_name as 'Подразделение'
                                , arm.arm_name as 'Имя АРМ'
                                , arm.ip_arm as 'IP адрес АРМ'
                                , arm.mac_arm  as 'MAC адрес АРМ'
                            FROM accounting a
                            JOIN server_num sn ON a.server_num_id = sn.id
                            JOIN arm ON a.arm_id = arm.id
                            JOIN user u ON a.user_id = u.id
                            JOIN unit ON u.unit = unit.id
                            """, con=cur)
    return fr

def insertion(server,user,arm, cur:sql.Connection):
    query = "INSERT INTO accounting (server_num_id,user_id,arm_id) VALUES ({},{},{});".format(server,user,arm)
    cursor = cur.cursor()
    cursor.execute(query)
    cur.commit()