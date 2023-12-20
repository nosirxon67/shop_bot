# import sqlite3


# async def insert_new_car(data: dict):
#     conn = sqlite3.connect('shop.db')
#     cursor = conn.cursor()
#     chat_id = data.get('chat_id')
#     name = data.get('name')
#     photo = data.get('image')
    

#     query = (f""" insert into new_car (photo, name,  chat_id)
#     values('{photo}','{name}','{chat_id}')""")
#     cursor.execute(query)
#     conn.commit()
#     return True


