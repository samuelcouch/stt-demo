import os
import json
from os.path import join, dirname
from dotenv import load_dotenv

"""
import the SpeeckToTextV1 package and rename it for convenience
"""
from watson_developer_cloud import SpeechToTextV1 as SpeechToText

"""
import the recorder package
"""
from recorder.recorder import Recorder

"""
accept audio file as parameter, pass the audio to watson and return the response
"""
def transcribe_audio(stt, path_to_audio_file):
  with open(join(dirname(__file__), path_to_audio_file), 'rb') as audio_file:
    return stt.recognize(audio_file,
      content_type='audio/wav')

def main():
  """
  load the environment variables
  """
  dotenv_path = join(dirname(__file__), '.env')
  load_dotenv(dotenv_path)

  """
  initialize the speech to text service
  """
  stt = SpeechToText(
          username=os.environ.get("STT_USERNAME"),
          password=os.environ.get("STT_PASSWORD"))

  """
  initialize the recorder, provide a filename to save it as
  """
  recorder = Recorder("speech.wav")

  print("How can I help you?\n")
  recorder.record_to_file()

  print("Transcribing audio....\n")
  result = transcribe_audio(stt, 'speech.wav')

  text = result['results'][0]['alternatives'][0]['transcript']
  print("Text: " + text + "\n")

if __name__ == '__main__':
  try:
    main()
  except:
    print("IOError detected, restarting...")
    main()
