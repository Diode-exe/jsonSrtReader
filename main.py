"""This script reads a JSON file named 'ACaudio.json' and prints the text from each segment
contained within the file.
The JSON file is expected to have a structure where there is a key called 'segments'
that contains a list of segments, each with a 'text' field."""

import json
import os

def save_to_txt(chunks, filename='output.txt'):
    """Saves the text from the segments to a text file."""
    if os.path.exists(filename):
        if input(f"{filename} already exists. Do you want to overwrite it? (y/n): ").lower() != 'y':
            print("Aborting save.")
            return
    with open(filename, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            f.write(chunk['text'] + '\n')
            f.write(f"Start: {chunk['start']}, End: {chunk['end']}\n")
            f.write('-' * 50 + '\n')

data = json.load(open('data.json', 'r', encoding='utf-8'))

segments = data['segments']

if input("Do you want to print the segments? (y/n): ").lower() == 'y':
    autonomous = input("Do you want to print segments autonomously? (y/n): ").lower() == 'y'
    for segment in segments:
        start = segment['start']
        end = segment['end']
        print(f"Text: {segment['text']}")
        print(f"Start: {start}, End: {end}")
        if not autonomous:
            input("Press enter to go to next segment... ")

save_to_txt(segments)
