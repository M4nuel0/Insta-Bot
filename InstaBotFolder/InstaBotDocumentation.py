from instabot import Bot 

bot = Bot()

#login
bot.login(username = "pizzicoli.jozef", password = "Pizzi.06")

#follow user
bot.follow("tonino.10078")

#follow users
bot.follow_users(["sarullo.manuel", "python"])         #you can insert a list of users

#unfollow the non followers
bot.unfollow_non_followers()

#upload an image
bot.upload_photo("pytube.jpg", caption = "There is a photo when i was a child")   #Insert the name of the file per first and then if you want, you can write a caption(ita = commento)

#send a message
bot.send_message("Hi man", "sarullo.manuel")      #For first insert the message and for second insert the username who the bot will send this message

#like a post
bot.like_user("callmebilaa", amount=3, filtration=False)


#comment
user_id = bot.get_user_id_from_username("callmebilaa")
media_id = bot.get_last_user_medias(user_id)
bot.comment(media_id[0], "Wake up")

#Get list of follower of anyone
follower_list = bot.get_user_followers("sarullo.manuel")   #Who follow an account(ita = followers)

following_list = bot.get_user_following("sarullo.manuel")  #Who an account follow(ita = seguiti)

for follower in follower_list:
    print(bot.get_username_from_user_id(follower))  #To get a list of follower of an account, do the same for the following_list


#To exit by the account
bot.logout()




