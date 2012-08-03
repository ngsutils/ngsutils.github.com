---
layout: templ
title: merge
module: fastq
---
    
    Merges two (or more) paired end FASTQ files together for combined mapping.
    The files need to have the paired reads in the same order. They will be
    written out as:
    
    @name1
    seq1
    +
    qual1
    @name1
    seq2
    +
    qual2
    ...
    
    The merged file is written to stdout.
    
    Usage: fastqutils merge {-slash} file1.fastq{.gz} file2.fastq{.gz} ...
    
    -slash    Split the read name at a '/' (Illumina paired format)
    
    
