---
layout: templ
title: removeclipping
module: bam
---
    
    Postprocesses a BAM file to remove all clipping from reads and alignments.
    
    Hard clipping is removed from the alignment. Soft clipping is removed from
    the alignment and the sequence. The number of soft clipped bases is added as
    the 'ZA:i' (5' clipping) and 'ZB:i' (3' clipping) tags. The percentage of soft
    clipped bases is given in the 'ZC:f' tag.
    
    Usage: bamutils removeclipping {-f} inbamfile outbamfile
    
    Options:
      -f     Force overwriting an existing outfile
    
    
