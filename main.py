import time
import vk_api
import xlwt
from config import POSTS_COUNT, GROPS_COUNT


def get_groups_id(word):
    res = vk.method('groups.search', {
        'q': word,
        'count': GROPS_COUNT,
    })
    res = [x['id'] for x in res['items']]
    return res



token = '4ace47a59579e6b7dfe283d465ec8659cb87daf33af2e9a2c0a60f1651e413ce3ae5b02b2b5cd4d1e5f53'
vk = vk_api.VkApi(login='', password='')
vk.auth()


semantics = [
    'Похудеть',
    # 'Женский фитнес',
    # 'Фитнес для начинающих',
    # 'Набрать мышечную массу',
    # 'Пресс',
    # 'Ягодицы',
    # 'Руки',
    # 'Живот',
    # 'Ноги',
    # 'Восстановление после травм / лечебная физкультура',
]

res_comments = []

words_len = len(semantics)
words_complete = 0
print('###########################Start################################')
print(f'Сделано {words_complete} слов из {words_len}')
try:
    for word in semantics:
        groups_id = get_groups_id(word=word)
        groups_len = len(groups_id)
        groups_complete = 0
        for group_id in groups_id:
            wall = vk.method('wall.get', {'owner_id': -group_id, 'count':POSTS_COUNT})
            time.sleep(0.5)
            comments_len = len(wall['items'])
            comments_complete = 0
            for post in wall['items']:
                comments = vk.method('wall.getComments', {'owner_id': -group_id, 'post_id': post['id']})
                if comments['count'] > 0:
                    comments_text = [comment['text'] for comment in comments['items'] if 'text' in comment]
                    res_comments.append(comments_text)
                time.sleep(0.5)
                comments_complete += 1
                print(f'        Сделано {comments_complete} постов из {comments_len}')
            groups_complete += 1
            print(f'    Сделано {groups_complete} групп из {groups_len}')
        words_complete += 1
        print(f'Сделано {words_complete} слов из {words_len}')
except vk_api.ApiError:
    print('Access denied')
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Python Sheet 1")
print(len(res_comments))
i = 0
for x in res_comments:
    for z in x:
        if '?' in z:
            sheet1.write(i, 0, z)
            print(z)
            i += 1
book.save('test.xls')
print('###############################END################################')
