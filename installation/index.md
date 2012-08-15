---
layout: templ
title: Installation
---

Getting the code
---

You can either download a specific version of NGSUtils or clone our Git repository. If you have `git` installed on
your computer, this is the recommended method for installation.

#### Download an archive

Go to: [https://github.com/ngsutils/ngsutils/tags](https://github.com/ngsutils/ngsutils/tags) to download the latest version of NGSUtils.

#### Git clone

The easiest way to install (and get updates) is to checkout the code from GitHub directly. To do this, you'll need
to clone our repository.

`git clone git://github.com/ngsutils/ngsutils.git`


Installation
---

Once you have the code downloaded, you need to run `make` in the ngsutils directory. This will create a virtualenv folder
(env) and install the needed libraries. Once you run `make`, you should be able to run the `bamutils`, `bedutils`, 
`fastqutils`, and `gtfutils` programs. It is often helpful to add these files to your $PATH so that you can call them
directly without entering their full pathnames.

### Requirements


#### Requires

* Mac OSX or Linux operating system (tested on RHEL5 and RHEL6)
* Python 2.6+ (including development packages)
* [virtualenv](http://www.virtualenv.org/)
* Make

> Note: for RHEL5, it is recommended that you add the EPEL repository to your yum configuration and 
> install the python26 and python26-virtualenv packages. This will let NGSUtils use the proper version of Python
> without disrupting any system utilities.

#### Will install

* [pysam](http://wwwfgu.anat.ox.ac.uk/~andreas/documentation/samtools/contents.html)
* Cython

The only libraries that are mandatory are *pysam* and *cython*. Additionally, Cython requires that the
Python headers be present on the system. For a linux system this can be achieved by installing
'python-devel' or similar. These will both be installed in the virtualenv env folder.

#### Recommended

* [samtools](http://samtools.sourceforge.net/) (indexing BAM/FASTA files)
* tabix (indexing tab-delimited BED files)

Some commands in NGSUtils require indexed BAM, FASTA, or BED files to work. These may all be indexed using [samtools](http://samtools.sourceforge.net/).