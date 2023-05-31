# baseball_savant_scraper

An easy tool to scrape the current odds listed on bettingdata.com

### Use as a command line:

```cmd
python3 src/baseball_savant_scraper/__init__.py --type "pitcher" --statistics "expected_statistics" --year "2023" --min="25"
```

### Import and use as a package:

```python
from baseball_savant_scraper import StatScraper
import json
stats_scraper = StatScraper(
  statistics="expected_statistics",
  type="pitcher",
  year="2023",
  min="25",
)
print(json.dumps(stats_scraper.stats, indent=2))
[
    {
        "is_qualified": "0",
        "year": "2023",
        "group_type": "0",
        "entity_name": "Then, Juan",
        "entity_id": "672730",
        "entity_team_name": "Mariners",
        "entity_team_name_alt": "SEA",
        "entity_team_id": "136",
        "grouping_code": "Pitcher",
        "pos": null,
        "pos_group": null,
        "pa": "31",
        "bip": "25",
        "launch_angle_avg": "-5.3",
        "sweet_spot_percent": 20,
        "exit_velocity_max": "106.1",
        "exit_velocity_avg": "91",
        "exit_velocity_fbld": "90.3",
        "exit_velocity_gb": "91.5",
        "distance_max": "365",
        "distance_avg": "77",
        "distance_hr_avg": null,
        "hard_hit_ct": "11",
        "hard_hit_percent": 44,
        "hard_hit_per_swing": 25,
        "barrel_ct": "0",
        "barrels_per_bip": 0,
        "barrels_per_pa": 0,
        "barrels_per_swing": 0,
        "ba": 0.241,
        "est_ba": 0.295,
        "slg": 0.241,
        "est_slg": 0.347,
        "woba": 0.245,
        "est_woba": 0.308,
        "wobacon": 0.248,
        "est_wobacon": 0.327,
        "xera": "3.87",
        "era": "3.68",
        "ba_minus_est_ba_diff": -0.05399999999999999,
        "slg_minus_est_slg_diff": -0.10599999999999998,
        "woba_minus_est_woba_diff": -0.063,
        "wobacon_minus_est_wobacon_diff": -0.07900000000000001,
        "era_minus_xera_diff": "-0.188",
        "est_wobacon_minus_wobacon_diff": -0.07900000000000001,
        "est_ba_minus_ba_diff": -0.05399999999999999,
        "est_woba_minus_woba_diff": -0.063,
        "est_slg_minus_slg_diff": -0.10599999999999998,
        "href": "<a href=\"/savant-player/672730\">Then, Juan</a>"
    },
    {
        "is_qualified": "0",
        "year": "2023",
        "group_type": "0",
        "entity_name": "Soriano, George",
        "entity_id": "666277",
        "entity_team_name": "Marlins",
        "entity_team_name_alt": "MIA",
        "entity_team_id": "146",
        "grouping_code": "Pitcher",
        "pos": null,
        "pos_group": null,
        "pa": "30",
        "bip": "25",
        "launch_angle_avg": "11.5",
        "sweet_spot_percent": 44,
        "exit_velocity_max": "106.8",
        "exit_velocity_avg": "89.6",
        "exit_velocity_fbld": "94.3",
        "exit_velocity_gb": "83.5",
        "distance_max": "369",
        "distance_avg": "166",
        "distance_hr_avg": null,
        "hard_hit_ct": "10",
        "hard_hit_percent": 40,
        "hard_hit_per_swing": 20.4,
        "barrel_ct": "2",
        "barrels_per_bip": 8,
        "barrels_per_pa": 6.7,
        "barrels_per_swing": 4.1,
        "ba": 0.259,
        "est_ba": 0.294,
        "slg": 0.296,
        "est_slg": 0.419,
        "woba": 0.266,
        "est_woba": 0.332,
        "wobacon": 0.263,
        "est_wobacon": 0.342,
        "xera": "4.57",
        "era": "2.57",
        "ba_minus_est_ba_diff": -0.034999999999999976,
        "slg_minus_est_slg_diff": -0.123,
        "woba_minus_est_woba_diff": -0.066,
        "wobacon_minus_est_wobacon_diff": -0.07900000000000001,
        "era_minus_xera_diff": "-1.999",
        "est_wobacon_minus_wobacon_diff": -0.07900000000000001,
        "est_ba_minus_ba_diff": -0.034999999999999976,
        "est_woba_minus_woba_diff": -0.066,
        "est_slg_minus_slg_diff": -0.123,
        "href": "<a href=\"/savant-player/666277\">Soriano, George</a>"
    }
]
```
