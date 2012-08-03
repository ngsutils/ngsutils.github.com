---
layout: templ
title: tobedgraph
module: bed
---
    
    Takes a BED file with overlapping regions and produces a BedGraph file.  This
    can optionally normalize the counts by a given factor.
    
     See: http://genome.ucsc.edu/goldenPath/help/bedgraph.html
          http://genome.ucsc.edu/goldenPath/help/bigWig.html
    
    Usage: bedutils tobedgraph [-plus | -minus] {-norm N} bamfile
    
    Options:
        -plus             only count reads on the plus strand
                          (default: count all reads)
        -minus            only count reads on the minus strand
    
        -norm VAL         the count at every position is calculated as:
                          floor(count * VAL).
    
    
