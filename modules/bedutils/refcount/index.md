---
layout: templ
title: refcount
module: bed
---
    
    Given a BED file containing genomic regions of interest (reference) and a set
    of other BED files (tabix-indexed), calculate how many samples also
    contain the region of interest.
    
    Example:
    ref           (A)========        (B)============================
    sample 1       ---    ----              -----  -- ------   ----
    sample 2           ----           ------------
    sample 3                                                     -----
    sample 4          ----
    
    Would return:
            sample 1        sample 2        sample 3        sample 4        total
    ref A      2               1               0               1              3
    ref B      4               1               1               0              3
    
    
    Usage: bedutils refcount {-ns} ref.bed sample1.bed sample2.bed ...
           bedutils refcount {-ns} ref.bed -group name sample1-1 sample1-2 ...\
                                  -group name sample2-1 sample2-2 ...
    
    Where the sample BED files are Tabix indexed (sample1.bed.tgz.tbi exists).
    The sample names are calculated using the names of the files.
    
    The reference BED file shouldn't be Tabix indexed (it is read directly)/
    
    If you have only two sample groups a Fisher Test p-value will be calculated.
    
    Options:
      -ns   Ignore strandedness in counts
    
    Bad argument: -h
    
    Given a BED file containing genomic regions of interest (reference) and a set
    of other BED files (tabix-indexed), calculate how many samples also
    contain the region of interest.
    
    Example:
    ref           (A)========        (B)============================
    sample 1       ---    ----              -----  -- ------   ----
    sample 2           ----           ------------
    sample 3                                                     -----
    sample 4          ----
    
    Would return:
            sample 1        sample 2        sample 3        sample 4        total
    ref A      2               1               0               1              3
    ref B      4               1               1               0              3
    
    
    Usage: bedutils refcount {-ns} ref.bed sample1.bed sample2.bed ...
           bedutils refcount {-ns} ref.bed -group name sample1-1 sample1-2 ...\
                                  -group name sample2-1 sample2-2 ...
    
    Where the sample BED files are Tabix indexed (sample1.bed.tgz.tbi exists).
    The sample names are calculated using the names of the files.
    
    The reference BED file shouldn't be Tabix indexed (it is read directly)/
    
    If you have only two sample groups a Fisher Test p-value will be calculated.
    
    Options:
      -ns   Ignore strandedness in counts
    
    
