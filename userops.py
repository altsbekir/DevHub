import requests

class User():

    url = ""
    name = ""
    response = {}
    public_repo = int()
    followers = int()
    following = int()
    created_at = ""

    def __init__(self, user_id):
        self.user_id = user_id
        self.url = f"https://api.github.com/users/{user_id}"
        self.response = requests.get(self.url).json()
        self.name = self.response["name"]
        self.public_repo = self.response["public_repos"]
        self.followers = self.response["followers"]
        self.following = self.response["following"]
        self.created_at = self.response["created_at"][:4]

    def get_info(self):
        print("Id: ", self.user_id)
        print("Kullanıcı adı: ", self.name)
        print("Public Repo: ", self.public_repo)
        print("Takipçi: ", self.followers)
        print("Takip edilen: ", self.following)
        print("Oluşturulma tarihi: ", self.created_at)