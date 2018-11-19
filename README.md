# Extract Markdown from BoostNote

## Abstract
You can extract Markdown from BoostNote!
BoostNote manages notes with cson file.
This program extract data from cson and generates markdown files.

Environment for operation check is
- macOS Mojave
- python 3.7.1

## Usage
```sh
git clone git@github.com:dorapon2000/boostnote2markdown.git
pip install -r requirements.txt
python boostnote_to_markdown.py

# Select your BoostNote working directory on the dialog.
```

Markdown files are made in directory "working_dir/markdown/"