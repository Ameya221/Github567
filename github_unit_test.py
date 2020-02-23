import unittest

from github import repository


class TestGetRepo(unittest.TestCase):
    def repository(self):

        self.assertEqual(repository(),['User: Ameya221', 'Repo: hello-world Number of commits: 7', 'Repo: Hellow-world Number of commits: 2', 'Repo: HelloWorld Number of commits: 1', 'Repo: Triangle567 Number of commits: 7', 'Repo: Triangle_testing Number of commits: 1'] )

        self.assertEqual(repository('safdjs'), 'Error: coudnt fetch the data')
