"""
GUI界面模块：用于选择球员和门将
展示：异常处理、lambda函数、组合数据类型（列表、字典、集合）
"""
import tkinter as tk
from tkinter import ttk, messagebox

class PlayerSelectionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("点球大战 - 球员选择")
        self.root.geometry("600x800")
        self.root.configure(bg='#f0f0f0')
        
        # 球员列表 - 展示组合数据类型（列表）
        self.all_players = [
            "梅西", "C罗", "哈兰德",
            "德布劳内", "莫德里奇", "姆巴佩", "莱万多夫斯基", "萨拉赫", "德容", "内马尔"
        ]
        
        # 守门员列表
        self.all_goalkeepers = ["诺伊尔", "库尔图瓦", "阿利森"]
        
        # 选择的球员顺序 - 展示组合数据类型（列表）
        self.selected_players = []
        # 选择的守门员
        self.selected_goalkeeper = None
        
        # 存储已选择的球员 - 展示组合数据类型（集合）
        self.used_players = set()
        
        # 创建界面
        self.create_widgets()
        
    def create_widgets(self):
        # 标题
        title_label = tk.Label(
            self.root, 
            text="⚽ 点球大战球员选择", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # 球员选择区域
        player_frame = tk.LabelFrame(
            self.root,
            text="从10名球员中选择5名并排列出场顺序",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0',
            fg='#34495e',
            padx=20,
            pady=15
        )
        player_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # 创建10个下拉选择框
        self.player_combos = []
        
        for i in range(5):
            row_frame = tk.Frame(player_frame, bg='#f0f0f0')
            row_frame.pack(pady=5, fill="x")
            
            label = tk.Label(
                row_frame,
                text=f"第 {i+1} 位:",
                width=8,
                anchor='w',
                bg='#f0f0f0',
                font=("Arial", 10)
            )
            label.pack(side="left", padx=5)
            
            combo = ttk.Combobox(
                row_frame,
                values=["请选择球员"] + self.all_players,
                state="readonly",
                width=25,
                font=("Arial", 10)
            )
            combo.set("请选择球员")
            combo.pack(side="left", padx=5)
            
            # 绑定选择事件 - 使用lambda函数
            combo.bind("<<ComboboxSelected>>", lambda e, idx=i: self.on_player_selected(idx))
            
            self.player_combos.append(combo)
        
        # 守门员选择区域
        keeper_frame = tk.LabelFrame(
            self.root,
            text="选择1名守门员",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0',
            fg='#34495e',
            padx=20,
            pady=15
        )
        keeper_frame.pack(pady=10, padx=20, fill="x")
        
        self.keeper_combo = ttk.Combobox(
            keeper_frame,
            values=["请选择守门员"] + self.all_goalkeepers,
            state="readonly",
            width=30,
            font=("Arial", 11)
        )
        self.keeper_combo.set("请选择守门员")
        self.keeper_combo.pack(pady=10)
        
        # 开始游戏按钮
        start_button = tk.Button(
            self.root,
            text="开始点球大战 ⚽",
            command=self.start_game,
            bg='#27ae60',
            fg='white',
            font=("Arial", 14, "bold"),
            padx=20,
            pady=10,
            cursor="hand2",
            relief="flat"
        )
        start_button.pack(pady=20)
        
    def on_player_selected(self, index):
        """当选择球员时更新其他下拉框的选项 - 使用lambda和组合数据类型"""
        # 更新已使用的球员集合
        self.update_used_players()
        
        # 更新所有下拉框的可用选项
        self.update_all_combos()
    
    def update_used_players(self):
        """更新已选择的球员集合 - 展示集合操作"""
        self.used_players = set()
        for combo in self.player_combos:
            selected = combo.get()
            if selected != "请选择球员":
                self.used_players.add(selected)
    
    def update_all_combos(self):
        """更新所有下拉框的可用选项 - 展示列表推导式和集合操作"""
        # 计算可用球员列表 - 使用列表推导式
        available = [p for p in self.all_players if p not in self.used_players]
        
        # 更新每个下拉框
        for i, combo in enumerate(self.player_combos):
            current = combo.get()
            # 更新选项列表
            options = ["请选择球员"] + available
            # 如果当前选择的球员不在可用列表中，保留它
            if current != "请选择球员" and current in self.all_players:
                if current not in options:
                    options.append(current)
            combo['values'] = options
    
    def start_game(self):
        """验证选择并开始游戏 - 展示异常处理"""
        try:
            # 收集选择的球员 - 使用列表推导式
            self.selected_players = [
                combo.get() for combo in self.player_combos
            ]
            
            # 验证所有位置都已选择
            if "请选择球员" in self.selected_players:
                raise ValueError("请为所有10个位置选择球员！")
            
            # 检查是否有重复 - 使用集合操作
            if len(set(self.selected_players)) != len(self.selected_players):
                raise ValueError("不能选择重复的球员！")
            
            # 检查守门员
            self.selected_goalkeeper = self.keeper_combo.get()
            if self.selected_goalkeeper == "请选择守门员":
                raise ValueError("请选择一名守门员！")
            
            # 关闭GUI并返回
            self.root.quit()
            self.root.destroy()
            
        except ValueError as e:
            messagebox.showerror("选择错误", str(e))
    
    def run(self):
        """运行GUI界面"""
        self.root.mainloop()
        return self.selected_players, self.selected_goalkeeper



