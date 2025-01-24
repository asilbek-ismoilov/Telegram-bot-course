import requests

def cat_img():
    url = "https://cataas.com/cat"
    response = requests.get(url)

    if response.status_code == 200:
        return response.content
    else:
        return "Xatolik qaytardi !"


# def cat_gif():
#     url = "https://cataas.com/cat/gif"

#     response = requests.get(url)

#     if response.status_code == 200:
#         mushuk_gif = response.content
#         return mushuk_gif
#     else:
#         return "Xatolik yuz berdi!"


# def cat_tag_text(tag, text):
#     # URL manzilini matn bilan dinamik yaratamiz
#     url = f"https://cataas.com/cat/{tag}/says/{text}"

#     response = requests.get(url)

#     if response.status_code == 200:
#         mushuk_rasm = response.content
#         return mushuk_rasm
#     else:
#         return "Xatolik yuz berdi!"