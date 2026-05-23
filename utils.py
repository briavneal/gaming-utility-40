import json
from typing import Any, Dict, List

def load_game_data(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_game_data(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def update_player_stats(player_data: Dict[str, Any], stats: Dict[str, Any]) -> Dict[str, Any]:
    player_data['stats'].update(stats)
    return player_data


def get_high_scores(data: List[Dict[str, Any]], top_n: int = 5) -> List[Dict[str, Any]]:
    return sorted(data, key=lambda x: x['score'], reverse=True)[:top_n]


def find_item_by_id(items: List[Dict[str, Any]], item_id: str) -> Dict[str, Any]:
    return next((item for item in items if item['id'] == item_id), None)