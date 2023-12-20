# import sqlite3



# async def update_photo (data: dict):
#     conn = sqlite3.connect('shop.db')
#     cursor = conn.cursor()
      
#     photo = data.get ('photo') 
#     products_id = data.get('id') 


#     query = f"update products set photo='{photo}' where id ={products_id}"
#     update = cursor.execute(query)
#     conn.commit()
#     return update


# async def update_name (data: dict):
#     conn = sqlite3.connect('shop.db')
#     cursor = conn.cursor()
      
#     name = data.get ('name') 
#     id = data.get('id') 


#     query = f"update new_car set name='{name}' where id ={id}"
#     update = cursor.execute(query)
#     conn.commit()
#     return update
