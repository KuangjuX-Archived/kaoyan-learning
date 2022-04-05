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

TEMPLATE_WORD2 = r"""
\item[{word}]
"""

TEMPLATE_JUST_WORD = r"""
\item[{word}]
"""

SRC_WORDLIST = 'WordList.csv'
DST_WORDLIST = 'wordlist.tex'
DST_WORDLIST2 = 'wordlist2.tex'
wordlist = open(DST_WORDLIST, 'w', encoding='utf-8')
wordlist2 = open(DST_WORDLIST2, 'w', encoding='utf-8')

wordlist.write(TEMPLATE_BEGIN)
wordlist2.write(TEMPLATE_BEGIN)

with open(SRC_WORDLIST, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if len(row) > 1 and row[0] != '英文':
            fmt_args_1 = {'word': row[0], 'explanations': row[1]}
            fmt_args_2 = {'word': row[0]}
            wordlist.write(TEMPLATE_WORD.format(**fmt_args_1))
            wordlist2.write(TEMPLATE_WORD2.format(**fmt_args_2))

wordlist.write(TEMPLATE_END)
wordlist2.write(TEMPLATE_END)

os.system("xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape wordlist.tex")
os.system("xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape wordlist2.tex")

remove_files = [
    "wordlist.log",
    "wordlist.aux",
    "wordlist.synctex.gz",
    "wordlist2.log",
    "wordlist2.aux",
    "wordlist2.synctex.gz",

]

for file in remove_files:
    os.remove(file)