from instabot import Bot

bot = Bot(max_messages_per_day=200, max_follows_per_day=200)

user_name = str(input("Enter the target username: "))
total_DMs = int(input("Enter the number of total DMs: "))

#login
bot.login(username = "", password = "", use_cookie = False)

#method 1
#Dm follower of a target user
follower_ids = bot.get_user_followers(user_name)

for count, each_follower in enumerate(follower_ids):
    
    if count > total_DMs:
        break

    bot.follow(each_follower)
    text_message = "Hello bro"
    username =bot.get_username_from_user_id(each_follower)
    bot.send_messages(text_message, [username])



#Method 2
#DM likers of a target user
likers_ids = bot.get_user_likers(user_name)

for count, each_liker in enumerate(likers_ids):
    
    if count > total_DMs:   
        break

    bot.follow(each_liker)
    text_message = "Hello bro"
    username =bot.get_username_from_user_id(each_liker)
    bot.send_messages(text_message, [username])






