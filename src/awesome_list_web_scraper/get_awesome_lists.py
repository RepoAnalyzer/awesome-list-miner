from github import Github, Repository

g = Github()


def get_awesome_lists() -> Repository:
    """Get repos that have awesome-list in topic.

    :return: repos
    """
    repos = g.search_repositories(query='awesome-list in:topics')

    return repos
