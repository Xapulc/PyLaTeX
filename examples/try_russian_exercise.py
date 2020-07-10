#!/usr/bin/python
"""
How to create document with russian language.

..  :copyright: (c) 2020 by Victor Kharlamov.
    :license: MIT, see License for more details.
"""

# begin-doc-include
from pylatex.base_classes import Options
from pylatex.package import Package
from pylatex import Document, Section, Subsection, Enumerate, NoEscape


class RussianDocument(Document):
    def __init__(self):
        super().__init__(geometry_options={"tmargin": "3cm",
                                           "bmargin": "3cm",
                                           "lmargin": "3cm",
                                           "rmargin": "3cm"})
        self.packages |= [Package('babel', Options("english", main="russian")),
                          Package("mathrsfs")]


if __name__ == "__main__":
    doc = RussianDocument()
    with doc.create(Section('Вариант 42')):
        with doc.create(Subsection("Стационарные последовательности в узком смысле")):
            with doc.create(Enumerate()) as enum:
                enum.add_item(NoEscape(r"Найти предел последовательности "
                                       r"случайных величин $\sum_{i=1}^n \sin(\xi_{i+1} - \xi_i) / n$, "
                                       r"где $\xi_i \sim R[0, 2\pi]$ -- н.о.р."))
                enum.add_item(NoEscape(r"Пусть $X \sim R\{1, \ldots, N\}$, $\sigma \in S_n$. "
                                       r"Рассмотрим последовательность "
                                       r"случайных величин $\xi_n := \sigma^n(X)$. "
                                       r"Показать, что случайная последовательность $\xi_n$ стационарна. "
                                       r"Когда она эргодична?"))
        with doc.create(Subsection("Пуассоновский процесс")):
            with doc.create(Enumerate()) as enum:
                enum.add_item(NoEscape(r"Найти $\mathsf{P}(\tau_{N_t+1} - t > x, t - \tau_{N_t} > y).$"))
                enum.add_item(NoEscape(r"Троллейбусы образуют пуассоновский поток. "
                                       r"Найти вероятность того, что два пассажира, пришедшие на остановку "
                                       r"в независимые случайные времена $R[0, 1]$, уедут вместе."))

    doc.generate_pdf('try_russian_exercise', clean_tex=False)
