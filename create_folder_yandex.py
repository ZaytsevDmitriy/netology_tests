import requests
import os.path


def get_headers():  # Запрос URL для загрузки
    if os.path.isfile('yandex_token.txt') is False:
        print('No token Yandex')
        exit()
    else:
        with open('yandex_token.txt', 'r') as file_objekt:
            YA_TOKEN = file_objekt.read().strip()
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(YA_TOKEN)
    }


def create_folder(folder_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources/"
    headers = get_headers()
    params = {"path": folder_name}
    request = requests.get(url=url, params=params, headers=headers)
    if request.status_code != 200:
        response = requests.put(url=url, params=params, headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print(f"Added new folder \"{folder_name}\"")
            return response.status_code




if __name__ == "__main__":

    create_folder('some_folder_name')