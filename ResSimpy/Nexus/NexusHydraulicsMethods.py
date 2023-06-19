from dataclasses import dataclass
import os
from typing import Optional, MutableMapping
from ResSimpy.Nexus.DataModels.NexusFile import NexusFile
from ResSimpy.Nexus.DataModels.NexusHydraulicsMethod import NexusHydraulicsMethod
from ResSimpy.Hydraulics import Hydraulics


@dataclass(kw_only=True)
class NexusHydraulicsMethods(Hydraulics):
    """Class for collection of Nexus hydraulics methods.

    Attributes:
        inputs (dict[int, NexusHydraulicsMethod]): Collection of Nexus hydraulics methods, as a dictionary
        files (dict[int, NexusFile]): Dictionary collection of hydraulics files, in Nexus fcs file.
    """

    __inputs: MutableMapping[int, NexusHydraulicsMethod]
    __files: dict[int, NexusFile]
    __properties_loaded: bool = False  # Used in lazy loading

    def __init__(self, inputs: Optional[MutableMapping[int, NexusHydraulicsMethod]] = None,
                 files: Optional[dict[int, NexusFile]] = None) -> None:
        if inputs:
            self.__inputs = inputs
        else:
            self.__inputs: MutableMapping[int, NexusHydraulicsMethod] = {}
        if files:
            self.__files = files
        else:
            self.__files = {}
        super().__init__()

    def __repr__(self) -> str:
        """Pretty printing hydraulics methods."""
        if not self.__properties_loaded:
            self.load_hydraulics_methods()
        printable_str = ''
        for table_num in self.__inputs.keys():
            printable_str += '\n--------------------------------\n'
            printable_str += f'HYD method {table_num}\n'
            printable_str += '--------------------------------\n'
            printable_str += self.__inputs[table_num].__repr__()
            printable_str += '\n'

        return printable_str

    @property
    def inputs(self) -> MutableMapping[int, NexusHydraulicsMethod]:
        if not self.__properties_loaded:
            self.load_hydraulics_methods()
        return self.__inputs

    @property
    def files(self) -> dict[int, NexusFile]:
        return self.__files

    def load_hydraulics_methods(self):
        # Read in hydraulics properties from Nexus hydraulics method files
        if self.__files is not None and len(self.__files) > 0:  # Check if hydraulics files exist
            for table_num in self.__files.keys():  # For each hydraulics property method
                hydraulics_file = self.__files[table_num].location
                if hydraulics_file is None:
                    raise ValueError(f'Unable to find hydraulics file: {hydraulics_file}')
                if os.path.isfile(hydraulics_file):
                    # Create NexusHydraulicsMethod object
                    self.__inputs[table_num] = NexusHydraulicsMethod(file_path=hydraulics_file, input_number=table_num)
                    self.__inputs[table_num].read_properties()  # Populate object with hydraulics props
        self.__properties_loaded = True