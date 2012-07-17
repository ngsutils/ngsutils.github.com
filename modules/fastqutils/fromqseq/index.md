---
layout: templ
title: fromqseq
module: fastqutils
---
    
    Converts an Illumina export.txt file to a FASTQ formatted file.
    This mainly consists of converting the quality scores to Phred format.
    In addtion, this can also remove reads which have failed the QC filter and
    trim away sequence that have a trailing 'B' for quality (Read Segment Quality
    Control Indicator).
    Based on: http://www.cassj.co.uk/blog/?p=490
              http://en.wikipedia.org/wiki/FASTQ_format
    
    Usage: fastqutils fromqseq {opts} export.txt
    
    Options:
      -solexa     file is pre-1.3 format (uses Solexa calculation for quality)
      -tag tag    Prefix the read names with this tag (such as the sample name)
      -trim       perform quality control indicator (trailing B) trimming
      -min N      the minimum allowed length for a read, post B-trimming
      -noqc       Don't remove reads that failed QC (for matching paired end data)
    
    
