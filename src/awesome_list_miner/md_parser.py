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


def is_web_href(href: str) -> bool:
    return bool(re.compile(r"^https?.*").fullmatch(href))
