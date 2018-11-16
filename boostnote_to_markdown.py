import os
import re
import json
import cson
import tkinter, tkinter.filedialog 

def convert_to_name(dir_key, conf):
    """Convert from directory key  to directory name

    :param  str dir_key:    string in boostnote.json/folder/folder
    :param  dict    conf:   dictionary converted from boostnote.json
    :rtype: str
    :return: directory name
    """
    for dir_meta in conf['folders']:
        if dir_meta['key'] == dir_key:
            dir_name = dir_meta['name']
            return dir_name

    return None

def sanitize(str_):
    """Sanitize string for Windows

    target: \\/:,*?<>|

    :param  str str_:   string you want to sanitize
    :rtype: string
    :return:    sanitized string
    """
    
    if re.search('[\\/:,*?<>|]', str_) is None:
        return str_

    str_ = str_.replace('\\', '[backslash]')
    str_ = str_.replace('/', '[spash]')
    str_ = str_.replace(':', '[colon]')
    str_ = str_.replace(',', '[hyphen]')
    str_ = str_.replace('*', '[star]')
    str_ = str_.replace('?', '[question]')
    str_ = str_.replace('<', '[less]')
    str_ = str_.replace('>', '[greater]')

    print(f'"{str_}" is sanitized')

    return str_

def extract_md_from_BoostNote():
    """Extract Markdown from BoostNote
    """

    cnt_success = 0
    cnt_skip = 0

    root = tkinter.Tk()
    root.withdraw()
    msg = 'Select your BoostNote working directory'
    boostnote = tkinter.filedialog.askdirectory(title=msg)
    conf_json = os.path.join(boostnote, 'boostnote.json')
    with open(conf_json) as f:
        conf = json.load(f)

    notes = os.path.join(boostnote, 'notes')
    for file in os.listdir(notes):
        with open(os.path.join(notes, file)) as f:
            note = cson.load(f)

            if note['type'] != 'MARKDOWN_NOTE':
                cnt_skip += 1
                continue

            key = note['folder']
            folder = convert_to_name(key, conf)
            title = note['title']
            content = note['content']

            if note['isTrashed'] :
                folder = 'Trash'

        folder = sanitize(folder)
        title = sanitize(title)

        output_dir = os.path.join(boostnote, 'markdown', folder)
        os.makedirs(output_dir, exist_ok=True)
        output_file_name = title + '.md'
        output_file = os.path.join(output_dir, output_file_name)
        
        with open(output_file, 'w') as f:
            f.write(content)

        cnt_success += 1

    print('=============================================')
    print('Converting BoostNote to Markdown is Success!!')
    print(f'success: \t{cnt_success}')
    print(f'skip:    \t{cnt_skip}')

if __name__ == '__main__':
    extract_md_from_BoostNote()