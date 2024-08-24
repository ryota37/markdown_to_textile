# unescape_textile.py

# エスケープされた記号と元の記号のマッピング
escape_mapping = {
    "&#45;": "-",
    "&amp;": "&",
    "&lt;": "<",
    "&gt;": ">",
    "&quot;": "\"",
    "&apos;": "'",
    "&#43;": "+",
    "&#61;": "=",
    "&#42;": "*",
    "&#47;": "/",
    "&#92;": "\\",
    "&#58": ":",
    "&#59;": ";",
    "&#63;": "?",
    "&#33;": "!",
    "&#36;": "$",
    "&#37;": "%",
    "&#35;": "#",
    "&#64;": "@",
    "&#94;": "^",
    "&#95;": "_",
    "&#126;": "~",
    "&#124;": "|"
}

def unescape_textile_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for escaped, original in escape_mapping.items():
        content = content.replace(escaped, original)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    # 上書きするファイルの指定
    file_path = 'test.textile'
    
    unescape_textile_file(file_path)

