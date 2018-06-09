import requests
import datetime


def get_trending_repositories(top_size, exactly_days):
    repository_url = 'https://api.github.com/search/repositories'
    date_week_ago = (
            datetime.date.today() -
            datetime.timedelta(exactly_days)
    ).isoformat()
    search_repositories = {
        'q': 'created: > {}'.format(date_week_ago),
        'sort': 'stars',
        'order': 'desc'
    }
    repositories = requests.get(
        repository_url,
        params=search_repositories).json()
    trend_repositories = repositories['items'][:top_size]
    return trend_repositories


def get_open_issues(owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'
    open_issues = requests.get(url.format(owner, repo_name)).json()
    return open_issues


def printer_repositories(repo_name, html_url, issues_count):
    print('The 20 top repositories are:')
    print('Repository: {}'.format(repo_name))
    print('url: {}'.format(html_url))
    print('Issues count: {}'.format(issues_count))


if __name__ == '__main__':
    count_of_repositiries = 20
    days = 7
    most_trending_repository = get_trending_repositories(
        count_of_repositiries,
        days
    )
    for repository in most_trending_repository:
        issues = get_open_issues(
            repository['owner']['login'],
            repository['name']
        )
        printer_repositories(
            repository['name'],
            repository['html_url'],
            len(issues)
        )
