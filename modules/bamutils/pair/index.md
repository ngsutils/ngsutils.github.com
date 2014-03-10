---
layout: templ
title: pair
module: bamutils
---
    
    Given two separately mapped paired-end files, re-pair the files, selecting
    the most likely pairing partners based upon strand, insert distance, and
    maximizing alignment scores.
    
    It is very important that the files are either in the same order with each
    read present in both files or sorted in name order.
    
    The value of the attribute/tag given will be used to determine which reads
    should be kept and which should be discarded. The tag should be a numeric
    (int/float) type. More than one tag can be used. The default is 'AS+, NM-'.
    
    The BEST pair will be kept that maximizes the tag values and otherwise
    satisfies strand and distance values.
    
    
    Usage: bamutils pair {opts} out.bam read1.bam read2.bam 
    
    Options
      -tag VAL            Tag to use to determine from which file reads will be
                          taken. (must be type :i or :f) You may have more than
                          one of these, in which case they will be sorted in
                          order. You can add a +/- at the end of the name to 
                          signify sort order (asc/desc). 
                          Default: AS+, NM-
    
      -size low-high      The minimum/maximum insert size to accept. By default,
                          this will attempt to minimize the distance between
                          reads, upto the lower-bound. Any pair over the upper
                          bound will be discarded. Note: for RNA, because it is
                          impossible to detect junctions that are between the
                          reads, this should be a very big range (ex: 50-1000000)
                          Default: 50-10000
    
      -fail1 fname.bam    Write all failed mappings from read1 to this file
      -fail2 fname.bam    Write all failed mappings from read1 to this file
                          (Note: -fail1 and -fail2 can be the same file.)
    
      -reason tag         Write the reason for failure to this tag (only for
                          failed reads/mappings) Must be a valid two char name.
    
    
