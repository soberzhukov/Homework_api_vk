import requests

class User:
    URL = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token':self.token,
            'v':self.version
        }
        self.owner_id = requests.get(self.URL+'users.get', self.params).json()['response'][0]['id']


    def mutual_friends(self, other_user):
        METOD = 'friends.getMutual'
        params = {
            'access_token': token,
            'v': self.version,
            'source_uid': self.owner_id,
            'target_uid': other_user.owner_id
        }
        resp = requests.get(self.URL+METOD, params=params)
        resp.raise_for_status()
        return resp.json()['response']


    def __and__(self, other):
        if not isinstance(other, User):
            return 'Это не класс User'
        else:
            list_users = [
                vk_1,
                vk_2,
                vk_3
            ]
            list_filter_user = []
            for user in list_users:
                if user.owner_id in self.mutual_friends(other):
                    list_filter_user.append(user)
                    return list_filter_user
                else:
                    return 'Нет общих друзей'

    def __str__(self):
        return f'vk.com/id{self.owner_id}'


if __name__ == '__main__':
    vk_1 = User(token, 5.126)
    vk_2 = User(token, 5.126)
    vk_3 = User(token, 5.126)

    print(vk_1.mutual_friends(vk_2))
    print(vk_1&vk_2)
    print(vk_1)
