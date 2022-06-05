import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token="aa55f257c441a278c01229267bb4a2f5e621126301f2967c12da1742500a4e31175d0ba03d3bf9bdb0074")
vk = session.get_api()

urls = ['photo-213733674_457239018', 'photo-213733674_457239019', 'photo-213733674_457239020',
        'photo-213733674_457239021', 'photo-213733674_457239022', 'photo-213733674_457239023',
        'photo-213733674_457239024', 'photo-213733674_457239025', 'photo-213733674_457239026',
        'photo-213733674_457239027']

def send_message(user_id, message):
    session.method("messages.send", {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    })
def send_photo(user_id, url):
    session.method("messages.send", {
        "user_id": user_id,
        "attachment": url,
        "random_id": 0
    })

for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        
        if text == "старт":
            while True:
                g = False
                url_id = []
                for i in range(5):
                    url_id.append(urls[random.randint(0,9)])
                url_id.sort()
                for i in range(4):
                    if url_id[i] == url_id[i+1]:
                        g = True
                if not g:
                    break
                
            send_photo(user_id, url_id[0])
            send_photo(user_id, url_id[1])
            send_photo(user_id, url_id[2])
            send_photo(user_id, url_id[3])
            send_photo(user_id, url_id[4])
            
