import requests
import os
from pprint import pprint

class YandexDissk:
    def __init__(self, token):
        self.token = token
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("этот_файлик_загрузился")
    def concenttrator(self):
        list_of_files_to_send_to_yandex = []
        for files in os.listdir():
            if files.endswith(('.txt', '.idea', '.py')):
                pass
            else:
                list_of_files_to_send_to_yandex.append(files)
        return list_of_files_to_send_to_yandex
    def upload_all(self):
        """Метод загружает файлы по списку из папки с с файлом питона на яндекс диск"""
        send_list = self.concenttrator()
        for sending_files in send_list:
            print(f"Вижу файл_C_uMEHEM_>>>>{sending_files}___ух как загружу его сейчас...")
            ya.upload_file_to_disk(sending_files, sending_files)


if __name__ == '__main__':
    TOKTOK = "__ТУТ__ТОКЕН___БЫЛ___AQAаA0heSk4BvпPu6IdGRуYf1I"
    ya = YandexDissk(token=TOKTOK)
    ya.upload_all() загружает все что есть в папке с ПИТОН-файлом в яндекс диск при наличии поставленного токена в токток переменную