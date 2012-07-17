---
layout: templ
title: Getting started
---

### Usage

Run the `bamutils`, `bedutils`, `fastqutils`, or `gtfutils` scripts. These are the main driver scripts
for NGSUtils. These scripts setup the virtualenv environment and run the requested command.

For ease of use, it is recommended that you add `bamutils`, `bedutils`, `fastqutils`, and `gtfutils` to your $PATH.

Running `bamutils` (or the others) without any arguments will return a list of commands available.  Running `bamutils command`
will give you the parameters required for that command (or `bedutils`, etc...)

General usage format:

    bamutils command {options} filename

    bedutils command {options} filename 

    fastqutils command {options} filename

    gtfutils command {options} filename

For more information see the individual module documentation:
* [bamutils](/modules/bamutils)
* [bedutils](/modules/bedutils)
* [fastqutils](/modules/fastqutils)
* [gtfutils](/modules/gtfutils)
