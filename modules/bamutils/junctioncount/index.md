---
layout: templ
title: junctioncount
module: bamutils
---
    
    Counts the number of reads that span each junction found in the BAM file.
    
    You can specify a particular genome range to scan (like a gene region).
    
    Usage: bamutils junctioncount {opts} bamfile {region}
    
    Region should be: chr:start-end (start 1-based)
    
    
    
