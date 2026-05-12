# AI on the Edge - Lesson 8
# Class Code: Text to Speech (TTS)
# Lori Pfahler
# May 2026

# import voice model Piper
from fusion_hat.tts import Piper

# create text to speech object and set specific voice model
tts = Piper()


# code to see all available voices/models
voice_dict = tts.available_models('en_US')
# print(voice_dict)

# output:
# 'amy': ['en_US-amy-low', 'en_US-amy-medium'],
# 'arctic': ['en_US-arctic-medium'],
# 'bryce': ['en_US-bryce-medium'],
# 'danny': ['en_US-danny-low'],
# 'hfc_female': ['en_US-hfc_female-medium'],
# 'hfc_male': ['en_US-hfc_male-medium'],
# 'joe': ['en_US-joe-medium'],
# 'john': ['en_US-john-medium'],
# 'kathleen': ['en_US-kathleen-low'],
# 'kristin': ['en_US-kristin-medium'],
# 'kusal': ['en_US-kusal-medium'],
# 'l2arctic': ['en_US-l2arctic-medium'],
# 'lessac': ['en_US-lessac-low', 'en_US-lessac-medium', 'en_US-lessac-high'],
# 'libritts': ['en_US-libritts-high'], 'libritts_r': ['en_US-libritts_r-medium'],
# 'ljspeech': ['en_US-ljspeech-medium', 'en_US-ljspeech-high'],
# 'norman': ['en_US-norman-medium'],
# 'reza_ibrahim': ['en_US-reza_ibrahim-medium'],
# 'ryan': ['en_US-ryan-low', 'en_US-ryan-medium', 'en_US-ryan-high'],
# 'sam': ['en_US-sam-medium']

# cycle through all voice models and hear the message; voice is the key, variations is the value
for voice, variations in voice_dict.items():
    # variations is a list that can have more than one element
    for variation in variations:
        # get the last "word" in the model name which are separated by dashes (see output above)
        variation_short = variation.split('-')[-1]
        # set the variation to use for speech
        tts.set_model(variation)
        # create the message that tells us the voice/model
        msg = f'Hi, I am {voice} {variation_short}. Are you ready to rumble? I am here to pump you up!'
        # say the message
        tts.say(msg, stream = False)


