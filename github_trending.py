import requests
import datetime


def get_trending_repositories(top_size, exactly_days):
    url = 'https://api.github.com/search/repositories'
    period_date = (
         datetime.date.today() -
         datetime.timedelta(exactly_days)).isoformat()
    search_repositories = {
        'q': 'created : > {}'.format(period_date), 'sort': 'stars'
    }
    repositories = requests.get(url, params=search_repositories).json()
    return repositories['items'][:top_size]

if __name__ == '__main__':
    count_of_repositiries = 20
    days = 7
    most_trending_repository = get_trending_repositories(
        count_of_repositiries, days
    )
    for repository in most_trending_repository:
        print('The most 20 trending_repositories are:')
        print('Url:', repository['html_url'],
               'Stars:', repository['stargazers_count'])
        print('Url:', repository['html_url'],
              'open_issues:', repository['open_issues'])
