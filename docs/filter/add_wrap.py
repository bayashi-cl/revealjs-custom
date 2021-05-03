"""
レベル2の見出し以下のコンテンツをdivタグの中に含めるフィルター。
"""

import io
import json
import sys


def wrap_section(ast):

    new_blocks = list()
    stacking = False

    for b in ast["blocks"]:
        if b["t"] == "Header":
            if b["c"][0] == 1:
                new_blocks.append(b)
                stacking = False
            elif b["c"][0] == 2:
                new_blocks.append(b)
                stacking = True
                div = {"t": "Div", "c": [["", ["wrap"], []], []]}
                new_blocks.append(div)
            else:
                if stacking:
                    new_blocks[-1]["c"][1].append(b)
                else:
                    new_blocks.append(b)

        elif b["t"] == "HorizontalRule":
            new_blocks.append(b)
            stacking = True
            div = {"t": "Div", "c": [["", ["wrap"], []], []]}
            new_blocks.append(div)

        else:
            if stacking:
                new_blocks[-1]["c"][1].append(b)
            else:
                new_blocks.append(b)

    ast["blocks"] = new_blocks

    return ast


if __name__ == "__main__":
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
    source = input_stream.read()
    ast = json.loads(source)

    wrap_section(ast)

    res = json.dumps(ast)
    sys.stdout.write(res)
