import os


def talk(words):
    # engine = pyttsx3.Engine
    # voices = engine.getProperty(__name__)
    # for voice in voices:
    #     engine.setProperty('voice', voice.id)
    # engine.say('The quick brown fox jumped over the lazy dog.')
    # engine.runAndWait()
    # os.say("Hi, this is the Awesome Weather Service...", {"voice":"kate"})
    os.system("echo " + words + "| RHVoice-test -p Elena")


talk("Список голосовых профилей")
