import requests
from tkinter import *  #import GUI



root = Tk()
root.title("DiscordWebhookMessage")#window title name
root.geometry("600x150+50+50")#window size
root.resizable(False,False)#control resize window set






label1 = Label(root, text="    ")
label1.grid(row=2,column=1)
label2 = Label(root, text="    ")
label2.grid(row=4,column=1)



labelDWU = Label(root, text="[Didcord Webhook Url]\n ex)https://discord.com/api/webhooks/...")
labelDWU.grid(row=1,column=2)
hookurl = Entry(root,width=70)
hookurl.grid(row=2,column=2)




labelMS = Label(root, text="[Message]")
labelMS.grid(row=3,column=2)
messageLine = Entry(root,width=70)
messageLine.grid(row=4,column=2)







def sendwebhook():
    headers = {
        'Content-Type': 'application/json',
    }
    json_data = {
        'content': messageLine.get(),
    }

    response = requests.post(hookurl.get(), headers=headers, json=json_data)


sendcomm = Button(root,text="Send",command=sendwebhook)
sendcomm.grid(row=4,column=3)





root.mainloop()#close window set