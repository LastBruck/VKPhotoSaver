# VKPhotoSaver
Данная программа написана на языке **Python 3.10**


Предназначена для сохранения **всех** фотографий из личного профилья **vk.com** с самым высоким доступным разрешением в базу данных **SQlite3**.


> Перед тем как начать работать c приложением - ознакомьтесь с [**Документацией VK**](https://dev.vk.com/api/getting-started)


### Для работы вам понадобится:
- Создать Standalone-приложение ВК.
- Подтвердить доступ приложения к фотографиям аккаунта 
```bash 
  https://oauth.vk.com/authorize?client_id=ID_ПРИЛОЖЕНИЯ&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.194
```
- После получения доступа, из сгенерированного URL скопировать ключ, он идёт после **"access_token="** и до **"&expires_in"**, и вставить в приложении в **VKtoken**. (Данный ключ работает 24 часа)


Приложение находится в файле **"VKPhotoSaver.py"**, а так же созданы 2 файла с классами **"SQLiteManager.py"** и **"PhotoDBManager.py"** для работы с SQL.
