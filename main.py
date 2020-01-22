import time
import vk_api
import xlwt
from config import POSTS_COUNT, GROPS_COUNT
from datetime import datetime, timezone


def get_groups_id(word):
    res = vk.method('groups.search', {
        'q': word,
        'count': GROPS_COUNT,
    })
    res = [x['id'] for x in res['items']]
    return res

def get_comments_search(vk, query):
    res_comments = []
    semantics = query.split()
    for word in semantics:
        groups_id = get_groups_id(word=word)
        for group_id in groups_id:
            try:
                wall = vk.method('wall.get', {'owner_id': -group_id, 'count':POSTS_COUNT})
                for post in wall['items']:
                    comments = vk.method('wall.getComments', {'owner_id': -group_id, 'post_id': post['id']})
                    if comments['count'] > 0:
                        comments_items = [comment for comment in comments['items'] if 'text' in comment]
                        for c in comments_items:
                            dt = datetime.utcfromtimestamp(c['date']).astimezone(timezone.utc).isoformat()
                            res = {
                                'text':c['text'],
                                'date':dt,
                                'type':'VK',
                                'source':{
                                        'id':c['id'],
                                        'from_id':c['from_id'],
                                        'post_id':c['post_id'],
                                        'owner_id':c['owner_id'],
                                    }
                            }
                            res_comments.append(res)
            except:
                pass
    return res_comments

def auth_vk(login, password):
    vk = vk_api.VkApi(login=login, password=password)
    vk.auth()
    return vk

def write_res(res_comments):
    i = 0
    for x in res_comments:
        print(x)

if __name__ == '__main__':
    vk = auth_vk('79057111710','mambo1005')
    res_comments = get_comments_search(vk, 'похудеть')
    write_res(res_comments)