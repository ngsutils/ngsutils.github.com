---
layout: templ
title: best
module: bamutils
---
    
    Given a BAM file sorted by read name with potentially multiple mappings, this
    will remove all but the best mapping.
    
    The value of the attribute/tag given will be used to determine which reads
    should be kept and which should be discarded. The tag should be a numeric
    (int/float) type. Multiple tags may be used. This defaults to 'AS+, NM-'.
    
    
    Usage: bamutils best {opts} input.bam output.bam
    
    Options
      -tag VAL    Tag to use to determine from which file reads will be taken.
                  (must be type :i or :f) You may have more than one of these,
                  in which case they will be sorted in order. You can add a +/-
                  at the end of the name to signify sort order (asc/desc). 
                  [default: AS+, NM-]
    
      -fail filename.bam    Write all failed mappings to this file.
    
    
    
