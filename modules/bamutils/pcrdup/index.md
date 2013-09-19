---
layout: templ
title: pcrdup
module: bamutils
---
    
    For a BAM file, find and mark all possible PCR duplicates. This is meant to be
    used primarily with paired-end reads, since these have better resolution to
    verify that we care seeing a legitimate PCR duplicate and not just reads that
    happen to start at the same location.
    
    The orientation for paired-end reads is assumed to be "FR" (forward-reverse).
    
    Note: The BAM file must be sorted in order to find duplicates. For paired-end
          reads, the the proper-pair (0x4) flag must be set and the isize/tlen
          field must be correctly calculated.
    Usage: bamutils pcrdup {options} infile.bam
    
    Options:
        -frag                The reads are single-end fragments, so mark PCR
                             duplicated based only on the location of the read 
                             (not-recommended)
    
        -bam filename        Output BAM file with PCR duplicates marked
    
        -counts filename     Output of the number of reads at each position 
    
                             Note: this is actually the number of duplicate reads
                             at each position. If a position has multiple reads
                             mapped to it, but they are not pcr duplicates, then
                             there each will be reported separately.
    
        You must set either -bam or -counts (or both).
    
    
