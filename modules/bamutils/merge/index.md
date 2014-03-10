---
layout: templ
title: merge
module: bamutils
---
    
    Combine multiple BAM files together (taking best-matches)
    
    Given a number of BAM files, this script will merge them together, taking
    only the best matches.  There can be any number of files, but the BAM header
    will be taken from the first one.  The input files should be sorted by read
    name, or at least have reads in the same order.
    
    The first input file should have a record for every read in the other files.
    However, the secondary files *may* have missing lines, so long as they are in
    the same order as the first file.
    
    The value of the attribute/tag given will be used to determine which reads
    should be kept and which should be discarded. The tag should be a numeric
    (int/float) type. More than one tag may be used. This defaults to ['AS+', 'NM-'].
    
    Additionally, each file can have more than one record for each read, that may
    all have the same value for the tag used in determining which reads to keep.
    For example, if the AS tag is used (default), then each read in a file
    may have the same AS value. In this case, all reads with the best AS score
    will be kept.
    
    
    
    Usage: bamutils merge {opts} out.bam in1.bam in2.bam ...
    
    Options
      -tag VAL    Tag to use to determine from which file reads will be taken.
                  (must be type :i or :f) You may have more than one of these,
                  in which case they will be sorted in order. You can add a +/-
                  at the end of the name to signify sort order (asc/desc). 
                  [default: AS+, NM-]
    
      -discard    Discard reads that aren't mapped in any file.
    
      -keepall    Keep all mappings for each read, not just the best one.
                  (Note: only one mapping to each ref/pos will be kept)
    
    
