import unittest
import leagueSort


class TestleagueSort(unittest.TestCase):

    def test_leagueSort(self):
        print("test_league")
        league_file = open("league.txt", "r")
        content_list = league_file.readlines()
        league_list = []
        for i in range(len(content_list)):
            league_list.append(content_list[i].strip('\n'))

        self.assertEqual(leagueSort.leagueSort(league_list), "pass")

        league_file.close()


if __name__ == '__main__':
    unittest.main()
