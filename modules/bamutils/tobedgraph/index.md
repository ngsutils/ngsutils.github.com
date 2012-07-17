---
layout: templ
title: tobedgraph
module: bamutils
---
    
    Convert BAM coverage to bedGraph
    
    Takes a BAM file and produces a bedGraph file.  This can optionally
    normalize the counts by a given factor.
    
     See: http://genome.ucsc.edu/goldenPath/help/bedgraph.html
          http://genome.ucsc.edu/goldenPath/help/bigWig.html
    
    Usage: bamutils tobedgraph [-plus | -minus] {-norm N} bamfile
    
    Options:
        -plus             only count reads on the plus strand
                          (default: count all reads)
        -minus            only count reads on the minus strand
    
        -norm VAL         the count at every position is calculated as:
                          floor(count * VAL).
    
    
