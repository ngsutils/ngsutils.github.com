---
layout: templ
title: bed3to6
module: bedutils
---
    
    Convert a BED3 file to a BED6 file with constant name, score, and strand.
    
    
    Usage: bedutils bed3to6 {-name val} {-score val} {-strand val} bedfile
    
    Defaults:
        name: chrom:start-end
        score: 0
        strand: "+"
    
    
    
