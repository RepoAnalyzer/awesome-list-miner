from github import Github

from awesome_list_miner import md_parser

g = Github()


def get_readme(
    full_name: str = None,
    owner="sindresorhus",
    repo="awesome",
):
    repo = g.get_repo(full_name or f"{owner}/{repo}")

    readme = repo.get_readme()

    return readme


print(get_readme().decoded_content)
html = md_parser.md_to_html(get_readme().decoded_content)
links = md_parser.find_all_links(html)
github_repo_links = filter(lambda link: md_parser.is_github_repo_url(link[1]), links)
for link in github_repo_links:
    print(link)
