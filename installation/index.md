---
layout: templ
title: Installation
---

We are working on setting up a dedicated version download, but until then, the easiest way to install (and get updates) is to checkout the code from GitHub directly.

Checkout the code and run `make`. This will create a virtualenv folder (env) and install the needed libraries. The only libraries that are
mandatory are *pysam* and *cython*. Cython requires that the Python headers be present on the system. For a linux system this can be
achieved by installing 'python-devel' or similar.

If you need read-only access use:
`git clone git://github.iu.edu/mbreese/ngsutils.git`

Requires

* Python 2.6+ (including development packages)
* virtualenv

Will install

* pysam
* Cython

Recommended

* samtools (indexing BAM/FASTA files)
* tabix (indexing tab-delimited BED files)
