import streamlit as st 
from db import db_connection, db_,db_query, insertion

st.write ("""
# КАБЕЛЬНЫЙ ЖУРНАЛ         
""")
cur = db_connection()
print ('Соединение не установлено')

with st.form('FORM'): 

    tab1, tab2 = st.tabs(['Учет', "Таблица данных"])
    
    with tab1:
        qur =db_query('user', cur)
        fio = st.selectbox('ФИО',qur)
        user = qur.loc[qur['fio']== fio]['id'].values.tolist()[0]

        col1, col2 = st.columns(2)

        serv = col1.selectbox('Номер серверной', db_query('server_num', cur))
        with col1.expander('Серверные',expanded=False):
            st.table(db_('server_num',cur))

        arm = col2.selectbox('Номер АРМ', db_query('arm', cur),)
        with col2.expander('АРМ',expanded=False):
            st.table(db_('arm',cur))

        ss = st.form_submit_button('Добавить запись', use_container_width=True)

        if ss:
            insertion(serv,user, arm, cur)
            # query = "INSERT INTO accounting (server_num_id,user_id,arm_id) VALUES ({},{},{});".format(serv,user,arm)
            # cursor = cur.cursor()
            # cursor.execute(query)
            # cur.commit()

    with tab2:
        st.table(db_('accounting',cur))

    