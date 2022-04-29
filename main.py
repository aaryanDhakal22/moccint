import pyttsx3
import speech_recognition as sr
import spacy
from study import study
from colored import fg, attr

r = sr.Recognizer()

mic = sr.Microphone()

nlp = spacy.load("en_core_web_lg")

audio_answers = []
audio_to_voice_answers = []
for index,question in study.items():

    Qs = question[0]
    As = question[1]

    engine = pyttsx3.init()
    engine.say(Qs)
    engine.runAndWait()

    print("Listening now")

    with mic as source :
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    audio_answers.append([Qs,As,audio])
    print("\nDone listening")
    if index == "03":
        break

for records in audio_answers:
    audio_traslated = r.recognize_google(records[2])
    audio_to_voice_answers.append([records[0],records[1],audio_traslated])
    real_answers = nlp(records[1])
    user_answers = nlp(audio_traslated)

    similarity = real_answers.similarity(user_answers)

    if float(similarity) > 0.9 :
        print("%sPASSED%s"%(fg(2),attr(0)),similarity)
    else:
        print("%sFAILED%s"%(fg(1),attr(0)),similarity)


for item in audio_to_voice_answers:
    print("Q : "+item[0]+"\n")
    print("A : "+item[1]+"\n")
    print("Your : "+item[2]+"\n")