import requests
import datetime

number_top_repositories = 20
days_ago = 7

def get_trending_repositories(top_size, exactly_day):
    url = 'https://api.github.com/search/repositories'
    period = (datetime.date.today() - datetime.timedelta(exactly_day))
    load_repositories = {'q':'created:>{}'.format(period), 'sort': 'stars'}
    repositories = requests.get(url,params=load_repositories).json()
    return repositories['items'][:top_size]

if __name__ == '__main__':
    top_repositories = get_trending_repositories(number_top_repositories, days_ago)
    print('The top {} repositories are:     ')
    for repository in top_repositories:
        print('Url:', repository['html_url'],
              'Stars:', repository['stargazers_count'],
              'open_issues', repository['open_issues'])


