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

SRC_WORDLIST = '高频词.csv'
DST_WORDLIST = '高频词.tex'
DST_WORDLIST2 = '高频词-中文.tex'
wordlist = open(DST_WORDLIST, 'w', encoding='utf-8')
wordlist2 = open(DST_WORDLIST2, 'w', encoding='utf-8')

wordlist.write(TEMPLATE_BEGIN)
wordlist2.write(TEMPLATE_BEGIN)

with open(SRC_WORDLIST, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    for index, row in enumerate(reader):
        if len(row) > 0 and row[0][0:8] != 'WordList':
            fmt_args_1 = {'word': row[0], 'explanations': row[1]}
            fmt_args_2 = {'word': row[0]}
            wordlist.write(TEMPLATE_WORD.format(**fmt_args_1))
            wordlist2.write(TEMPLATE_WORD2.format(**fmt_args_2))

wordlist.write(TEMPLATE_END)
wordlist2.write(TEMPLATE_END)

os.system("xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape 高频词.tex")
os.system("xelatex -synctex=1 -interaction=nonstopmode -file-line-error -shell-escape 高频词-中文.tex")

remove_files = [
    "高频词.log",
    "高频词.aux",
    "高频词.synctex.gz",
    "高频词-中文.log",
    "高频词-中文.aux",
    "高频词-中文.synctex.gz",
]

for file in remove_files:
    os.remove(file)