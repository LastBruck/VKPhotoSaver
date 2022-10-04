from PhotoDBManager import PhotoDBManager

import requests, json, time

VKuser = 0 #ID account
VKtoken = ''

URL = 'https://api.vk.com/method/photos.getAll?v=5.194'

def get_photo_list(offset=0, count=20):
    """ Create a list of links to photos

    Args:
        offset (int, optional): _description_. Defaults to 0.
        count (int, optional): _description_. Defaults to 20.

    Returns:
        _type_: _description_
    """
    response = requests.get(URL,    
        params={
            'owner_id': VKuser,
            'access_token': VKtoken,
            'offset': offset,
            'count': count,
            'photo_sizes': 0
        })
    photos_list = response.json()
    count_photos = photos_list['response']['count']
    photo_url = []
    if offset >= count_photos:
        return photo_url
    for file in photos_list['response']['items']:
        list_sizes = file['sizes']
        list_sizes_sorted = sorted(list_sizes, key=lambda d: d['height'])
        file_url = list_sizes_sorted[-1]['url']
        photo_url.append(file_url)
    else:
        time.sleep(0.5)
        return photo_url + get_photo_list(offset+count, count)

def save_photos():
    """ Function saves photos
    """
    photos_list = get_photo_list()
    name = []
    for file in photos_list:
        filen = file.split("/")[-1]
        filename = filen.split("?size")[0]
        name.append(filename)
        api = requests.get(file)
        
        # save_on_pc(name, filename, api.content)
        sql.upload_photo(filename, api.content) 

def sql_data_output():
    """ Function saves data from the database to a TXT file
    """
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


def sql_delete_data():
    """ Function deletes data from the database table by line(if "data" is empty, it deletes all data)
    """
    data = []
    if not data:
        sql.delete_data(field=None, value=None)
    else:
        for value in data:
            sql.delete_data(field="id", value=value)


def save_on_pc(name, filename, photo):
    """ Function saves photos on PC

    Args:
        name (list): list of names for numbering each file
        filename (str): file name
        photo (bytes): photo binary code
    """
    num_file = enumerate(name, 1)
    for num in num_file:
        num
    number = num[0]
    with open(f"data/{number}_%s" % filename, "wb") as file:
        file.write(photo)


sql = PhotoDBManager('db_photos.db', tablename="photos1")
sql.create_table_photo()

save_photos()

sql.close()