import requests, json, time
from PhotoDBManager import PhotoDBManager

VKuser = 0 #ID account
VKtoken = ''

URL = 'https://api.vk.com/method/photos.getAll?v=5.194'

# Create a list of links to photos
def get_photos_list(offset=0, count=20):
    response = requests.get(URL,    
        params={
            'owner_id': VKuser,
            'access_token': VKtoken,
            'offset': offset,
            'count': count,
            'photo_sizes': 0
        })
    photos_list = response.json()     # an array of requests.get data
    count_photos = photos_list['response']['count']     # total photos counter
    photo_url = []      # list of links to photos
    if offset >= count_photos:         # Limit photos
        return photo_url
    for file in photos_list['response']['items']:
        list_sizes = file['sizes']  # we get lists of sizes and references to these sizes
        list_sizes_sorted = sorted(list_sizes, key=lambda d: d['height'])  # sort the sizes in ascending order
        file_url = list_sizes_sorted[-1]['url']  # select the link with the highest size
        photo_url.append(file_url) # add to the list of links to photos
    else:
        time.sleep(0.5)
        return photo_url + get_photos_list(offset+count, count)    # add "count" to the "offset"

# Function saves photos
def save_photos():
    photos_list = get_photos_list()    # getting a list of links to photos
    for file in photos_list:
        filen = file.split("/")[-1]            # pull the filename
        filename = filen.split("?size")[0]     # from the links
        api = requests.get(file)   # query the links from the list of links to photos
        
        # make a request to save the photo to the database
        sql.upload_photo(filename, api.content)  # in the request we send the name of the photo and the binary code of the photo. 
                                                 # the encoding standard is Base64


# Function saves data from the database to a TXT file
def sql_data_output():
    data = []
    querys=["timestamp", "filename"]
    if not data:
        result = sql.select(columns=querys, field=None, value=None)
    else:
        result = []
        for value in data:
            result.append(sql.select(columns=querys, field="id", value=value))
    with open('text.txt', 'w', encoding='utf-8') as my_file:
        my_file.write('\n'.join(str(tup) for tup in result))

# Function deletes data from the database table by line(if "data" is empty, it deletes all data)
def sql_delete_data():
    data = []
    if not data:
        sql.delete_data(field=None, value=None)
    else:
        for value in data:
            sql.delete_data(field="id", value=value)


sql = PhotoDBManager('db_photos.db', tablename="photos1")  # Call the "PhotoDBmanager" class, set the database name and the table name
sql.create_table_photo()

save_photos()

sql.close()