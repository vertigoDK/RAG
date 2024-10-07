import requests
from bs4 import BeautifulSoup
import os

urls = [
    "https://pushkinlibrary.kz/ru/homeru/historyru.html",
    "https://pushkinlibrary.kz/ru/homeru/aboutru.html",
    "https://pushkinlibrary.kz/ru/homeru/pravila.html",
    "https://pushkinlibrary.kz/ru/homeru/putevodrus.html",
    "https://pushkinlibrary.kz/ru/homeru/press-about-us.html",
    "https://pushkinlibrary.kz/ru/homeru/guestbookru.html",
    "https://pushkinlibrary.kz/ru/homeru/grafik.html",
    "https://pushkinlibrary.kz/ru/homeru/cont-ru.html",
    "https://pushkinlibrary.kz/ru/servicesru/stat-shitatelem.html",
    "https://pushkinlibrary.kz/ru/servicesru/virkespravka.html",
    "https://pushkinlibrary.kz/ru/servicesru/eddru.html",
    "https://pushkinlibrary.kz/ru/servicesru/prodlit-knigu.html",
    "https://pushkinlibrary.kz/ru/servicesru/zapis-na-kursy.html",
    "https://pushkinlibrary.kz/ru/servicesru/advacat.html",
    "https://pushkinlibrary.kz/ru/servicesru/kruzhki-i-kluby.html",
    "https://pushkinlibrary.kz/ru/resursy/raritety.html",
    "https://pushkinlibrary.kz/ru/resursy/virt-expo.html",
    "https://pushkinlibrary.kz/ru/resursy/birelbikitapru.html",
    "https://pushkinlibrary.kz/ru/resursy/ru-newbooks.html",


]

# Функция для парсинга и сохранения текста в файл
def save_page_content(url, folder="data"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлечение текста со страницы
    content = soup.get_text(separator="\n")

    # Генерация имени файла на основе ссылки
    file_name = url.split("/")[-1].replace(".html", "") + ".txt"

    # Проверка существования папки для хранения файлов
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Сохранение текста в файл
    file_path = os.path.join(folder, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Сохранено: {file_path}")

# Парсим и сохраняем все страницы
for url in urls:
    save_page_content(url)
