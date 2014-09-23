---
layout: templ
title: nearest
module: bedutils
---
    
    For each BED region, find the nearest annotated region from a reference file.
    Usage: bedutils nearest {-max val} query.bed reference.bed
    
    Options:
      -max    The maximal distance to look for a nearest region
              (default: 100K)
    
      -match  Only use regions in the reference that contain the name
              from the query file.
    
    
