from aiogram.types import InlineQuery, InlineQueryResultPhoto
from loader import dp
from search_images import fetch_inline_search_images

# @dp.inline_query()
# async def inline_search(inline_query: InlineQuery):

#     try:
#         text = inline_query.query
#         photos = await fetch_inline_search_images(text, count=20)

#         results = [
#             InlineQueryResultPhoto(
#                 id=str(i),
#                 photo_url=img,
#                 thumbnail_url=img
#             )
#             for i, img in enumerate(photos)
#         ]

#         await inline_query.answer(results=results)

#     except Exception as e:
#         print(f"Xatolik: {e}")
