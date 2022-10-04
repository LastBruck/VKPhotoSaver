import datetime
from SQLiteManager import SqliteManager

class PhotoDBManager(SqliteManager):
    def create_table_photo(self):
        """ The function creates a table with fields and their types specified in the class
        """
        __fields = {
            "timestamp":"integer", 
            "filename":"text", 
            "photo":"blob"
        }
        self.create_table(fields = __fields)

    def upload_photo(self, filename = str, photo = bytes):
        """ The function creates a "timestamp", checks each photo against a binary code for recurrence in the database, and if there is no recurrence, it sends the data to the database for recording

        Args:
            filename (str, optional): _description_. Defaults to str.
            photo (bytes, optional): _description_. Defaults to bytes.
        """
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
