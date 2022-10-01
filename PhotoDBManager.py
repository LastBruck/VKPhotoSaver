import datetime
from SQLiteManager import SqliteManager

class PhotoDBManager(SqliteManager):
    def create_table_photo(self):
        # Field names and types for a table in the database
        __fields = {
            "timestamp":"integer", 
            "filename":"text", 
            "photo":"blob"
        }
        self.create_table(fields = __fields)

    def upload_photo(self, filename = str, photo = bytes):
        current_time = datetime.datetime.now()
        time_stamp = current_time.timestamp()
        data = {
                "timestamp":time_stamp,
                "filename":filename, 
                "photo":photo
            }
        is_file_exists = self.contains(checkfield="photo", value=photo)
        if is_file_exists is False:
            self.insert(data=data)
