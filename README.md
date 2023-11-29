# CNN/DailyMail Dataset as SQLite

[![PyPI][pypi-badge]][pypi-link]
[![Python 3.9][python39-badge]][python39-link]
[![Python 3.10][python310-badge]][python310-link]
[![Build Status][build-badge]][build-link]

Creates a SQLite database if the CNN and DailyMail summarization dataset.


## Documentation

See the [full documentation](https://plandes.github.io/cnndmdb/index.html).
The [API reference](https://plandes.github.io/cnndmdb/api.html) is also
available.


## Obtaining

The easiest way to install the command line program is via the `pip` installer:
```bash
pip3 install zensols.cnndmdb
```

Binaries are also available on [pypi].


## Usage

This package can be used from the command line with the `cnndmdb`
[command](#command-line), or as a [Python API](#api).


### Install

1. Create the SQLite database file: `cnndmdb load`.  This takes a while since
   the entire corpus is first downloaded and then inserted into the SQLite
   file.
1. Check to make sure the file `data/cnndm.sqlite3` was created.
1. Optionally create a `~/.cnndmdbrc` to relocate the `data/cnndm.sqlite3`
   file.

To relocate the SQLite file, add the following to the `~/.cnndmdbrc` file:
```ini
[cnndmdb_default]
db_file = ~/path/to/cnndm.sqlite3
```


### Command Line

The SQLite database keys can be given:
```bash
cnndmdb keys
```

Then the command line can also be used to print articles:
```bash
cnndmdb show -t org 3b07f5102c69e3e609d73b2ccb0dc5549d4fbaf6
```
The `-t org` tells it to use the original corpus keys.  This option also allows
for selected SQLite `rowid` keys or a Kth smallest article.


### API

The corpus objects are accessible as mapped Python objects.  For example:

```python
corpus: Corpus = ApplicationFactory.get_corpus()
art: Article = next(iter(corpus.stash.values()))
print(art.text)
```


## Data Source

The data is sourced from a [Tensorflow dataset], which in turn uses the
[Abigail See GitHub] repository.

```bibtex
@article{DBLP:journals/corr/SeeLM17,
  author    = {Abigail See and
               Peter J. Liu and
               Christopher D. Manning},
  title     = {Get To The Point: Summarization with Pointer-Generator Networks},
  journal   = {CoRR},
  volume    = {abs/1704.04368},
  year      = {2017},
  url       = {http://arxiv.org/abs/1704.04368},
  archivePrefix = {arXiv},
  eprint    = {1704.04368},
  timestamp = {Mon, 13 Aug 2018 16:46:08 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SeeLM17},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

```bibtex
@inproceedings{hermann2015teaching,
  title={Teaching machines to read and comprehend},
  author={Hermann, Karl Moritz and Kocisky, Tomas and Grefenstette, Edward and Espeholt, Lasse and Kay, Will and Suleyman, Mustafa and Blunsom, Phil},
  booktitle={Advances in neural information processing systems},
  pages={1693--1701},
  year={2015}
}
```


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## License

[MIT License](LICENSE.md)

Copyright (c) 2023 Paul Landes


<!-- links -->
[pypi]: https://pypi.org/project/zensols.cnndmdb/
[pypi-link]: https://pypi.python.org/pypi/zensols.cnndmdb
[pypi-badge]: https://img.shields.io/pypi/v/zensols.cnndmdb.svg
[python39-badge]: https://img.shields.io/badge/python-3.9-blue.svg
[python39-link]: https://www.python.org/downloads/release/python-390
[python310-badge]: https://img.shields.io/badge/python-3.10-blue.svg
[python310-link]: https://www.python.org/downloads/release/python-310
[build-badge]: https://github.com/plandes/cnndmdb/workflows/CI/badge.svg
[build-link]: https://github.com/plandes/cnndmdb/actions

[Tensorflow dataset]: https://www.tensorflow.org/datasets/catalog/cnn_dailymail
[Abigail See GitHub]: https://github.com/abisee/cnn-dailymail
