import speech_recognition as sr

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Capturar audio desde el micrófono
with sr.Microphone() as source:
    print("Di algo...")
    audio = recognizer.listen(source)

# Reconocer el texto en el audio
try:
    text = recognizer.recognize_google(audio)
    print("Texto reconocido: " + text)
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print("Error en la solicitud al servicio de reconocimiento: {0}".format(e))