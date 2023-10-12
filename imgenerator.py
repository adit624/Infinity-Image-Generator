import os
import random
import time
#mengecek pibrary requests
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
#mengecek library fake_useragent
try:
    from fake_useragent import UserAgent
except ImportError:
    os.system("pip install fake_useragent")
    from fake_useragent import UserAgent

# Daftar bahasa yang akan digunakan
languages = ['en-US', 'es-ES', 'fr-FR', 'de-DE', 'it-IT']

author = """
T   I   |   O   L   |   A   E | B   | B   O   K   1   9
  H   S | T   O   S | M   D   |   Y |   J   R   I   9
"""
print(author)
print(" ")

# Fungsi untuk mengganti spasi dengan "%20"
def replace_space(image_prompt):
    return image_prompt.replace(" ", "%20")

# Fungsi untuk mengunduh gambar dari URL dan menyimpannya dengan nama yang sesuai
def download_image(image_prompt, output_folder):
    # Menggabungkan URL dengan image_prompt
    seed = str(random.randint(1, 9999999))
    image_prompt_encoded = replace_space(image_prompt)
    url = f"https://image.pollinations.ai/prompt/{image_prompt_encoded};seed={seed}.%204%20k%20resolution.width=1440&height=3200;HD,HQ;Ultra%20Detail"

    # Membuat user-agent acak
    user_agent = UserAgent().random

    # Membuat header untuk permintaan HTTP
    headers = {
        'User-Agent': user_agent,
        'Accept-Language': random.choice(languages)
    }

    # Mengirim permintaan GET ke URL dengan header yang telah dibuat
    response = requests.get(url, headers=headers)

    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        # Mengambil nama file dari URL
        file_name = os.path.join(output_folder, f"{image_prompt}.jpg")

        # Memeriksa apakah file dengan nama yang sama sudah ada
        count = 1
        while os.path.exists(file_name):
            # Jika sudah ada, tambahkan angka ke nama file
            file_name = os.path.join(output_folder, f"{image_prompt}_{count}.png")
            count += 1

        # Menyimpan gambar ke file
        with open(file_name, 'wb') as file:
            file.write(response.content)

        print(f"Gambar berhasil diunduh dan disimpan sebagai {file_name}")
        time.sleep(2)
    else:
        print(f"Gagal mengunduh gambar. Kode status: {response.status_code}")
        time.sleep(2)

# Folder tempat menyimpan gambar
output_folder = os.path.expanduser("~/storage/downloads/")

#input awal
input_main = input("Masukkan image_prompt (atau ketik 'exit' untuk keluar): ")
while True:
    # Input image_prompt
    image_prompt = input_main

    if image_prompt.lower() == 'exit':
        break

    # Memanggil fungsi download_image
    download_image(image_prompt, output_folder)
