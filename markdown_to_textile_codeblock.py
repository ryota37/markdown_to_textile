import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.CodeBlock):
        # 言語指定がある場合は取得し、classとして追加
        language = elem.classes[0] if elem.classes else ''
        # Textile形式の<pre><code>ブロックに変換
        return pf.RawBlock(f'<pre><code class="{language}">\n{elem.text}\n</code></pre>', format='textile')

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == "__main__":
    main()

