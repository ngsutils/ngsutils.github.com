---
layout: templ
title: tobedgraph
module: bamutils
---
    
    Convert BAM coverage to bedGraph based on read depth. This will take into
    account gaps in RNAseq alignments and not display any coverage across introns.
    
    This can optionally normalize the counts by a given factor or display only
    coverage for a specific strand.
    
     See: http://genome.ucsc.edu/goldenPath/help/bedgraph.html
          http://genome.ucsc.edu/goldenPath/help/bigWig.html
    
    Usage: bamutils tobedgraph {opts} bamfile
    
    Options:
        -plus             Only count reads on the plus strand
                          (default: count all reads)
        -minus            Only count reads on the minus strand
    
        -norm VAL         The count at every position is calculated as:
                          floor(count * VAL).
    
        -ref name         Only count reads mapping to this reference (chrom)
    
        -region chr:start-end    Count reads mapping to this genome region
                                 (start is 1-based)
    
    
