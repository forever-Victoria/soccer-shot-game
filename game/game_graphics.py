"""
Turtle图形显示模块：显示球场、球门、守门员和比赛过程
展示：面向对象编程
"""
import turtle
import time

class GameGraphics:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=1200, height=700)
        self.screen.bgcolor("#2d8659")  # 绿色草坪
        self.screen.title("点球大战")
        self.screen.tracer(0)  # 关闭自动刷新，手动控制
        
        # 创建画笔
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        
        # 创建文字显示画笔（用于临时消息）
        self.text_pen = turtle.Turtle()
        self.text_pen.hideturtle()
        self.text_pen.speed(0)
        
        # 创建比分显示画笔（专门用于比分，不会与其他文字混淆）
        self.score_pen = turtle.Turtle()
        self.score_pen.hideturtle()
        self.score_pen.speed(0)
        
        # 创建守门员画笔
        self.gk_pen = turtle.Turtle()
        self.gk_pen.hideturtle()
        self.gk_pen.speed(0)
        
        # 比分
        self.my_score = 0
        self.opponent_score = 0
        self.current_round = 1
        
        # 绘制初始画面
        self.draw_field()
        
    def draw_field(self):
        """绘制球场"""
        self.pen.color("white")
        self.pen.width(3)
        
        # 中间线
        self.pen.up()
        self.pen.goto(0, -350)
        self.pen.down()
        self.pen.goto(0, 350)
        
        # 绘制左侧球门
        self.draw_goal(-550, 0, "left")
        
        # 绘制右侧球门
        self.draw_goal(550, 0, "right")
        
        # 绘制初始比分和轮次
        self.update_score()
        self.update_round_display()
        
        self.screen.update()
    
    def draw_goal(self, x, y, side):
        """绘制球门"""
        self.pen.color("white")
        self.pen.width(4)
        
        # 球门尺寸
        goal_width = 120
        goal_height = 80
        goal_depth = 40
        
        self.pen.up()
        
        if side == "left":
            # 左侧球门（从左侧看）
            # 前门柱
            self.pen.goto(x, y - goal_height/2)
            self.pen.down()
            self.pen.goto(x, y + goal_height/2)
            
            # 横梁
            self.pen.goto(x + goal_depth, y + goal_height/2)
            
            # 后门柱
            self.pen.goto(x + goal_depth, y - goal_height/2)
            
            # 底线
            self.pen.goto(x, y - goal_height/2)
            
            # 球网线
            self.pen.color("#cccccc")
            self.pen.width(1)
            for i in range(5):
                self.pen.up()
                self.pen.goto(x, y - goal_height/2 + (i+1) * goal_height/6)
                self.pen.down()
                self.pen.goto(x + goal_depth, y - goal_height/2 + (i+1) * goal_height/6)
        else:
            # 右侧球门（从右侧看）
            # 前门柱
            self.pen.goto(x, y - goal_height/2)
            self.pen.down()
            self.pen.goto(x, y + goal_height/2)
            
            # 横梁
            self.pen.goto(x - goal_depth, y + goal_height/2)
            
            # 后门柱
            self.pen.goto(x - goal_depth, y - goal_height/2)
            
            # 底线
            self.pen.goto(x, y - goal_height/2)
            
            # 球网线
            self.pen.color("#cccccc")
            self.pen.width(1)
            for i in range(5):
                self.pen.up()
                self.pen.goto(x, y - goal_height/2 + (i+1) * goal_height/6)
                self.pen.down()
                self.pen.goto(x - goal_depth, y - goal_height/2 + (i+1) * goal_height/6)
        
        self.pen.up()
    
    def draw_goalkeeper(self, x, y, side):
        """绘制守门员小人"""
        self.gk_pen.clear()
        self.gk_pen.color("yellow")
        self.gk_pen.width(3)
        
        if side == "left":
            # 左侧守门员
            self.gk_pen.up()
            self.gk_pen.goto(x + 60, y)
            
            # 头部（圆形）
            self.gk_pen.down()
            self.gk_pen.circle(8)
            
            # 身体
            self.gk_pen.up()
            self.gk_pen.goto(x + 60, y - 8)
            self.gk_pen.down()
            self.gk_pen.goto(x + 60, y - 25)
            
            # 左臂
            self.gk_pen.up()
            self.gk_pen.goto(x + 60, y - 15)
            self.gk_pen.down()
            self.gk_pen.goto(x + 50, y - 20)
            
            # 右臂
            self.gk_pen.up()
            self.gk_pen.goto(x + 60, y - 15)
            self.gk_pen.down()
            self.gk_pen.goto(x + 70, y - 20)
            
            # 左腿
            self.gk_pen.up()
            self.gk_pen.goto(x + 60, y - 25)
            self.gk_pen.down()
            self.gk_pen.goto(x + 55, y - 35)
            
            # 右腿
            self.gk_pen.up()
            self.gk_pen.goto(x + 60, y - 25)
            self.gk_pen.down()
            self.gk_pen.goto(x + 65, y - 35)
            
        else:
            # 右侧守门员
            self.gk_pen.up()
            self.gk_pen.goto(x - 60, y)
            
            # 头部（圆形）
            self.gk_pen.down()
            self.gk_pen.circle(8)
            
            # 身体
            self.gk_pen.up()
            self.gk_pen.goto(x - 60, y - 8)
            self.gk_pen.down()
            self.gk_pen.goto(x - 60, y - 25)
            
            # 左臂
            self.gk_pen.up()
            self.gk_pen.goto(x - 60, y - 15)
            self.gk_pen.down()
            self.gk_pen.goto(x - 70, y - 20)
            
            # 右臂
            self.gk_pen.up()
            self.gk_pen.goto(x - 60, y - 15)
            self.gk_pen.down()
            self.gk_pen.goto(x - 50, y - 20)
            
            # 左腿
            self.gk_pen.up()
            self.gk_pen.goto(x - 60, y - 25)
            self.gk_pen.down()
            self.gk_pen.goto(x - 65, y - 35)
            
            # 右腿
            self.gk_pen.up()
            self.gk_pen.goto(x - 60, y - 25)
            self.gk_pen.down()
            self.gk_pen.goto(x - 55, y - 35)
        
        self.screen.update()
    
    def update_score(self):
        """更新比分显示 - 在左上角显示两行比分，每次射门后更新"""
        # 清除之前的比分显示
        self.score_pen.clear()
        self.score_pen.color("white")
        self.score_pen.up()
        
        # 设置左上角位置（屏幕宽度1200，高度700，左上角约在-550, 330）
        score_x = -550
        score_y = 330
        
        # 显示我方比分（第一行）
        self.score_pen.goto(score_x, score_y)
        self.score_pen.write(
            f"我方: {self.my_score}", 
            align="left", 
            font=("Arial", 20, "bold")
        )
        
        # 显示对方比分（第二行，向下偏移30像素）
        self.score_pen.goto(score_x, score_y - 30)
        self.score_pen.write(
            f"对方: {self.opponent_score}", 
            align="left", 
            font=("Arial", 20, "bold")
        )
        
        self.screen.update()
    
    def update_round_display(self):
        """更新轮次显示 - 在顶部中间显示当前轮次"""
        # 清除之前的轮次显示
        self.text_pen.color("white")
        self.text_pen.up()
        
        # 在顶部中间显示轮次
        self.text_pen.goto(0, 300)
        # 用背景色覆盖旧内容
        self.text_pen.color("#2d8659")
        self.text_pen.write(" " * 30, align="center", font=("Arial", 20, "bold"))
        self.text_pen.color("white")
        self.text_pen.write(
            f"第 {self.current_round} 轮", 
            align="center", 
            font=("Arial", 20, "bold")
        )
        
        self.screen.update()
    
    def show_message(self, message, duration=1.5):
        """显示消息"""
        self.text_pen.color("yellow")
        self.text_pen.up()
        self.text_pen.goto(0, -280)
        self.text_pen.write(message, align="center", font=("Arial", 18, "bold"))
        self.screen.update()
        time.sleep(duration)
        self.text_pen.clear()
        self.screen.update()
    
    def animate_shot(self, side, direction, is_goal):
        """动画显示射门"""
        ball = turtle.Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.shapesize(0.5)
        ball.speed(3)
        
        if side == "left":
            # 从左向右射
            start_x = -400
            goal_x = 550
            ball.up()
            ball.goto(start_x, 0)
            ball.showturtle()
            
            # 根据方向调整角度
            if direction == "L":
                target_y = -30
            elif direction == "R":
                target_y = 30
            else:  # C
                target_y = 0
            
            # 移动到球门
            ball.goto(goal_x, target_y)
            
        else:
            # 从右向左射
            start_x = 400
            goal_x = -550
            ball.up()
            ball.goto(start_x, 0)
            ball.showturtle()
            
            # 根据方向调整角度
            if direction == "L":
                target_y = 30
            elif direction == "R":
                target_y = -30
            else:  # C
                target_y = 0
            
            # 移动到球门
            ball.goto(goal_x, target_y)
        
        time.sleep(0.5)
        ball.hideturtle()
        ball.clear()
        
        # 显示结果
        if is_goal:
            self.show_message("⚽ 进球！", 1.5)
        else:
            self.show_message("❌ 被扑出！", 1.5)
    
    def update_round(self, round_num):
        """更新轮次"""
        self.current_round = round_num
        self.update_round_display()
    
    def final_result(self, my_score, opponent_score):
        """显示最终结果"""
        self.text_pen.color("yellow")
        self.text_pen.up()
        self.text_pen.goto(0, 0)
        
        if my_score > opponent_score:
            result_text = f"🎉 恭喜获胜！\n最终比分: {my_score} - {opponent_score}"
        elif my_score < opponent_score:
            result_text = f"😢 遗憾败北\n最终比分: {my_score} - {opponent_score}"
        else:
            result_text = f"🤝 平局！\n最终比分: {my_score} - {opponent_score}"
        
        self.text_pen.write(result_text, align="center", font=("Arial", 24, "bold"))
        self.screen.update()
    
    def close(self):
        """关闭窗口"""
        self.screen.bye()



