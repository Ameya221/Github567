import requests, json

def repository(ID):
    list = []
    URL = 'https://api.github.com/users/{}/repos'.format(ID)
    data = json.loads(requests.get(URL).text)
    list.append('User: {}'.format(ID))


    try:
        for f in data:
            name = f['name']
            url = 'https://api.github.com/repos/{}/{}/commits'.format(ID, name)
            info = requests.get(url)
            json_info = json.loads(info.text)
            list.append('Repo: {} Number of commits: {}'.format(name, len(json_info)))
    except (TypeError, KeyError, IndexError):
        return 'Error: coudnt fetch the data'
    for i in list:
        print(i)
    return i

repository('Ameya221')
