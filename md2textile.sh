# Before executing this command, copy markdown text and maintain it in clipboard.

pbpaste > test.md
pandoc -F markdown_to_textile_codeblock.py -t textile test.md -o test.textile

python3 unescape_textile.py

cat test.textile | pbcopy
