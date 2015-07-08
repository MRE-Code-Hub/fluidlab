"""
Laboratory experiments (:mod:`fluidlab`)
============================================

.. _lab:
.. currentmodule:: fluidlab

The package :mod:`fluidlab` contains:

.. autosummary::
   :toctree: generated/

   objects
   exp
   postproc

"""

from fluidlab._version import __version__

from fluidlab.util import load_exp
del util

import fluiddyn as fld
fld.load_exp = load_exp
del fld
