from threading import Thread
import os
from helpers import check_filename
from datetime import datetime

"""
Author
    Ahtesham Zaidi
    
"""


def download_files(links: list) -> None:
    """
    Downloads all the links in the list asynchronously using separate threads.

    Args:
        links (list): A list of links to download.

    Returns:
        None
    """
    for link in links:
        """Iterates through all links in the links list and downloads them asynchronously."""
        Thread(target=download, args=(link,)).start()


def download(link: str) -> None:
    """
    Downloads a single file from the given link.

    Args:
        link (str): The link to the file to download.

    Returns:
        None
    """
    try:

        filename = link.split("/")[-1]
        cmd = rf'curl {link} --output {filename}'

        if not check_filename(filename):
            filename = f"get_file_{datetime.now().time().strftime('%H_%M_%S')}"
            if 'img' in link or 'photo' in link:
                filename += ".png"
            cmd = rf"""curl "{link}" --output "{filename}" """

        print(f'Downloading file :: {link} ..... \n')
        os.system(cmd)
        print(f'Downloading finished :: {link} ..... \n')

    except:
        print("Something is wrong with the download link")


if __name__ == "__main__":
    download('www.ex.com')
    download_files(['https://example.com/file1.mp3',
                   'https://example.com/file2.mp3', 'https://example.com/file.pdf'])
