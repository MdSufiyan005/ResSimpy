from dataclasses import dataclass
import re
from typing import Optional

from ResSimpy.Nexus import nexus_file_operations


@dataclass(kw_only=True)
class NexusFile:
    """ Class to deal with origin and structure of Nexus files and preserve origin of include files
    Attributes:
        location (Optional[str]): Path to the original file being opened. Defaults to None.
        includes (Optional[list[str]]): list of file paths that the file contains. Defaults to None.
        origin (Optional[str]): Where the file was opened from. Defaults to None.
        includes_objects (Optional[list['NexusFile']]): The include files but generated as a NexusFile instance. \
            Defaults to None.
    """
    location: Optional[str] = None
    includes: Optional[list[str]] = None
    origin: Optional[str] = None
    includes_objects: Optional[list['NexusFile']] = None
    file_content_as_list: Optional[list] = None

    def __init__(self, location: Optional[str] = None, includes: Optional[list[str]] = None,
                 origin: Optional[str] = None, includes_objects: Optional[list['NexusFile']] = None,
                 file_content_as_list: Optional[list] = None):
        self.location: Optional[str] = location
        self.includes: Optional[list[str]] = includes
        self.origin: Optional[str] = origin
        self.includes_objects: Optional[list['NexusFile']] = includes_objects
        self.file_content_as_list: Optional[list] = file_content_as_list

    @classmethod
    def generate_file_include_structure(cls, file_path: str, origin: Optional[str] = None, recursive: bool = True):
        """generates a nexus file instance for a provided text file with information storing the included files

        Args:
            file_path (str): path to a file
            origin (Optional[str], optional): Where the file was opened from. Defaults to None.

        Returns:
            NexusFile: a class instance for NexusFile with knowledge of include files
        """
        # load file as list and clean up file
        file_as_list = nexus_file_operations.load_file_as_list(file_path)
        file_as_list = nexus_file_operations.strip_file_of_comments(file_as_list)

        # prevent python from mutating the lists that its iterating over
        modified_file_as_list: list = []
        # search for the INCLUDE keyword and append to a list:
        inc_file_list: list[str] = []
        includes_objects: Optional[list] = []
        for line in file_as_list:
            if "INCLUDE" not in line.upper():  # TODO replace with check_token function
                modified_file_as_list.append(line)
                continue
            inc_file_path = nexus_file_operations.get_token_value('INCLUDE', line, [line])
            if inc_file_path is None:
                modified_file_as_list.append(line)
                continue
            # store the included files as files inside the object
            inc_file_list.append(inc_file_path)
            if not recursive:
                modified_file_as_list.append(line)
            else:
                inc_file = cls.generate_file_include_structure(inc_file_path, origin=file_path, recursive=True)
                if includes_objects is None:
                    raise ValueError('includes_objects is None - recursion failure.')
                includes_objects.append(inc_file)

                prefix_line, suffix_line = re.split('INCLUDE', line, maxsplit=1, flags=re.IGNORECASE)
                suffix_line = suffix_line.lstrip()
                suffix_line = suffix_line.replace(inc_file_path, '', 1)
                if prefix_line:
                    modified_file_as_list.append(prefix_line)
                modified_file_as_list.append(inc_file)
                if suffix_line:
                    modified_file_as_list.append(suffix_line)

        includes_objects = None if not includes_objects else includes_objects

        nexus_file_class = cls(
            location=file_path,
            includes=inc_file_list,
            origin=origin,
            includes_objects=includes_objects,
            file_content_as_list=modified_file_as_list,
            )

        return nexus_file_class

    def generate_included_file_objects(self):
        """Builds NexusFile objects for any include files that have been found in the original instance
        """
        # check if there are any includes and exit if not
        if not self.includes:
            return None

        self.includes_objects = []
        for file_path in self.includes:
            inc_file = self.generate_file_include_structure(file_path, origin=self.location)
            self.includes_objects.append(inc_file)

        return self.includes_objects

    def export_network_lists(self):
        """ Exports lists of connections from and to for use in network graphs

        Raises:
            ValueError: If the from and to lists are not the same length
        Returns:
            tuple[list]: list of to and from file paths where the equivalent indexes relate to a connection
        """
        from_list = [self.origin]
        to_list = [self.location]
        if not [self.origin]:
            to_list = []
        if self.includes is not None:
            from_list += [self.location] * len(self.includes)
            to_list += self.includes
        if len(from_list) != len(to_list):
            raise ValueError(f"{from_list=} and {to_list=} are not the same length")

        return from_list, to_list