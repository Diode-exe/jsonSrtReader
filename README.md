# JSON SRT Reader

A simple script to read JSON SRT files and save them to ```output.txt```.

You can also print the content to the console if you want.

## Usage

1. Place your JSON SRT file in the same directory as this script and name it `data.json`.
2. Run the script using Python:

    ```bash
    python json_srt_reader.py
    ```

3. The output will be saved to `output.txt` in the same directory.

## Example JSON SRT Format

```json
[
    {
        "start": "00:00:01,000",
        "end": "00:00:04,000",
        "text": "Hello, world!"
    },
    {
        "start": "00:00:05,000",
        "end": "00:00:08,000",
        "text": "Welcome to JSON SRT Reader."
    }
]
```
