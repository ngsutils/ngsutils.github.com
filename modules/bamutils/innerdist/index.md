---
layout: templ
title: innerdist
module: bamutils
---
    
    Calculate the inner mate-pair distance from two BAM files
    
    With paired-end reads, knowing the inner mate-pair distance is key for some
    downstream analyses or mapping. This value can be estimated using wet-lab
    techniques, but can also be found empirically. If you map each fragment
    separately to a common reference (genome or transcriptome), this command will
    calculate the average distance between the fragments.
    
    Reads where one (or both) fragment is unmapped are ignored, as are pairs that
    map to different references.
    
    (reference) ===============================================================
                     (frag 1) >>>>>>>>>                      <<<<<<<< (frag 2)
                                       |--------------------|
                                      inner mate-pair distance
    
    This will also work if the reads are aligned in the opposite orientation:
    
    (reference) ===============================================================
                     (frag 2) >>>>>>>>>                      <<<<<<<< (frag 1)
                                       |--------------------|
                                      inner mate-pair distance
    
    or if they overlap:
    
    (reference) ===============================================================
                               (frag 1) >>>>>>>>>
                                             <<<<<<<< (frag 2)
                                            |----|
                                      inner mate-pair distance (negative)
    
    
    Usage: bamutils innerdist filename1.bam filename2.bam
    
    Note: BAM files must be paired and they must be mapped to the
          same reference and reads must be in the same order.
    
    
    
