from github import ContentFile, Github

g = Github()


def get_readme(
    full_name: str = None,
    owner="sindresorhus",
    repo="awesome",
) -> ContentFile:
    """
    Get readme from a repository.

    Use readme.decoded_content to read raw file.

    :param owner: nickname of the repository owner
    :type owner: str
    :param repo: repository
    :type repo: str
    :param full_name: owner/repo combination (may be easier to parse from urls)
    :return: readme content file, see:
    - [repository content github api docs](shorturl.at/fpW78)
    - [class documentation of PyGithub](http://tny.im/spi1L)
    """
    repo = g.get_repo(full_name or f"{owner}/{repo}")

    readme = repo.get_readme()

    return readme
