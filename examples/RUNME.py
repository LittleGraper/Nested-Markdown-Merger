import os

def find_markdown_files(directory):
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') or file.endswith('.mdx'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def merge_markdown_files(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in files:
            with open(file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n\n')

if __name__ == '__main__':
    directory_to_scan = '.'  # Current Working Directory
    output_file = 'merged_output.md'
    markdown_files = find_markdown_files(directory_to_scan)
    merge_markdown_files(markdown_files, output_file)
    print(f'Merged {len(markdown_files)} files into {output_file}')


