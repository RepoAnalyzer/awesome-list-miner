import re
from typing import List, Tuple

from bs4 import BeautifulSoup
from markdown import markdown


def md_to_html(markdown_text: str) -> BeautifulSoup:
    html = markdown(markdown_text)
    soup = BeautifulSoup(html)

    return soup


def find_all_links(soup: BeautifulSoup) -> List[Tuple[str, str]]:
    """
    :return: list of links (tuple only consisting of title and href)
    """
    links = soup.find_all("a")

    results = [(link.string, link.get("href")) for link in links]

    return results


def is_github_repo_url(url: str) -> bool:
    """
    Used to remove markdown anchor links, website references... and leave
    only github repositories.

    See [available symbols in github repository name](shorturl.at/ACFG0)
    """
    return bool(re.compile(r"^https?://github.com/[\w.-]+/[\w.-]+").fullmatch(url))
