---
layout: templ
title: filter
module: fastqutils
---
    
    Filter reads in a FASTQ file. The filtering criteria can be applied as a
    batch, allowing you to use more than one criterion at a time.
    
    
    Usage: fastqutils filter {opts} {filters} file.fastq{.gz}
    Options:
      -discard filename           Write the name of all discarded reads to a file
      -illumina                   Use Illumina scaling for quality values
                                  (-qual filter) [default: Sanger-scale]
      -stats filename             Write filter stats out to a file
      -v                          Verbose
    
    Filters:
      -wildcard num               Discard reads w/ more than N wildcards (N or .)
    
      -size minsize               Discard reads that are too short
    
      -qual minval window_size    Truncate reads (5'->3') where the quality falls
                                  below a threshold (floating average over
                                  window_size)
    
      -suffixqual minval          Trim away bases from the 3' end with low quality
                                  value should be given as a character (in Sanger
                                  scale)(like Illumina B-trim)
    
      -trim seq pct mintrim       Trim away at least [mintrim] bases that match a
                                  [sequence] (3' adaptor) allowing for a match
                                  percentage [pct] (0.0-1.0)
    
      -paired                     Only keep reads that are correctly paired
    
      -whitelist keeplist.txt     Only keep reads whose name is in the keeplist
    
    
    
