import pathlib


def allowed_upload_size(filepath: pathlib.Path, size: int) -> bool:
    '''Takes file pathlib.Path object and compares
    it size with maximum allowed filesize given in Mbytes.'''
    size_in_bytes = size * 1024 * 1024
    return filepath.stat().st_size < size_in_bytes
