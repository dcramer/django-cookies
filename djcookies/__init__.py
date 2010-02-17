"""
django-cookies
~~~~~~

`django-cookies <http://www.github.com/dcramer/django-cookies>` is a package
that aims to replace the built-in request.COOKIES to add methods to set
and delete cookies without having a response ready.

:copyright: 2010 by David Cramer
"""

__all__ = ('__version__', '__build__', '__docformat__', 'get_revision')
__version__ = (0, 0, 2)
__docformat__ = 'restructuredtext en'

import os

def _get_git_revision(path):
    revision_file = os.path.join(path, 'refs', 'heads', 'master')
    if not os.path.exists(revision_file):
        return None
    fh = open(revision_file, 'r')
    try:
        return fh.read()
    finally:
        fh.close()

def get_revision():
    """
    :returns: Revision number of this branch/checkout, if available. None if
        no revision number can be determined.
    """
    package_dir = os.path.dirname(__file__)
    checkout_dir = os.path.normpath(os.path.join(package_dir, '..'))
    path = os.path.join(checkout_dir, '.git')
    if os.path.exists(path):
        return _get_git_revision(path)
    return None

__build__ = get_revision()