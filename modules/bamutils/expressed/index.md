---
layout: templ
title: expressed
module: bamutils
---
    
    Finds regions expressed in a BAM file
    
    This will scan a BAM file, looking for regions of mapped reads. The found
    regions are output in BED format. These regions are found in a model-free
    manner, so they may represent novel or known transcripts. This is also helpful
    for peak-finding in ChIP-seq experiments.
    
    Usage: bamutils expressed {options} bamfile
    
    Options:
    -ns             Ignore strandedness when creating regions
                    (default: false)
    
    -uniq           Only use unique starting positions when performing counts
                    (default: false)
    
    -dist N         minimum distance required between regions - they will be
                    merged if w/in this distance
                    (default: 10)
    
    -mincount N     The minimum number of reads required in a region
                    (default: 2)
    
    
