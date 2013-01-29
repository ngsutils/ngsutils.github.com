---
layout: templ
title: stats
module: fastqutils
---
    
    Calculates summary statistics for a FASTQ file.
    
    It can calculate distribution of read lengths, average quality by base
    position, if a file is in colorspace, if it contains paired end data, and
    what encoding is used for the quality values (Sanger or Illumina).
    
    Note: Any quality values less than 0 are treated as 0.
    
    Usage: fastqutils stats filename.fastq{.gz}
    
