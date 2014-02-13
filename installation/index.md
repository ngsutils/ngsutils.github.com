---
layout: templ
title: Installation
---

Installation
---

### Getting the code

You can either download a specific version of NGSUtils or clone our Git repository. If you have `git` installed on
your computer, this is the recommended method for installation.

#### Download an archive

Go to: [https://github.com/ngsutils/ngsutils/tags](https://github.com/ngsutils/ngsutils/tags) to download the latest version of NGSUtils.

#### Git clone

The easiest way to install (and get updates) is to checkout the code from GitHub directly. To do this, you'll need
to clone our repository.


#### Install/compile dependencies

```
$ git clone git://github.com/ngsutils/ngsutils.git
$ cd ngsutils
$ make
```

Once you have the code downloaded, you need to run `make` in the ngsutils directory. This will create a virtualenv folder
(venv) and install the needed libraries. Once you run `make`, you should be able to run the `bamutils`, `bedutils`, 
`fastqutils`, and `gtfutils` programs. It is often helpful to add these files to your $PATH so that you can call them
directly without entering their full pathnames.


##### Custom python interpreter

If you need to use a custom python interpreter, such as `python2.6`, then you can specify this at the command line before running `make`.
The given interpreter will be used to create the virtualenv environment and be used by NGSUtils in the future without needing to specify the
PYTHON variable.

```
$ PYTHON=python2.6 make
```

### Requirements


#### Requires

* Mac OSX or Linux operating system (tested on RHEL5 and RHEL6)
* Python 2.6+ (including development packages)
* Make


> Note: for RHEL5, it is recommended that you add the EPEL repository to your yum configuration and 
> install the python26 packages. This will let NGSUtils use the proper version of Python
> without disrupting any system utilities.
>
> Also, virtualenv is now bundled with NGSUtils to make installation easier.

#### Will install

* [pysam](http://wwwfgu.anat.ox.ac.uk/~andreas/documentation/samtools/contents.html)
* Cython
* [swalign](http://github.com/mbreese/swalign)
* [eta](http://github.com/mbreese/eta) (progress bars for terminal; hidden when run in pipelines)
* coverage

Additionally, Cython requires that the Python headers be present on the system. For a linux 
system this can be achieved by installing 'python-devel' or similar.

#### Recommended

Here are some other tools that NGSUtils will work with.

* [samtools](http://samtools.sourceforge.net/) (indexing BAM/FASTA files)
* tabix (indexing tab-delimited BED files)

Some commands in NGSUtils require indexed BAM, FASTA, or BED files to work. These may all be indexed using [samtools](http://samtools.sourceforge.net/).