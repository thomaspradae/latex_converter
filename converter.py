import re
import os 

def convert_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # No conversion zones
    content = re.sub(r'<!-- noconvert -->(.*?)<!-- /noconvert -->', lambda x: x.group(0), content, flags=re.DOTALL)

    # LaTeX conversions
    content = re.sub(r'\$\$(.+?)\$\$', r'\\[ \1 \\]', content)
    content = re.sub(r'\$(.+?)\$', r'\\( \1 \\)', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def main():

    base_path = os.getcwd()

    folders = ['building', 'notes', 'writing']

    for folder in folders:
        full_path = os.path.join(base_path, folder)

        for root, dirs, files in os.walk(full_path):
            for file in files:
                if file.endswith('.md'):
                    convert_file(os.path.join(root, file))
                    
if __name__ == '__main__':
    main()
