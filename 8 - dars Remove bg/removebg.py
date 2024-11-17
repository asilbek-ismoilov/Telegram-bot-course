import requests
from io import BytesIO

# Orqa fonga rasm qo'yish
def bg_add_pic(Bg_pic_url, FILE_NAME):
    rasm = ''
    API_KEY = 'pLDBBi1Y56s8HkBUdQZg47Tp'

    # Bg_pic_url dan rasmni yuklab olish
    bg_image_response = requests.get(Bg_pic_url)

    if bg_image_response.status_code == 200:
        # Rasmni yuklab olib, xotirada ochish
        bg_image_file = BytesIO(bg_image_response.content)

        # remove.bg API'ga rasmni yuborish
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            data={
                'image_url': FILE_NAME,
                'size': 'auto',
            },
            files={'bg_image_file': ('image.jpg', bg_image_file)},
            headers={'X-Api-Key': API_KEY},
        )

        if response.status_code == requests.codes.ok:
            rasm = response.content
        else:
            print("Error:", response.status_code, response.text)
    else:
        print("Error loading background image:", bg_image_response.status_code)

    return rasm


# Orqa fonni o'chirish
def remove_bg(FILE_NAME):
    rasm=''
    API_KEY ='pLDBBi1Y56s8HkBUdQZg47Tp'

    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': FILE_NAME,
        'size': 'auto',
    },
    headers={'X-Api-Key': API_KEY},
)
    if response.status_code == requests.codes.ok:
        rasm = response.content
    else:
        print("Error:", response.status_code, response.text)
    return rasm

# Orqafonga rang qo'shish
def remove_bg_color(FILE_NAME, color="white"):
    rasm=''
    API_KEY ='pLDBBi1Y56s8HkBUdQZg47Tp'

    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': FILE_NAME,
        'size': 'auto',
        'bg_color': color
    },
    headers={'X-Api-Key': API_KEY},
)
    if response.status_code == requests.codes.ok:
        rasm = response.content
    else:
        print("Error:", response.status_code, response.text)
    return rasm