from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import pyttsx3
import speech_recognition
import  threading

# Create a chatbot instance
bot=ChatBot('Bot')

# Create a trainer for deep learning training
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot using ChatterBot's English corpus
trainer.train('chatterbot.corpus.english')

# Train the chatbot using custom data
trainer=ListTrainer(bot)
for files in os.listdir('data/english/'):
    data=open('data/english/'+files,'r',encoding='utf-8').readlines()

    #trainer.train(data_list)
    trainer.train(data)

def botReply():
    question = questionField.get()
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END, 'You: ' + question + '\n\n')
    textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0, END)

def errorBotReply():
    root.destroy()
    import updated_qustion

def logoutBot():
    root.destroy()

def audioToText():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)


                questionField.delete(0,END)
                questionField.insert(0,query)
                botReply()

        except Exception as e:
            print(e)
root=Tk()

root.geometry('500x570+100+30')
root.title('ChatBot created by Basil')
root.config(bg='firebrick1')

logoPic=PhotoImage(file='logo11.png')


logoPicLabel=Label(root,image=logoPic,bg='firebrick1')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

errorPic=PhotoImage(file='ERV1.png')


errorButton=Button(root,image=errorPic, command=errorBotReply)
errorButton.pack(side='left', padx=10, pady=10)

askPic=PhotoImage(file='ask12.png')


askButton=Button(root,image=askPic,command=botReply)
askButton.pack(side='left', padx=10, pady=10)

logoutPic=PhotoImage(file='logout.png')


logoutButton=Button(root,image=logoutPic, command=logoutBot)
logoutButton.pack(side='left', padx=10, pady=10)

def click(event):
    askButton.invoke()
    errorButton.invoke()


root.bind('<Return>',click)


thread=threading.Thread(target=audioToText)
thread.setDaemon(True)
thread.start()
root.mainloop()