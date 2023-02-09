from pathlib import Path

import pytest

from awesome_list_miner.md_parser import find_all_links, is_web_href, md_to_html

script_location = Path(__file__).absolute().parent


def read(file_name: str) -> str:
    f = open(script_location / "__mocks__/" / file_name, "r")
    return f.read()


@pytest.mark.parametrize(
    "markdown,links",
    [
        (
            read("simple.md"),
            [
                ("Table of Contents", "#table-of-contents"),
                ("Simple", "#simple"),
                ("folke/lazy.nvim", "https://github.com/folke/lazy.nvim"),
            ],
        ),
    ],
)
def test_find_all_links(markdown, links):
    assert find_all_links(md_to_html(markdown)) == links


@pytest.mark.parametrize(
    "markdown,links",
    [
        (
            read("simple.md"),
            [
                ("folke/lazy.nvim", "https://github.com/folke/lazy.nvim"),
            ],
        ),
    ],
)
def test_find_all_web_links(markdown, links):
    assert (
        list(
            filter(
                lambda link: is_web_href(link[1]), find_all_links(md_to_html(markdown))
            )
        )
        == links
    )
