from instabot import Bot
import time

bot = Bot()

time.sleep(2)
print("===============================================================================================")
print("  #######    ##     #     #####    #######     ######            #####       #####     #######") 
print("     #       #  #   #     #           #        #    #            #    #     #     #       #   ")
print("     #       #   #  #     #####       #        ######            #  ##      #     #       #   ")
print("     #       #    # #         #       #        #    #            #    #     #     #       #   ")
print("  #######    #     ##     #####       #        #    #            #####       #####        #   ")
print("===============================================================================================")
time.sleep(2)

#Insert the username of the user who you want to give a list of following
who_user = input("Insert the username of the user, who you want to give list of following: ")
print("=======================================================================================")
time.sleep(1)

#For start the entire program
def Start():
    #Insert the datas for login
    Username = input("Insert your username: ")
    time.sleep(1)
    print("===============================================================")
    Password = input("Insert your password: ")
    #To login
    bot.login(username = Username, password = Password, use_cookie = False)
    time.sleep(10)

    #For take user following
    list_following = bot.get_user_following(who_user)
    time.sleep(5)
    print("===============================================================")
    
    #For print on the screen the following list of the target user
    for following in list_following:
        print(bot.get_username_from_user_id(following))
        time.sleep(2)

    print("================================================================")
    print("LIST COMPLETED")


Start()

    








