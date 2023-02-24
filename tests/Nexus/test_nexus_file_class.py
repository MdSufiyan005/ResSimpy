from typing import Union

import pytest
from ResSimpy.Nexus.DataModels.NexusFile import NexusFile

from tests.multifile_mocker import mock_multiple_files


def mock_different_includes(mocker, filename, test_file_contents, inc_file_content1, inc_file_content2='',
                            ):
    """Mock method that returns different test file contents depending upon the model"""
    if "test_file_path" in filename:
        file_contents = test_file_contents
    elif "inc_file1" in filename:
        file_contents = inc_file_content1
    elif "inc_file2" in filename:
        file_contents = inc_file_content2
    else:
        raise FileNotFoundError(filename)
    open_mock = mocker.mock_open(read_data=file_contents)
    return open_mock


def test_generate_file_include_structure_basic(mocker):
    # Arrange
    file_path = 'test_file_path.dat'
    test_file_contents = 'basic_file INCLUDE inc_file1.inc'
    include_file_contents = 'inc file contents'

    expected_includes_list = ['inc_file1.inc']
    expected_location = 'test_file_path.dat'
    expected_origin = None

    nexus_file_include1 = NexusFile(location='inc_file1.inc', includes=[], origin=file_path,
                                    includes_objects=None, file_content_as_list=[include_file_contents])

    expected_file_content_as_list = ['basic_file ', nexus_file_include1]

    expected_nexus_file = NexusFile(location=expected_location, includes=expected_includes_list,
                                    origin=expected_origin, includes_objects=[nexus_file_include1],
                                    file_content_as_list=expected_file_content_as_list)

    def mock_open_wrapper(filename, mode):
        mock_open = mock_multiple_files(mocker, filename, potential_file_dict={
            'test_file_path.dat': test_file_contents,
            'inc_file1.inc': include_file_contents,
        }
                                        ).return_value
        return mock_open

    mocker.patch("builtins.open", mock_open_wrapper)
    # Act
    nexus_file = NexusFile.generate_file_include_structure(file_path)

    # Assert
    assert nexus_file == expected_nexus_file


def test_generate_file_include_structure_multiple_includes(mocker):
    # Arrange
    file_path = 'test_file_path.dat'
    test_file_contents = (
'''basic_file INCLUDE inc_file1.inc
second_file INCLUDE inc_file2.inc''')
    include_file_contents = 'inc file contents'
    include_file_contents_2 = 'inc2 file contents'

    expected_includes_list = ['inc_file1.inc', 'inc_file2.inc']
    expected_location = 'test_file_path.dat'
    expected_origin = None

    nexus_file_include1 = NexusFile(location='inc_file1.inc', includes=[], origin=file_path,
                                    includes_objects=None, file_content_as_list=[include_file_contents])
    nexus_file_include2 = NexusFile(location='inc_file2.inc', includes=[], origin=file_path,
                                    includes_objects=None, file_content_as_list=[include_file_contents_2])
    expected_file_content_as_list = ['basic_file ', nexus_file_include1, '\n', 'second_file ', nexus_file_include2]

    expected_nexus_file = NexusFile(location=expected_location, includes=expected_includes_list,
                                    origin=expected_origin, includes_objects=[nexus_file_include1, nexus_file_include2],
                                    file_content_as_list=expected_file_content_as_list)

    def mock_open_wrapper(filename, mode):
        mock_open = mock_multiple_files(mocker, filename, potential_file_dict={
            'test_file_path.dat': test_file_contents,
            'inc_file1.inc': include_file_contents,
            'inc_file2.inc': include_file_contents_2,
        }).return_value
        return mock_open
    mocker.patch("builtins.open", mock_open_wrapper)
    # Act
    nexus_file = NexusFile.generate_file_include_structure(file_path)

    # Assert
    assert nexus_file == expected_nexus_file


def test_generate_file_include_structure_nested_includes(mocker):
    # Arrange
    file_path = 'test_file_path.dat'
    test_file_contents = 'basic_file INCLUDE inc_file1.inc'

    include_file_contents = 'inc file contents INCLUDE inc_file2.inc'
    include_file_contents_2 = 'inc2 file contents'

    expected_includes_list = ['inc_file1.inc']
    expected_location = 'test_file_path.dat'
    expected_origin = None

    nexus_file_include2 = NexusFile(location='inc_file2.inc', includes=[], origin='inc_file1.inc',
                                    includes_objects=None, file_content_as_list=[include_file_contents_2])
    nexus_file_include1 = NexusFile(location='inc_file1.inc', includes=['inc_file2.inc'], origin=file_path,
                                    includes_objects=[nexus_file_include2],
                                    file_content_as_list=['inc file contents ', nexus_file_include2])

    expected_file_content_as_list = ['basic_file ', nexus_file_include1]

    expected_nexus_file = NexusFile(location=expected_location, includes=expected_includes_list,
                                    origin=expected_origin, includes_objects=[nexus_file_include1],
                                    file_content_as_list=expected_file_content_as_list)

    def mock_open_wrapper(filename, mode):
        mock_open = mock_multiple_files(mocker, filename, potential_file_dict={
            'test_file_path.dat': test_file_contents,
            'inc_file1.inc': include_file_contents,
            'inc_file2.inc': include_file_contents_2,
        }).return_value
        return mock_open

    mocker.patch("builtins.open", mock_open_wrapper)
    # Act
    nexus_file = NexusFile.generate_file_include_structure(file_path)

    # Assert
    assert nexus_file == expected_nexus_file


def test_iterate_line():
    # Arrange
    expected_flat_list = ['fcs_file content', 'hello', 'world', 'footer']

    include_file = NexusFile(location='inc_file1.inc', includes=[], origin='test_file.dat',
                             includes_objects=None, file_content_as_list=['hello', 'world'])
    nested_list: list[Union[str, NexusFile]] = ['fcs_file content', include_file, 'footer']
    nexus_file = NexusFile(location='test_file.dat', includes=['inc_file1.inc'], origin=None,
                           includes_objects=[include_file], file_content_as_list=nested_list)

    # Act
    store_list = []
    for line in NexusFile.iterate_line(nexus_file.file_content_as_list):
        store_list.append(line)

    # Assert
    assert store_list == expected_flat_list


@pytest.mark.parametrize("max_depth, expected_results", [
    (0, ['fcs_file content', 'footer']),
    (1, ['fcs_file content', 'hello', 'world', 'footer']),
    (2, ['fcs_file content', 'hello', 'deeper', 'nesting', 'world', 'footer']),
    (None, ['fcs_file content', 'hello', 'deeper', 'nesting', 'world', 'footer'])
], ids=['0 depth', '1 layer', '2 layers', 'all layers'])
def test_iterate_line_nested(max_depth, expected_results):
    # Arrange
    inc_2 = NexusFile(location='inc2.inc', includes=[], origin='inc_file1.inc',
                      includes_objects=None, file_content_as_list=['deeper', 'nesting'])
    include_file = NexusFile(location='inc_file1.inc', includes=[], origin='test_file.dat',
                             includes_objects=[inc_2], file_content_as_list=['hello', inc_2, 'world'])

    nested_list: list[Union[str, NexusFile]] = ['fcs_file content', include_file, 'footer']
    nexus_file = NexusFile(location='test_file.dat', includes=['inc_file1.inc'], origin=None,
                           includes_objects=[include_file], file_content_as_list=nested_list)

    # Act
    store_results = []
    for line in NexusFile.iterate_line(nexus_file.file_content_as_list, max_depth=max_depth):
        store_results.append(line)
    # Assert
    assert store_results == expected_results