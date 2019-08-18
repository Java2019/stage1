import os
import speech_recognition as sr
import sys
import webbrowser


def talk(words):
     os.system("echo " + words + "| RHVoice-test -p Elena")


def comand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language='ru_RU').lower()
        print(task)
    except sr.UnknownValueError:
        # talk('Я вас не поняла.')
        task = comand()
    return task


def makesomthing(task: str):
    if 'открой сайт' in task:
        sitename = task.partition('открой сайт')[2].strip()
        url = 'http://' + sitename
        webbrowser.open(url)
    elif 'стоп' in task:
        sys.exit()
    elif 'привет' in task:
        talk('привет')
    elif 'проверить почту' in task:
        url = 'https://mail.yandex.ru/?uid=13617957#inbox'
        webbrowser.open(url)
    elif 'facebook' in task:
        url = 'https://facebook.com'
        webbrowser.open(url)
    elif 'skype' in task:
        url = 'https://web.skype.com/'
        webbrowser.open(url)
    elif 'пока' in task:
        talk('пока')
    elif 'спокойной ночи' in task:
        talk('спокойной ночи')

while True:
    makesomthing(comand())
