---
layout: templ
title: remove_dup
module: gtf
---
    In RefSeq annotations, a particular transcript may be assigned to multiple
    locations. In this case, the transcript name is altered to be
    transciptid_dup1. This program will remove all _dup? entries from a GTF file.
    
    Usage: gtfutils remove_dup filename.gtf
    
