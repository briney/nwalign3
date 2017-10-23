#!/usr/bin/env python
# filename: wrappers.py

import sys

from .cnwalign import global_align, global_align_no_matrix, score_alignment


def global_align_wrapper(s1, s2, matrix=None, match=1, gap_open=-1, gap_extend=-1, server=0):
    match = int(match)
    gap_open = int(gap_open)
    gap_extend = int(gap_extend)
    if sys.version_info[0] >= 3:
        s1 = s1.encode()
        s2 = s2.encode()
    a1, a2 = global_align(s1, s2, match, gap_open, gap_extend, matrix)
    return (a1.decode(), a2.decode())


def global_align_no_matrix_wrapper(s1, s2, **kwargs):
    if sys.version_info[0] >= 3:
        s1 = s1.encode()
        s2 = s2.encode()
    a1, a2 = global_align_no_matrix(s1, s2, **kwargs)
    return (a1.decode(), a2.decode())


def score_alignment_wrapper(s1, s2, **kwargs):
    if sys.version_info[0] >= 3:
        s1 = s1.encode()
        s2 = s2.encode()
    score = score_alignment(s1, s2, **kwargs)
    return score
