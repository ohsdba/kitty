#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPL v3 Copyright: 2018, Kovid Goyal <kovid at kovidgoyal.net>


import os
import subprocess
import shutil

docs_dir = os.path.dirname(os.path.abspath(__file__))
publish_dir = os.path.join(os.path.dirname(os.path.dirname(docs_dir)), 'kovidgoyal.github.io', 'kitty')

subprocess.check_call(['make', 'html'], cwd=docs_dir)
if os.path.exists(publish_dir):
    shutil.rmtree(publish_dir)
shutil.copytree(os.path.join(docs_dir, '_build', 'html'), publish_dir)
os.chdir(os.path.dirname(publish_dir))
subprocess.check_call(['git', 'add', 'kitty'])
subprocess.check_call(['git', 'commit', '-m', 'kitty website updates'])
subprocess.check_call(['git', 'push'])
