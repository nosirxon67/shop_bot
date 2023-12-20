
# import sqlite3

# async def get_all_car(chat_id: int):
#     conn = sqlite3.connect("shop.db")
#     cursor = conn.cursor()

#     query = f"select * from new_car where chat_id={chat_id}"
#     new_car = cursor.execute(query).fetchall()
#     return new_car