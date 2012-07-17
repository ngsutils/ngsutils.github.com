---
layout: templ
title: Getting started
---

Usage
---
Run the `bamutils`, `bedutils`, `fastqutils`, or `gtfutils` scripts. These are the main driver scripts 
that setup the appropriate environment (loading pysam) and run the requested command.

For ease of use, it is recommended that you add `bamutils`, `bedutils`, `fastqutils`, and `gtfutils` to your $PATH.

Running `bamutils` without any arguments will return a list of commands available.  Running `bamutils command`
will give you the parameters required for that command (or `bedutils`, etc...)

General usage format:

`bamutils command {options} filename`  

`bedutils command {options} filename`  

`fastqutils command {options} filename`  

`gtfutils command {options} filename`  
