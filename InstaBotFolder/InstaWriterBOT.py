from instabot import Bot
import time

bot = Bot()

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
Username = input("Insert your Username: ")
print("=============================================")
Password = input("Insert your Password: ")

#To login
bot.login(username = Username, password = Password, use_cookie = False)
time.sleep(10)

#To write at some peoples
def Writing():
    who_write = input("Insert the usernames who i could write, Separated by a comma: ").split(",")
    what_write = input("What i could write: ")
    bot.send_messages(what_write, who_write)    
    time.sleep(2)
    print("================================================================================================")
    print("WRITING COMPLETED")

#For start the function Writing
Writing()

#To logout by the account
bot.logout()
    
