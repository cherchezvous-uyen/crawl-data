import mysql.connector

class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="champions"
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS champions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                url TEXT,
                title VARCHAR(255),
                date VARCHAR(100),
                author VARCHAR(255),
                content TEXT,
                hashtag TEXT
            )
        """)

    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO champions(url, title, date, author, content, hashtag) 
            VALUES (%s, %s, %s, %s, %s, %ss)
        """, (item["url"], item["title"], item["date"], item["author"], 
              item["content"], item["hashtag"]))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# class MongoDBPipeline:
#     def open_spider(self, spider):
#         self.client = MongoClient("mongodb://localhost:27017/")
#         self.db = self.client["vnexpress"]
#         self.collection = self.db["hosophaan"]

#     def process_item(self, item, spider):
#         self.collection.insert_one(dict(item))
#         return item

#     def close_spider(self, spider):
#         self.client.close()

class TxtPipeline:
    def open_spider(self, spider):
        self.file = open("vnexpress_hosophaan.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        self.file.write(f"url: {item['url']}\n")
        self.file.write(f"title: {item['title']}\n")
        self.file.write(f"date: {item['time']}\n")
        self.file.write(f"author: {item['author']}\n")
        self.file.write(f"content: {item['content']}\n")
        self.file.write(f"hashtag: {item['tags']}\n")
        self.file.write("="*50 + "\n")
        return item

    def close_spider(self, spider):
        self.file.close()