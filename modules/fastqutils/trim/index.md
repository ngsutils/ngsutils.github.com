---
layout: templ
title: trim
module: fastqutils
---
    
    Removes linkers from 5' and 3' ends by performing local
    s/w alignments with the linker sequences
    
    Usage: fastqutils trim {opts} filename.fastq{.gz}
    
    You must specify at least one of the following:
      -5 seq      5' linker sequence to remove
      -3 seq      3' linker sequence to remove
    
    Options
      -len val         Minimum length of a read (discards shorter) [default: 25]
      -pct val         Required percent identity (0->1.0) [default: 0.8]
      -min val         Minumum number of bases to trim (or minumum dist. from the
                       ends) [default: 4]
      -failed fname    Write failed reads to file
      -v               Verbose output for each alignment
    
    
