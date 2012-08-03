---
layout: templ
title: cims
module: bam
---
    
    Finds regions of unusual deletions (CLIP-seq)
    
    Given a set of BAM files, we search for areas where there are an unusual
    amount of deletions.  For CLIP-Seq, this can be an indicator of the location
    of protein-RNA interaction.
    
    Output is either a BED file or a FASTA format file containing these hotspots.
    Only unique regions are returned across all files.
    
    See: Zhang and Darnell, Nature Biotechnology (2011)
         doi:10.1038/nbt.1873
         pmid:21633356
    
    
    Usage: bamutils cims {opts} in.bam {in.bam...}
    
    Options:
        -fasta ref.fa    Ouput in FASTA format (requires reference genome.fa)
                         [default: BED output]
    
        -flanking N      The number of flanking bases on either side to report
                         (FASTA output only) [default: 12]
    
        -cutoff N        Cut-off % for deletions - if the % of reads that
                         include a deletion at a position is higher than this
                         number, the fragment is reported (0->1.0)
                         [default: 0.1]
    
        -ns              Don't take the strand of the read into account
    
        -window N        The maximum length of a deletion window
                         [default: 20]
    
    
