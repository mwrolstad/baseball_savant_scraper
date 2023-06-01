import argparse
import json
import re
import requests

from bs4 import BeautifulSoup


COOKIES = {
    "AMCVS_A65F776A5245B01B0A490D44%40AdobeOrg": "1",
    "s_ecid": "MCMID%7C79561376762042481851150433034797703144",
    "AMCV_A65F776A5245B01B0A490D44%40AdobeOrg": "1099438348%7CMCIDTS%7C19502%7CMCMID%7C79561376762042481851150433034797703144%7CMCAAMLH-1685568541%7C9%7CMCAAMB-1685568541%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1684970941s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.1.0",
    "s_cc": "true",
    "s_sq": "%5B%5BB%5D%5D",
    "_dd_s": "",
}

HEADERS = {
    "authority": "baseballsavant.mlb.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9,ht;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}

BASE_URL = "https://baseballsavant.mlb.com/leaderboard"
REGEX = re.compile("(var data = )(.*)(;\\\n)")


def scrape_stats(statistics: str, type: str, year: str, team: str = None, min: str = "q", proxies: dict = None):
    response = requests.get(
        f"{BASE_URL}/{statistics}",
        params={
            "type": type,
            "year": year,
            "position": "",
            "team": team if team else "",
            "min": min,
        },
        cookies=COOKIES,
        headers=HEADERS,
        proxies=proxies,
    )
    if response.status_code != 200:
        print(f"Bad response code: {response.status_code}")
        print(response.text)
        for stats in stats_scripts:
            print(stats.text)
        return []

    stats_soup = BeautifulSoup(response.text, features="lxml")
    stats_scripts = stats_soup.select("script")

    stats_dicts = [stats.text for stats in stats_scripts if stats.text.strip().startswith("var data =")]

    if len(stats_dicts) == 0:
        print("Could not find the JSON object in response:")
        for stats in stats_scripts:
            print(stats)
        return []

    stats_matches = REGEX.findall(stats_dicts[0])

    return json.loads(stats_matches[0][1])


class StatScraper:
    def __init__(self, statistics: str, type: str, year: str, team: str = "", min: str = "q", proxies: dict = None):
        try:
            self.stats = scrape_stats(statistics, type, year, team, min, proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            self.stats = []


def main(statistics: str, type: str, year: int, team: str = "", min: str = "q"):
    games = StatScraper(statistics, type, year, team, min)
    print(json.dumps(games.stats, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--statistics", required=True, help="The type of statistics we want to grab.", choices=["expected_statistics"]
    )
    parser.add_argument(
        "--type",
        required=True,
        help="The level of granularity of the statistics, either pitchers/batters or teams.",
        choices=[
            "pitcher",
            "batter",
            "pitcher-team",
            "batter-team",
        ],
    )
    parser.add_argument(
        "--year",
        required=True,
        help="The year to grab the data for.",
        default="2023",
    )
    parser.add_argument(
        "--team",
        required=False,
        help="The specific team you'd like to get the stats for. A blank string is all teams.",
        default=None,
    )
    parser.add_argument(
        "--min",
        required=False,
        help="The minimum statistic to filter on.",
        choices=["q", "1", "25", "50", "100", "150", "200"],
        default="q",
    )
    args = parser.parse_args()
    main(args.statistics, args.type, args.year, args.team, args.min)
