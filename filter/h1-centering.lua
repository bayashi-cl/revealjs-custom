-- レベル1の見出しにcenterクラスを追加し、
-- reveal.js上で画面中央に表示するフィルタ。
-- -V center=falseオプションをつけて使ってください。

function Header(elem)
    if elem.level == 1 then
        table.insert(elem.classes, 'center')
    end
    return elem
end
