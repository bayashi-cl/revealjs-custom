# revealjs-custom

サンプルは[こちら](https://bayashi-cl.github.io/revealjs-custom/sample.html)

## css

### orange.css

reveal.jsのカスタムテーマ。  
テキストを左寄せし、全体的に見栄えを整えた。

### rmd-fix.css

Rのrevealjsパッケージから生成されるhtmlとの差を吸収する。

## filter

### add_wrap.py

レベル2の見出し以下のコンテンツをdivタグの中に含めるフィルター。

`-F filter/add_wrap.py`で適用する。

### h1-centering.lua

レベル1の見出しにcenterクラスを追加するフィルター。

`-L filter/h1-centering.lua`で適用する。
