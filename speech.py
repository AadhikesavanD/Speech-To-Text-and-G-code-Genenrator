import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the index for the Bluetooth microphone
bluetooth_microphone_index = int(input("Enter the index of your Bluetooth microphone: "))

# Function to convert text to speech
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

# G-code dictionary for alphabet drawing (A-Z)
gcode_alphabet = {
    "a": ["G00 X0 Y0", "G01 X5 Y15", "G01 X10 Y0", "G00 X2 Y7", "G01 X8 Y7"],  # A
    "b": ["G00 X0 Y0", "G01 X0 Y15", "G01 X5 Y15", "G01 X10 Y10", "G01 X5 Y5", "G01 X0 Y5"],  # B
    "c": ["G00 X10 Y15", "G01 X0 Y15", "G01 X0 Y0", "G01 X10 Y0"],  # C
    "d": ["G00 X0 Y0", "G01 X0 Y15", "G01 X5 Y15", "G01 X10 Y10", "G01 X5 Y0"],  # D
    "e": ["G00 X10 Y15", "G01 X0 Y15", "G01 X0 Y0", "G01 X10 Y0", "G00 X0 Y7", "G01 X8 Y7"],  # E
    "f": ["G00 X10 Y15", "G01 X0 Y15", "G01 X0 Y7", "G01 X8 Y7"],  # F
    "g": ["G00 X10 Y15", "G01 X0 Y15", "G01 X0 Y0", "G01 X10 Y0", "G01 X10 Y7", "G01 X5 Y7"],  # G
    "h": ["G00 X0 Y0", "G01 X0 Y15", "G00 X10 Y0", "G01 X10 Y15", "G00 X0 Y7", "G01 X10 Y7"],  # H
    "i": ["G00 X5 Y15", "G01 X5 Y0", "G00 X2 Y15", "G01 X8 Y15", "G00 X2 Y0", "G01 X8 Y0"],  # I
    "j": ["G00 X10 Y15", "G01 X10 Y0", "G01 X5 Y0", "G01 X0 Y5"],  # J
    "k": ["G00 X0 Y0", "G01 X0 Y15", "G00 X0 Y7", "G01 X10 Y15", "G00 X0 Y7", "G01 X10 Y0"],  # K
    "l": ["G00 X0 Y15", "G01 X0 Y0", "G01 X10 Y0"],  # L
    "m": ["G00 X0 Y0", "G01 X0 Y15", "G01 X5 Y10", "G01 X10 Y15", "G01 X10 Y0"],  # M
    "n": ["G00 X0 Y0", "G01 X0 Y15", "G01 X10 Y0", "G01 X10 Y15"],  # N
    "o": ["G00 X0 Y0", "G01 X10 Y0", "G01 X10 Y15", "G01 X0 Y15", "G01 X0 Y0"],  # O
    "p": ["G00 X0 Y0", "G01 X0 Y15", "G01 X5 Y15", "G01 X10 Y10", "G01 X5 Y7", "G01 X0 Y7"],  # P
    "q": ["G00 X0 Y0", "G01 X10 Y0", "G01 X10 Y15", "G01 X0 Y15", "G01 X0 Y0", "G01 X5 Y5", "G01 X10 Y0"],  # Q
    "r": ["G00 X0 Y0", "G01 X0 Y15", "G01 X5 Y15", "G01 X10 Y10", "G01 X5 Y7", "G01 X0 Y7", "G01 X10 Y0"],  # R
    "s": ["G00 X10 Y15", "G01 X0 Y15", "G01 X0 Y7", "G01 X10 Y7", "G01 X10 Y0", "G01 X0 Y0"],  # S
    "t": ["G00 X5 Y15", "G01 X5 Y0", "G00 X0 Y15", "G01 X10 Y15"],  # T
    "u": ["G00 X0 Y15", "G01 X0 Y0", "G01 X10 Y0", "G01 X10 Y15"],  # U
    "v": ["G00 X0 Y15", "G01 X5 Y0", "G01 X10 Y15"],  # V
    "w": ["G00 X0 Y15", "G01 X2 Y0", "G01 X5 Y10", "G01 X8 Y0", "G01 X10 Y15"],  # W
    "x": ["G00 X0 Y15", "G01 X10 Y0", "G00 X0 Y0", "G01 X10 Y15"],  # X
    "y": ["G00 X0 Y15", "G01 X5 Y7", "G01 X5 Y0", "G00 X10 Y15", "G01 X5 Y7"],  # Y
    "z": ["G00 X0 Y15", "G01 X10 Y15", "G01 X0 Y0", "G01 X10 Y0"],  # Z
}

# Function to convert text to G-code for the writing machine
def text_to_gcode(text):
    gcode_sequence = []
    for char in text.lower():
        if char in gcode_alphabet:
            gcode_sequence.extend(gcode_alphabet[char])  # Add G-code sequence for each letter
            gcode_sequence.append("G00 Z1")  # Lift pen after each letter (example)
    return gcode_sequence

# Loop to listen for speech input, convert to G-code, and output result
while True:
    try:
        # Use Bluetooth microphone as the audio source
        with sr.Microphone(device_index=bluetooth_microphone_index) as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Listening for text to convert to G-code...")
            
            # Listen to the user's input
            audio = r.listen(source2)
            
            # Recognize and convert speech to text
            MyText = r.recognize_google(audio, language="en-US")
            MyText = MyText.lower().strip()
            
            print("Recognized Text:", MyText)
            
            # Convert recognized text to G-code sequence
            gcode_output = text_to_gcode(MyText)
            
            if gcode_output:
                print("G-code Output:")
                for line in gcode_output:
                    print(line)
                SpeakText("G-code generated for your text.")
            else:
                print("No G-code generated for the recognized text.")
                SpeakText("Sorry, I could not generate G-code for that text.")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")
