# import requests

# Image ------------------

# cat = requests.get("https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962_square.jpg")
# dog = requests.get("https://www.youriowalawyers.com/images/blog/iStock-149075263.jpg")

# animal = input("Hayvon monini kiriting: ")

# if animal == "cat":
#     if cat.status_code == 200:
#         content = cat.content
#         with open("cat.jpg", "wb") as file:
#             file.write(content)
#             print("rasm yuklandi")

# elif animal == "dog":
#     if dog.status_code == 200:
#         content = dog.content
#         with open("dog.jpg", "wb") as file:
#             file.write(content)
#             print("rasm yuklandi")
# else:
#     print("Buday hayvon mavjud emas")


# cat -------------------

# url = "https://cataas.com/cat"
# response = requests.get(url)

# if response.status_code == 200:
#     content = response.content
#     # print(content)
#     with open("cat.jpg", "wb") as file:
#         file.write(content)
