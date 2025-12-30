import tkinter as tk
from tkinter import ttk
import time

# 导入核心起卦模块
from zhouyi_core import qi_gua, symbol

class ZhouYiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("周易起卦程序")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # 设置字体
        self.font_title = ("SimHei", 16, "bold")
        self.font_normal = ("SimHei", 12)
        self.font_gua = ("SimHei", 18, "bold")
        self.font_yao = ("SimHei", 20)
        
        # 创建界面组件
        self.create_widgets()
        
    def create_widgets(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        title_label = ttk.Label(main_frame, text="周易起卦", font=self.font_title)
        title_label.pack(pady=20)
        
        # 起卦按钮
        self.gua_button = ttk.Button(main_frame, text="开始起卦", command=self.generate_gua)
        self.gua_button.pack(pady=20)
        
        # 提示信息
        tips_label = ttk.Label(main_frame, text="心诚则灵", font=self.font_normal, foreground="#666666")
        tips_label.pack(pady=10)
        
        # 卦象显示区域
        gua_frame = ttk.LabelFrame(main_frame, text="本卦（下→上）", padding="10")
        gua_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 创建爻象显示区域
        self.yao_frames = []
        # 从下往上创建爻象显示区域（初爻在最下面）
        for i in range(5, -1, -1):
            yao_frame = ttk.Frame(gua_frame)
            yao_frame.pack(fill=tk.X, pady=5)
            
            # 爻位标签（1爻到6爻）
            yao_label = ttk.Label(yao_frame, text=f"{i+1}爻", width=5, font=self.font_normal)
            yao_label.pack(side=tk.LEFT, padx=10)
            
            # 爻象符号
            symbol_label = ttk.Label(yao_frame, text="", font=self.font_yao, foreground="#333333")
            symbol_label.pack(side=tk.LEFT, padx=20)
            
            # 爻数值
            value_label = ttk.Label(yao_frame, text="", font=self.font_normal)
            value_label.pack(side=tk.LEFT, padx=20)
            
            # 是否变爻
            change_label = ttk.Label(yao_frame, text="", font=self.font_normal, foreground="#FF0000")
            change_label.pack(side=tk.LEFT, padx=20)
            
            # 存储框架引用，索引0对应1爻（最下面），索引5对应6爻（最上面）
            self.yao_frames.insert(0, {
                "symbol": symbol_label,
                "value": value_label,
                "change": change_label
            })
    
    def generate_gua(self):
        """生成卦象并显示结果"""
        # 禁用按钮防止重复点击
        self.gua_button.config(state=tk.DISABLED)
        self.gua_button.config(text="正在起卦...")
        self.root.update()
        
        # 模拟起卦过程的延迟
        time.sleep(1)
        
        # 调用核心模块生成卦象
        gua = qi_gua()
        
        # 显示结果
        for i, (frame, value) in enumerate(zip(self.yao_frames, gua)):
            # 更新爻象符号
            frame["symbol"].config(text=symbol(value))
            
            # 更新爻数值
            frame["value"].config(text=str(value))
            
            # 更新是否变爻
            if value in (6, 9):
                frame["change"].config(text="(变)")
            else:
                frame["change"].config(text="")
        
        # 恢复按钮状态
        self.gua_button.config(text="开始起卦")
        self.gua_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZhouYiGUI(root)
    root.mainloop()