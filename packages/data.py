import pandas
from pandas import DataFrame
import tarfile
from typing import Union, BinaryIO

# functions
def read_from_tar(tar_file_path: str,
                  target: str, 
                  method: str = 'default') -> Union[str, BinaryIO]:
    """Reads contents from Tarfile."""
    # get tarfile
    compressed_data = tarfile.open(tar_file_path, 'r')

    # check method
    if method == 'all':
        # create extraction path
        extract_path = '/'.join(tar_file_path.split('/')[:-1])

        # extract all
        compressed_data.extractall(extract_path)

        # set decompressed to tar_file_path - tar.gz + target
        decompressed = extract_path + '/' + target

    # default
    else:
        # now get decompressed
        decompressed = compressed_data.extractfile(target)

    # return fileobject and extension
    return decompressed


def load_jp_census_data() -> DataFrame:
    """Load Japanese Gov Census data."""
    # get file pointer or file path
    fp = read_from_tar('/home/jovyan/work/data/jp_pop.tar.gz', 'jp_pop.csv')
    
    # get dataframe
    return pandas.read_csv(fp)


def jp_prefecture_pop() -> dict[str, int]:
    """Get dictionary of Japanese prefecture population data."""
    # get total census data
    jp_pop = load_jp_census_data()
    
    # get only population data with prefecture as key
    return dict(list(zip(jp_pop.Prefecture, jp_pop.Population)))