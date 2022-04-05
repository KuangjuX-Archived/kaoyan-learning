import os
import sys
import shutil
import csv


TEMPLATE_BEGIN = r"""
\documentclass[a4paper, 10pt]{ctexart}
\usepackage{multicol}
\usepackage{enumitem}
\title{考研英语词汇}
\author{KuangjuX}
\begin{document}
\begin{multicols*}{2}
    \begin{description}
"""


TEMPLATE_END = r"""
    \end{description}
\end{multicols*}
\end{document}
"""

TEMPLATE_WORD = r"""
\item[{word}] {explanations}
"""

TEMPLATE_JUST_WORD = r"""
\item[{word}]
"""

SRC_WORDLIST = 'WordList.csv'
DST_WORDLIST = 'wordlist.tex'
wordlist = open(DST_WORDLIST, 'w', encoding='utf-8')
wordlist.write(TEMPLATE_BEGIN)

with open(SRC_WORDLIST, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if len(row) > 1 and row[0] != '英文':
            fmt_args = {'word': row[0], 'explanations': row[1]}
            wordlist.write(TEMPLATE_WORD.format(**fmt_args))
            print(fmt_args)

wordlist.write(TEMPLATE_END)

os.system("xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape wordlist.tex")


remove_files = [
    "wordlist.log",
    "wordlist.aux",
    "wordlist.synctex.gz"
]

for file in remove_files:
    os.remove(file)