#!/usr/bin/env python3

import unittest
import sys
import os


if __name__ == '__main__':

  if 'src_dir' not in os.environ:
    os.environ['src_dir'] = os.getcwd() + '/..'
  if 'bin_dir' not in os.environ:
    os.environ['bin_dir'] = os.getcwd()
  src_dir = os.environ['src_dir']
  bin_dir = os.environ['bin_dir']
  for i in [ 'silence', 'fail', 'lockf' ]:
    if i not in os.environ:
      os.environ[i] = bin_dir + '/' + i
  if 'echo' not in os.environ:
    os.environ['echo'] = src_dir + '/test/echo.sh'

  unittest.main(module=None, argv=[sys.argv[0], 'discover',
      '--start-directory',  src_dir + '/test', '--pattern', '*.py',
      ])
      # not necessary, problematic for out-of-source builds:
      # '--top-level-directory', src_dir])


