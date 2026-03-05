"""This script reads a JSON file named 'data.json' and prints the text from each segment
contained within the file.
The JSON file is expected to have a structure where there is a key called 'segments'
that contains a list of segments, each with a 'text' field."""

import json
import os
import argparse

def save_to_txt(chunks, filename='output.txt'):
    """Saves the text from the segments to a text file."""
    if not args.save:
        return
    if os.path.exists(filename) and not args.overwrite:
        if input(f"{filename} already exists. Do you want to overwrite it? (y/n): ").lower() != 'y':
            print("Aborting save.")
            return
    with open(filename, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            f.write(chunk['text'] + '\n')
            f.write(f"Start: {chunk['start']}, End: {chunk['end']}\n")
            f.write('-' * 50 + '\n')

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default='data.json',
                    help='The JSON file to read from')
parser.add_argument('--autonomous', action='store_true',
                    help='Print segments autonomously without waiting for user input')
parser.add_argument('--overwrite', action='store_true',
                    help='Overwrite the output file if it already exists')
parser.add_argument('--save', action='store_true',
                    help='Save the segments to a text file')
args = parser.parse_args()

try:
    data = json.load(open(args.file, 'r', encoding='utf-8'))
except FileNotFoundError:
    print(f"The file '{args.file}' was not found.")
    exit()
except json.JSONDecodeError:
    print(f"Error decoding JSON from '{args.file}'.")
    exit()

try:
    segments = data['segments']
except KeyError:
    print("The key 'segments' was not found in the JSON data.")
    print("This is not a fault of the program,")
    print("but rather an issue with the structure of the JSON file.")
    exit()

if input("Do you want to print the segments? (y/n): ").lower() == 'y':
    autonomous = args.autonomous or input("Do you want to print \
segments autonomously? (y/n): ").lower() == 'y'
    for segment in segments:
        start = segment['start']
        end = segment['end']
        print(f"Text: {segment['text']}")
        print(f"Start: {start}, End: {end}")
        if not autonomous:
            input("Press enter to go to next segment... ")

save_to_txt(segments)
