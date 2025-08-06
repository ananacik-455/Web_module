# Імітуйте 3 асинхронні "API-виклики", кожен з яких має випадкову
# затримку від 0.5 до 2.0 секунд. Використайте `asyncio.gather()`
# для їх конкурентного виконання. Виведіть загальний час виконання.

import random
import datetime
import asyncio
import time
import aiohttp
#
# async def fetch_url(url):
#     print(f'[{datetime.datetime.now().strftime('%H:%M:%S')}] Start downloading data from {url}')
#     await asyncio.sleep(random.uniform(0.5, 2.5))
#     data = f"Data from {url}"
#     print(f'[{datetime.datetime.now().strftime('%H:%M:%S')}] End downloading data from {url}')
#     return data
#
# urls = [
#     "http://example.com/page1",
#     "http://example.com/page2",
#     "http://example.com/page3",
#     "http://example.com/page4",
# ]
#
# async def main():
#     start = time.perf_counter()
#     result = await asyncio.gather(*[fetch_url(url) for url in urls])
#     end = time.perf_counter()
#     print(f"Total spent time: {end - start:.3f}")
#     print(f"Result: {result}")
#
# if __name__ == '__main__':
#     asyncio.run(main())

# Створіть асинхронну функцію `get_post_and_comments(session, post_id)`,
# яка одночасно (конкурентно) отримує дані про пост та всі його коментарі з JSONPlaceholder.
# URL для поста: `https://jsonplaceholder.typicode.com/posts/{post_id}`
# URL для коментарів: `https://jsonplaceholder.typicode.com/posts/{post_id}/comments`
# Виведіть заголовок поста та кількість коментарів.

# async def get_post_and_comments(session, post_id):
#     post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#     comments_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
#
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Завантажую пост {post_id} та коментарі...")
#     try:
#         # Запускаємо обидва запити конкурентно
#         post_response, comments_response = await asyncio.gather(
#             session.get(post_url),
#             session.get(comments_url)
#         )
#
#         post_response.raise_for_status()
#         comments_response.raise_for_status()
#
#         post_data = await post_response.json()
#         comments_data = await comments_response.json()
#
#         print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Пост {post_id} та коментарі завантажено.")
#         return {
#             "post_id": post_id,
#             "post_title": post_data,
#             "comments_count": comments_data
#         }
#     except aiohttp.ClientError as e:
#         print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Помилка завантаження поста {post_id} або коментарів: {e}")
#         return {"post_id": post_id, "error": str(e)}
#
# async def main_task_7():
#     print("Запускаю Завдання 7 (отримання постів та коментарів)...")
#     # post_ids = [1, 2, 3, 999] # Додамо неіснуючий ID для тестування помилки
#     start_time = time.perf_counter()
#
#     async with aiohttp.ClientSession() as session:
#         tasks = [get_post_and_comments(session, pid) for pid in range(1, 11)]
#         results = await asyncio.gather(*tasks)
#
#     end_time = time.perf_counter()
#     print(f"Всі запити Завдання 7 завершено за {end_time - start_time:.2f} секунд.")
#     print("Отримані результати:")
#     for res in results:
#         if "post_title" in res:
#             print(f"  - Пост ID: {res['post_id']}, Заголовок: '{res['post_title']}', Коментарів: {res['comments_count']}")
#         else:
#             print(f"  - Помилка для поста {res['post_id']}: {res['error']}")
#
# asyncio.run(main_task_7())

async def get_post_and_comments(session, post_id):
    post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    post_comment_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"

    try:

        post_response, comments_response = await asyncio.gather(
            session.get(post_url),
            session.get(post_comment_url)
        )

        post_response.raise_for_status()
        comments_response.raise_for_status()

        post_data = await post_response.json()
        comments_data = await comments_response.json()

        return {"title": post_data["title"], "num_post_comments": len(comments_data)}

    except aiohttp.ClientError as e:
        print(e)
        return {"title": "", "num_post_comments": 0}

async def main():
    ids = list(range(1, 11))
    ids.append(999)
    async with aiohttp.ClientSession() as session:
        tasks = [get_post_and_comments(session, id_) for id_ in ids]
        responses = await asyncio.gather(*tasks)
    # print(responses)

    for response in responses:
        print(response, "\n")

if __name__ == "__main__":
    asyncio.run(main())