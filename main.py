import pyttsx3
import speech_recognition as sr
import spacy
from study import study
from colored import fg, attr

r = sr.Recognizer()

mic = sr.Microphone()

nlp = spacy.load("en_core_web_lg")

for index, records in study.items():

    question = records[0]
    answer = records[1]

    engine = pyttsx3.init()
    engine.say(question)
    engine.runAndWait()
    engine.stop()
    
    print("Listening now")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print("Done listening\n")

    audio_traslated = r.recognize_google(audio)
    print("Done Translating")
    nlp_answers = nlp(answer)
    nlp_user_answers = nlp(audio_traslated)

    similarity = nlp_answers.similarity(nlp_user_answers)

    if float(similarity) > 0.9:
        print("%sPASSED%s" % (fg(2), attr(1)), similarity)
    else:
        print("%sFAILED%s" % (fg(1), attr(0)), similarity)

    print("Q : " + question + "\n")
    print("A : " + answer + "\n")
    print("Your : " + audio_traslated + "\n")
