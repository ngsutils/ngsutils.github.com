---
layout: templ
title: unmerge
module: fastqutils
---
    
    Splits a combined FASTQ file into two (or more) FASTQ files.
    
    Files will be written as "out_template.N.fastq" where N is the
    pair number.
    
    Usage: fastqutils unmerge combined.fastq out_template
    
    Options:
      -gz    gzip compress the output files
    
    
