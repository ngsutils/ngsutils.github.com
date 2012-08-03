---
layout: templ
title: renamepair
module: bamutils
---
    
    Postprocesses a BAM file to rename pairs that have an extra /N value
    
    Some aligners output paired end reads with names ending in /1 or /2 to signify
    where the read came from in a paired end experiment. This can cause problems
    with downstream analysis packages that expect paired end reads to have the
    exact same name.
    
    Usage: bamutils renamepair {opts} inbamfile outbamfile
    
    Options:
      -f           Force overwriting an existing outfile
      -delim val   The trailing delimiter to use (default '/')
    
    
