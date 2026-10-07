import speech_recognition as sr
import pyttsx3


def listen_to_speech():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        text = recognizer.recognize_google(audio)

        return text

    except sr.WaitTimeoutError:

        return "No speech detected."

    except sr.UnknownValueError:

        return "Could not understand the speech."

    except sr.RequestError:

        return "Speech recognition service is unavailable."

    except Exception as e:

        return f"Microphone error: {str(e)}"


def speak_text(text):

    try:

        engine = pyttsx3.init()

        engine.setProperty(
            "rate",
            165
        )

        engine.setProperty(
            "volume",
            1.0
        )

        engine.say(text)

        engine.runAndWait()

    except Exception as e:

        print("Text-to-speech error:", e)