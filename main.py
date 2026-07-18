from userops import User

def get_choice():
    print("Bir eylem seçin: ")
    print("1 - Takipçileri listele.")
    print("2 - Takip edilenleri listele.")
    print("3 - Repoları listele.")
    print("4 - Kullanıcıdan çık.")
    print("5 - Programdan çık.")
    choice = int(input("Seçiminiz: "))
    return choice

while True:

    try:

        newUser = User(input("Kullanıcı adını girin: "))
        newUser.get_info()

        while True:
            choice = get_choice()
            if choice == 1: newUser.list_followers()
            elif choice == 2: newUser.list_following()
            elif choice == 3: newUser.list_repos()
            elif choice == 4: break
            elif choice == 5: exit()
            else: print("(1 - 5) arasında bir seçim yapın")

    except Exception as e:
        print("Hata! ", e)