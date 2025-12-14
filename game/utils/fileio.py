def save_result(player_score, keeper_saves):
    with open("score.txt", "a", encoding="utf-8") as f:
        f.write(f"玩家得分: {player_score}, 守门员扑救成功: {keeper_saves}\n")
