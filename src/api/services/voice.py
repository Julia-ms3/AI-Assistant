import speech_recognition as speech


async def setup_voice():
    rec = speech.Recognizer()
    with speech.Microphone(device_index=0) as source:
        rec.adjust_for_ambient_noise(source, duration=1)
        print("say something: ")
        audio = rec.listen(source)
    try:
        txt = rec.recognize_google(audio, language='uk')
        return txt

    except Exception as e:
        print(e)
