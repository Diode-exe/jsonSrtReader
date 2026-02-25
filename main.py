"""This script reads a JSON file named 'ACaudio.json' and prints the text from each segment contained
within the file.
The JSON file is expected to have a structure where there is a key called 'segments'
that contains a list of segments, each with a 'text' field."""

import json

data = json.load(open('data.json', 'r', encoding='utf-8'))

segments = data['segments']

for segment in segments:
    start = segment['start']
    end = segment['end']
    print(f"Text: {segment['text']}")
    print(f"Start: {start}, End: {end}")
    input("Press enter to go to next segment... ")
