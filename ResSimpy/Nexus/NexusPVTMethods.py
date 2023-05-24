from dataclasses import dataclass
import os
from typing import Optional, MutableMapping
from ResSimpy.Nexus.DataModels.NexusFile import NexusFile
from ResSimpy.Nexus.DataModels.NexusPVTMethod import NexusPVTMethod
from ResSimpy.PVTMethods import PVTMethods


@dataclass(kw_only=True)
class NexusPVTMethods(PVTMethods):
    """Class for collection of Nexus PVT property methods
    Attributes:
        pvt_methods (dict[int, NexusPVTMethod]): Collection of Nexus PVT property methods, as a dictionary
        pvt_files (dict[int, NexusFile]): Dictionary collection of PVT property files, as defined in Nexus fcs file
    """

    __pvt_methods: MutableMapping[int, NexusPVTMethod]
    __pvt_files: dict[int, NexusFile]
    __properties_loaded: bool = False  # Used in lazy loading

    def __init__(self, pvt_methods: Optional[MutableMapping[int, NexusPVTMethod]] = None,
                 pvt_files: Optional[dict[int, NexusFile]] = None):
        if pvt_methods:
            self.__pvt_methods = pvt_methods
        else:
            self.__pvt_methods: MutableMapping[int, NexusPVTMethod] = {}
        if pvt_files:
            self.__pvt_files = pvt_files
        else:
            self.__pvt_files = {}
        super().__init__()

    def __repr__(self) -> str:
        """Pretty printing pvt methods"""
        if not self.__properties_loaded:
            self.load_pvt_methods()
        printable_str = ''
        for table_num in self.__pvt_methods.keys():
            printable_str += '\n--------------------------------\n'
            printable_str += f'PVT method {table_num}\n'
            printable_str += '--------------------------------\n'
            printable_str += self.__pvt_methods[table_num].__repr__()
            printable_str += '\n'

        return printable_str

    @property
    def pvt_methods(self) -> MutableMapping[int, NexusPVTMethod]:
        if not self.__properties_loaded:
            self.load_pvt_methods()
        return self.__pvt_methods

    @property
    def pvt_files(self) -> dict[int, NexusFile]:
        return self.__pvt_files

    def load_pvt_methods(self):
        # Read in pvt properties from Nexus pvt method files
        if self.__pvt_files is not None and len(self.__pvt_files) > 0:  # Check if pvt files exist
            for table_num in self.__pvt_files.keys():  # For each pvt property method
                pvt_file = self.__pvt_files[table_num].location
                if pvt_file is None:
                    raise ValueError(f'Unable to find pvt file: {pvt_file}')
                if os.path.isfile(pvt_file):
                    # Create NexusPVTMethod object
                    self.__pvt_methods[table_num] = NexusPVTMethod(file_path=pvt_file, method_number=table_num)
                    self.__pvt_methods[table_num].read_properties()  # Populate object with pvt properties in file
        self.__properties_loaded = True