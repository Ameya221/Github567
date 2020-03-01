import requests, json, unittest
from unittest import mock


class Test(unittest.TestCase):

    @mock.patch('Github_mock.number_commits')
    def test_number_commits(self, mock):
        mock.return_value = 21
        self.assertEqual(number_commits("Ameya221", "Github567"), 21)


def getHub_repo(user):
    result = []
    url = requests.get(f'https://api.github.com/users/{user}/repos')
    list = json.loads(url.text)

    try:
        for line in list:
            repository = line.get("name")
            result.append(repository)
    except ValueError:
        raise ValueError("Error: invalid user id")

    return result


def number_commits(user_name, repo):
    url = requests.get('https://api.github.com/repos/{}/{}/commits'.format(user_name, repo))
    commits = json.loads(url.text)
    return len(commits)


def main():
    user = "Ameya221"

    for repository in getHub_repo(user):
        num = number_commits(user, repository)
        print("Repository: " + repository + ", No of commits: " + num)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()