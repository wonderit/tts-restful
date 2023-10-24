from piper.voice import PiperVoice as piper  # Backbone of text to speech
import wave  # Writing text to speech to wave files
from sys import platform
from os import remove
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Stop pygame from saying hello in the console

# Check if the operating system is MacOS
if platform == 'darwin':
    print('This library cannot be used on MacOS yet, due to piper not being supported there.')
    exit()  # Piper isn't available on MacOS yet

model = None  # Set the model to none at the start
voice = None  # Set the voice to none at the start


# Function to load and set the voice model to be used
def load(model_set):
    global model
    global voice

    if '.onnx' in model_set:  # Is the extension .onnx in the filename, if not add it below.
        model = model_set  # Set model variable as is.
    else:
        model = model_set + '.onnx'  # Set model variable and append .onnx.

    # Try to load the model
    try:
        voice = piper.load(model)  # Load the model
    except:
        print("Something went wrong, did you type the correct name for the model?")
        exit()


# Function to save a text to speech file to disk
def save(text, file_name, speaker_id, model_set=model):
    global model
    global voice

    if model_set == None and model == None:  # Check if a model has been set, if not then exit.
        print("No model was set! Please set a model using the load function: load(\"your_model_here\")")
        exit()
    elif model_set != None:  # Is there a voice that should be used only once?
        temp_voice = piper.load(model_set)
        with wave.open(file_name, "wb") as wav_file:
            return temp_voice.synthesize(text, wav_file, speaker_id=speaker_id)
    else:  # If not, use the voice that was set eariler.
        with wave.open(file_name, "wb") as wav_file:
            return voice.synthesize(text, wav_file)

