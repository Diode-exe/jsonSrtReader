# JSON SRT Reader

A simple script to read JSON SRT files and save them to ```output.txt```.

You can also print the content to the console if you want.

## Usage

1. Place your JSON SRT file in the same directory as this script and name it `data.json`.
2. Run the script using Python:

    ```bash
    python main.py
    ```

3. The output will be saved to `output.txt` in the same directory.

## Example JSON SRT Format

```json
    "segments": [
            {
                "start": 0.773,
                "end": 7.228,
                "text": " Hi, you're using the JSON SRT reader script. ",
            },
            {
                "start": 7.229,
                "end": 14.456,
                "text": " How is it? ",
            },
            {
                "start": 14.457,
                "end": 21.684,
                "text": "Computers are great, aren't they? ",
            },
    ]
```
