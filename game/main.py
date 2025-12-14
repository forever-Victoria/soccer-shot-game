"""
点球大战主程序
展示：异常处理、lambda函数、组合数据类型、面向对象编程、
     模块与包、文件读写
"""
import random
import time
from typing import List, Tuple
import tkinter as tk
from tkinter import messagebox, simpledialog

# 模块导入 - 展示模块与包
from game_gui import PlayerSelectionGUI
from game_graphics import GameGraphics

class PenaltyGame:
    """点球游戏类 - 展示面向对象编程"""
    
    def __init__(self):
        # 使用组合数据类型（列表）存储游戏数据
        self.my_players: List[str] = []
        self.my_goalkeeper = None
        self.my_score = 0
        self.opponent_score = 0
        self.rounds = 5
        
        # 使用元组存储射门方向映射 - 展示组合数据类型（元组）
        self.direction_map: Tuple[str, str, str] = ("L", "C", "R")
        
    def select_team(self) -> Tuple[List[str], str]:
        """选择球员和守门员 - 展示异常处理"""
        try:
            gui = PlayerSelectionGUI()
            players, goalkeeper = gui.run()
            
            if not players or len(players) != 5:
                raise ValueError("必须选择5名球员")
            if not goalkeeper:
                raise ValueError("必须选择一名守门员")
            
            self.my_players = players
            self.my_goalkeeper = goalkeeper
            return players, goalkeeper
            
        except Exception as e:
            print(f"选择过程出错: {e}")
            raise
    
    def validate_direction(self, direction: str) -> str:
        """验证射门方向 - 展示lambda函数和异常处理"""
        try:
            direction = direction.strip().upper() if direction else ""
            
            # 使用lambda函数验证方向 - 展示lambda函数
            is_valid = lambda d: d in self.direction_map
            if not is_valid(direction):
                raise ValueError(f"无效方向: {direction}，必须是 L、C 或 R")
            
            return direction
        except (AttributeError, TypeError) as e:
            raise ValueError(f"方向验证失败: {e}")
    
    def player_shoot(self, player_name: str, graphics: GameGraphics) -> bool:
        """玩家射门 - 展示异常处理、lambda函数"""
        root = tk.Tk()
        root.withdraw()
        
        try:
            direction = None
            while True:
                try:
                    direction = simpledialog.askstring(
                        "射门方向",
                        f"{player_name} 请选择射门方向:\nL - 左侧\nC - 中间\nR - 右侧",
                        parent=root
                    )
                    
                    if direction is None:
                        root.destroy()
                        return False
                    
                    direction = self.validate_direction(direction)
                    break
                    
                except ValueError as e:
                    messagebox.showerror("输入错误", str(e))
            
            root.destroy()
            
            # 对方守门员随机猜测方向
            keeper_guess = random.choice(list(self.direction_map))
            
            # 判断是否进球 - 使用lambda函数
            is_goal_func = lambda d, g: d != g
            is_goal = is_goal_func(direction, keeper_guess)
            
            # 显示射门动画
            graphics.show_message(
                f"{player_name} 射向: {direction}\n对方守门员扑向: {keeper_guess}", 
                2
            )
            graphics.draw_goalkeeper(550, 0, "right")  # 显示对方守门员
            time.sleep(0.5)
            graphics.animate_shot("left", direction, is_goal)
            
            if is_goal:
                self.my_score += 1
                graphics.my_score = self.my_score
                graphics.update_score()  # 更新比分
            
            return is_goal
            
        except tk.TclError as e:
            print(f"GUI错误: {e}")
            root.destroy()
            return False
        except Exception as e:
            print(f"射门过程中发生错误: {e}")
            root.destroy()
            return False
    
    def opponent_shoot(self, graphics: GameGraphics) -> bool:
        """对方射门 - 展示异常处理、lambda函数"""
        # 对方随机选择方向
        opponent_dir = random.choice(list(self.direction_map))
        
        root = tk.Tk()
        root.withdraw()

        keeper_dir = None
        try:
            while True:
                try:
                    keeper_dir = simpledialog.askstring(
                        "守门",
                        f"你控制的守门员 {self.my_goalkeeper} 请选择扑救方向:\nL - 左侧\nC - 中间\nR - 右侧",
                        parent=root
                    )
                    if keeper_dir is None:
                        root.destroy()
                        return False
                    keeper_dir = self.validate_direction(keeper_dir)
                    break
                except ValueError as e:
                    messagebox.showerror("输入错误", str(e))
            

                    if keeper_dir is None:
                        root.destroy()
                        return False

                    keeper_dir = self.validate_direction(keeper_dir)
                    break
                    
                except ValueError as e:
                    messagebox.showerror("输入错误", str(e))

            root.destroy()
                # 使用lambda函数判断是否进球 - 展示lambda函数
            is_goal = (lambda d, g: d != g)(opponent_dir, keeper_dir)
            
            # 显示射门动画
            graphics.show_message(
                f"对方射向: {opponent_dir}\n{self.my_goalkeeper} 扑向: {keeper_dir}", 
                2
            )
            graphics.draw_goalkeeper(-550, 0, "left")  # 显示我方守门员
            time.sleep(0.5)
            graphics.animate_shot("right", opponent_dir, is_goal)
            
            if is_goal:
                self.opponent_score += 1
                graphics.opponent_score = self.opponent_score
                graphics.update_score()  # 更新比分
            
            return is_goal
        except tk.TclError as e:
            print(f"GUI错误: {e}")
            root.destroy()
            return False
        except Exception as e:
            print(f"守门过程中发生错误: {e}")
            root.destroy()
            return False
    
    def play_game(self, graphics: GameGraphics) -> Tuple[int, int]:
        """进行点球大战 - 展示异常处理和组合数据类型"""
        graphics.my_score = 0
        graphics.opponent_score = 0
        graphics.update_score()  # 初始化比分显示
        
        try:
            for round_num in range(1, self.rounds + 1):
                graphics.update_round(round_num)
                
                # 我方射门
                graphics.show_message(f"第 {round_num} 轮 - 我方射门", 1.5)
                player_name = self.my_players[round_num - 1]
                graphics.show_message(f"{player_name} 准备射门", 1)
                try:
                    self.player_shoot(player_name, graphics)
                except Exception as e:
                    print(f"射门出错: {e}")
                    continue
                
                time.sleep(1)
                
                # 对方射门
                graphics.show_message(f"第 {round_num} 轮 - 对方射门", 1.5)
                graphics.show_message(f"对方球员准备射门", 1)
                try:
                    self.opponent_shoot(graphics)
                except Exception as e:
                    print(f"守门出错: {e}")
                    continue
                
                time.sleep(1)
            
            # 显示最终结果
            graphics.final_result(self.my_score, self.opponent_score)
            
            return self.my_score, self.opponent_score
            
        except Exception as e:
            print(f"游戏过程中发生错误: {e}")
            raise

def save_game_result(my_score: int, opponent_score: int, players: List[str], goalkeeper: str):
    """保存游戏结果 - 展示文件读写"""
    try:
        with open("score.txt", "a", encoding="utf-8") as f:
            f.write(f"\n=== 点球大战结果 ===\n")
            f.write(f"比分: 我方 {my_score} - {opponent_score} 对方\n")
            f.write(f"球员: {', '.join(players)}\n")
            f.write(f"守门员: {goalkeeper}\n")
        print(f"\n结果已保存到 score.txt")
    except Exception as e:
        print(f"保存文件时出错: {e}")

def main():
    """主函数 - 展示异常处理、文件读写"""
    print("=== 点球大战游戏 ===")
    
    graphics = None
    game = None
    
    try:
        # 创建游戏实例
        game = PenaltyGame()
        
        # 选择球员和守门员
        print("\n请在弹出的窗口中选择球员和守门员...")
        try:
            players, goalkeeper = game.select_team()
            print(f"\n已选择球员: {players}")
            print(f"已选择守门员: {goalkeeper}")
        except Exception as e:
            print(f"选择过程出错: {e}")
            return
        except KeyboardInterrupt:
            print("\n用户中断选择")
            return
        
        # 初始化图形界面
        try:
            graphics = GameGraphics()
            time.sleep(1)
        except Exception as e:
            print(f"图形界面初始化失败: {e}")
            raise
        
        # 显示初始画面和提示
        graphics.show_message("点球大战开始！", 2)
        graphics.draw_goalkeeper(550, 0, "right")  # 显示对方守门员
        
        # 开始游戏
        try:
            my_score, opp_score = game.play_game(graphics)
            
            # 保存结果到文件 - 展示文件读写
            save_game_result(my_score, opp_score, players, goalkeeper)
            
            print(f"\n=== 比赛结束 ===")
            print(f"最终比分: 我方 {my_score} - {opp_score} 对方")
            
            # 保持窗口打开
            if graphics:
                graphics.screen.mainloop()
            
        except KeyboardInterrupt:
            print("\n用户中断游戏")
        except Exception as e:
            print(f"游戏过程中发生错误: {e}")
            import traceback
            traceback.print_exc()
    
    except Exception as e:
        print(f"程序执行出错: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # 清理资源 - 展示异常处理的finally块
        try:
            if graphics:
                pass  # graphics会在mainloop中保持
        except Exception as e:
            print(f"清理资源时出错: {e}")

if __name__ == "__main__":
    main()
