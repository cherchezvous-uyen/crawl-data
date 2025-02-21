# import mysql.connector

# class MySQLHandler:
#     def __init__(self, host='localhost', user='root', password='', database='champions'):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.connection = None
#         self.cursor = None

#     def connect(self):
#         if not self.connection:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )
#             self.cursor = self.connection.cursor()

#     def insert_data(self, table, data):
#         if not self.connection:
#             self.connect()

#         # Insert data vào bảng news (ví dụ)
#         query = f"""
#         INSERT INTO {table} (title, url, location, description, publish_date, content, author, tags)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         self.cursor.execute(query, data)
#         self.connection.commit()

#     def close(self):
#         if self.connection:
#             self.cursor.close()
#             self.connection.close()
