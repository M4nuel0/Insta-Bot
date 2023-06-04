from instabot import Bot        #Pre-assembly library with functions which we can use in the program
import time
from os import system, name

bot = Bot(max_follows_per_day=200, max_messages_per_day=200)             #Take a name to the variable which will do the action in the program

time.sleep(2)
print("===============================================================================================")
print("  #######    ##     #     #####    #######     ######            #####       #####     #######") 
print("     #       # #    #     #           #        #    #            #    #     #     #       #   ")
print("     #       #   #  #     #####       #        ######            #  ##      #     #       #   ")
print("     #       #    # #         #       #        #    #            #    #     #     #       #   ")
print("  #######    #     ##     #####       #        #    #            #####       #####        #   ")
print("===============================================================================================")
time.sleep(2)

#Input for insert the username and the password
Username = input("\n\nInsert your Username: ")
print("===================================================================================================")
Password = input("Insert your Password: ")

#To login
bot.login(username = Username, password = Password, use_cookie = False)
time.sleep(10)

#To write at some peoples
def Writing():
    print("\n====================================================================================================")
    write_mode = input("Do you want use a list of users? Y/N: ").lower()
    
    if write_mode == "y" or write_mode == "yes":
        print("\n==========================================================================================================================================")
        what_method = str(input("INSERT THE METHOD: 1 = Write at the follower of a target user  |   2 = Write at the likers of a post of a target user: "))
        
        if what_method == "1":

            print("\n================================================================================================")
            user_name = str(input("Enter the target username: "))
            print("===================================================================================================")
            text_message = str(input("Insert the text of the message: "))
            print("=====================================================================================================")
            total_DMs = int(input("Enter the number of total DMs: "))
            follower_ids = bot.get_user_followers(user_name)

            for count, each_follower in enumerate(follower_ids):
        
                if count > total_DMs:
                    break

                username = bot.get_username_from_user_id(each_follower)
                bot.send_messages(text_message, [username])
                time.sleep(10)

            time.sleep(2)
            print("====================================================================================================")
            print("MESSAGES SENT")

        elif what_method == "2":

            print("\n================================================================================================")
            user_name = str(input("Enter the target username: "))
            print("===================================================================================================")
            text_message = str(input("Insert the text of the message: "))
            print("===================================================================================================")
            total_DMs = int(input("Enter the number of total DMs: "))

            likers_ids = bot.get_user_likers(user_name)

            for count, each_liker in enumerate(likers_ids):
    
                if count > total_DMs:   
                    break

                username =bot.get_username_from_user_id(each_liker)
                bot.send_messages(text_message, [username])
                time.sleep(10)

            time.sleep(2)
            print("=================================================================================================")
            print("MESSAGES SENT")

    elif write_mode == "n" or write_mode == "no":
        print("\n================================================================================================")
        who_write = input("Insert the usernames who i could write, Separated by a comma: ").split(",")
        time.sleep(1)
        print("================================================================================================")
        what_write = input("What i could write: ")
        bot.send_messages(what_write, who_write)    
        time.sleep(2)
        print("================================================================================================")
        print("MESSAGES SENT")

    else:
        print("\n====================================================================================================")
        print("PLEASE, ANOTHER TIME INSERT A CORRECT VALUE")
        time.sleep(2)
        _ = system('cls')
        Start()

#To get list of follower by an user
def GetFollower():
    print("\n=================================================================================================")
    who_getFollower = input("Insert the username who you want to get list of followers: ")
    list_follower = bot.get_user_followers(who_getFollower)
    time.sleep(2)
    for follower in list_follower:
        print(bot.get_username_from_user_id(follower))
    time.sleep(2)
    print("=================================================================================================")
    print("LIST COMPLETED")

#To get a list of following by an user
def GetFollowing():
    print("\n=================================================================================================")
    who_getFollowing = input("Insert the username who you want to get list of followings: ")
    list_following = bot.get_user_following(who_getFollowing)
    time.sleep(2)
    for following in list_following:
        print(bot.get_username_from_user_id(following))
    time.sleep(2)
    print("===================================================================================================")
    print("LIST COMPLETED")


#To comment a post by an user
def Comment():
    print("\n====================================================================================================")
    who_comment = input("Insert the username who you would to comment a post: ")
    user_id = bot.get_user_id_from_username(who_comment)
    print("======================================================================================================")
    number_media = int(input("Insert the number of the media which you would to comment: "))
    media_id = bot.get_last_user_medias(user_id, count=0)
    print("======================================================================================================")
    what_comment = input("Insert what you would to comment: ")
    bot.comment(media_id[number_media], what_comment)
    time.sleep(2)
    print("=====================================================================================================")
    print("COMMENT SENT")

 #To like a post by an user
def LikePost():
    print("\n========================================================================================================")
    who_like = input("Insert the username who you would to like a post: ")
    print("===========================================================================================================")
    number_post = int(input("How many post do you want to like: "))
    bot.like_user(who_like, number_post, filtration=False)
    time.sleep(2)
    print("========================================================================================================")
    print("LIKE SENT")


#To follow a list of users
def Follow():
    print("\n========================================================================================================")
    who_follow = input("Insert a list of users to follow, Separated by a comma: ").split(",")
    bot.follow_users(who_follow)
    time.sleep(2)
    print("=========================================================================================================")
    print("FOLLOWING COMPLETED")


#To upload a photo choose by the user
def UploadPhoto():
    print("\n==========================================================================================================")
    name_photo = input("Insert the name that the photo has in your drive: ")
    print("=========================================================================================================")
    what_caption = input("Insert the caption which you would to write in your photo: ")
    bot.upload_photo(name_photo, what_caption)
    time.sleep(2)
    print("=========================================================================================================")
    print("UPLOADING COMPLETED")


#To start the bot
def Start():
    #To choose the action which the bot will do
    print("\n\n===============================================================================================================")
    what_do = input("CHOOSE WHAT DO: Upload photo, Comment, Writing, Follow, Like post, Get following, Get follower: ").lower()
    if what_do == "upload photo":
        time.sleep(2)
        UploadPhoto()
    elif what_do == "comment":
        time.sleep(2)
        Comment()
    elif what_do == "writing":
        time.sleep(2)
        Writing()
    elif what_do == "follow":
        time.sleep(2)
        Follow()
    elif what_do == "like post":
        time.sleep(2)
        LikePost()
    elif what_do == "get following":
        time.sleep(2)
        GetFollowing()
    elif what_do == "get follower":
        time.sleep(2)
        GetFollower()
    else:                   #If the user insert an incorrect value
        print("\n======================================================================================================")
        print("ERROR, INSERT A CORRECT VALUE")
        time.sleep(2)
        _ = system('cls')
        Start()
    
    restart_Bot = input("\n\nDo you want to re-start the Bot, Y/N: ").lower()
    if restart_Bot == "y" or restart_Bot == "yes":           #Loop to start and re-start the Bot
        time.sleep(2)
        _ = system('cls')
        Start()
    elif restart_Bot == "n" or restart_Bot == "no":                   #To interrupt the Bot
        time.sleep(2) 
        print("\n=======================================================================================================")
        print("OKAY, THANKS FOR USING MY BOT")
        time.sleep(2)
        bot.logout()           #To logout by the account
        time.sleep(5)
        _ = system('cls')
    else:
        print("\n========================================================================================================")
        print("PLEASE, ANOTHER TIME INSERT A CORRECT VALUE")
        time.sleep(2)
        _ = system('cls')


#To START the entire Bot or program
Start()









