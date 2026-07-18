import requests

class User():

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

    def list_followers(self):
        followers_list = [dict["login"] for dict in requests.get(f"{self.url}/followers").json()]
        for follower in followers_list:
            follower_obj = User(follower)
            print(f"{followers_list.index(follower) + 1}. {follower} ({follower_obj.name})")

    def list_following(self):
        following_list = [dict["login"] for dict in requests.get(f"{self.url}/following").json()]
        for following in following_list:
            following_obj = User(following)
            print(f"{following_list.index(following) + 1}. {following} ({following_obj.name})")

    def list_repos(self):
        for (ix, repo) in enumerate(requests.get(f"{self.url}/repos").json()):
            print(f"{ix + 1}. {repo["name"]} ({repo["stargazers_count"]} stars.)")