class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscriptions = subscriptions
        self.subscribers = subscribers

    def subscribe(self, user):
        user.subscribers += 1
        user.username = self.username  
        self.subscriptions += 1

user1 = Youtube("Elshad")
user2 = Youtube("Renad")
user2.subscribe(user2)
print(user1.subscribers)  
print(user1.username)
print(user2.username)  
print(user1.subscriptions)  
print(user2.subscribers)  
print(user2.subscriptions)  
