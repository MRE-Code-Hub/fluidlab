"""Interfaces with pyvisa (:mod:`fluidlab.instruments.interfaces.visa`)
=======================================================================

Provides:

.. autoclass:: PyvisaInterface
   :members:
   :private-members:

"""

import pyvisa as visa

from fluidlab.instruments.interfaces import QueryInterface


class PyvisaInterface(QueryInterface):
    def __init__(self, resource_name, backend='@py'):
        rm = visa.ResourceManager(backend)
        instr = rm.get_instrument(resource_name)
        self._lowlevel = instr
        self.pyvisa_instr = instr
        self.write = instr.write
        self.read = instr.read
        self.query = instr.query
        self.close = instr.close


if __name__ == '__main__':
    interface = PyvisaInterface('ASRL2::INSTR', backend='@sim')
