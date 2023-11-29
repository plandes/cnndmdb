#!/usr/bin/env python

from pathlib import Path
from zensols.cli import CliHarness; CliHarness.add_sys_path(Path('../src/python'))
from zensols.cnndmdb import Article, Corpus, ApplicationFactory


def main():
    corpus: Corpus = ApplicationFactory.get_corpus()
    art: Article = next(iter(corpus.stash.values()))
    print(art.text)
    art.write()


if (__name__ == '__main__'):
    main()
