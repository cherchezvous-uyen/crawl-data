import mysql.connector

class MySQLPipeline:
    def __init__(self):
        try:
            self.db_handler = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='champions'
            )
            self.cursor = self.db_handler.cursor()
            print("Kết nối đến MySQL thành công!")
        except mysql.connector.Error as e:
            print(f"Lỗi khi kết nối đến MySQL: {e}")
            raise

    def open_spider(self, spider):
        try:
            # Tạo bảng nếu chưa tồn tại
            create_table_query = """
            CREATE TABLE IF NOT EXISTS champ (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                url VARCHAR(255),
                time DATETIME,
                author VARCHAR(255),
                category VARCHAR(255),
                content TEXT,
                description TEXT,
                tags TEXT
            )
            """
            self.cursor.execute(create_table_query)
            self.db_handler.commit()
            print("Bảng champ đã được tạo hoặc đã tồn tại.")
        except mysql.connector.Error as e:
            print(f"Lỗi khi tạo bảng: {e}")

    def process_item(self, item, spider):
        try:
            # Chèn dữ liệu vào bảng champ
            insert_query = """
            INSERT INTO champ (title, url, time, author, category, content, description, tags)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                item['title'],
                item['url'],
                item['time'],
                item['author'],
                item['category'],
                item['content'],
                item['description'],
                item['tags']
            )
            self.cursor.execute(insert_query, data)
            self.db_handler.commit()
            print(f"Đã chèn dữ liệu vào bảng champ: {item['title']}")
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn dữ liệu: {e}")
        return item

    def close_spider(self, spider):
        # Đóng kết nối MySQL khi spider kết thúc
        self.cursor.close()
        self.db_handler.close()
        print("Đã đóng kết nối MySQL.")
