import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("بازی تست هوش")
        self.root.geometry("500x400")
        
        self.questions = [
            ("عمیق ترین نقطه خلیج فارس چند متر است؟", "93متر", ["103متر", "123متر", "93متر", "230متر"]),
            ("در زمان کدام پادشاه، بحرین از خاک ایران جدا شد؟", "محمد رضا پهلوی", ["محمد رضا پهلوی", "ناصرالدین شاه", "مظفرالدین شاه", "شاه اسماعیل"]),
            ("کدام ورزشکار رکورد دار بیشترین مدال در تاریخ المپیک است؟", "مایکل فلپس", ["یوسین بولت", "حسین رضا زاده", "بن جانسن", "مایکل فلپس"]),
            ("کدام کتاب اثر ویکتور هوگو نیست؟", "سپید دندان", ["سپید دندان", "روح انسان", "مردی که میخندد", "بینوایان"]),
            ("کدام کشور سه زبان رسمی دارد؟", "بلژیک", ["بلژیک", "کانادا", "سوییس", "سنگاپور"]),
            ("کوتاه ترین مرز خاکی مشترک ایران با چه کشوری است؟", "ارمنستان", ["آذربایجان", "ارمنستان", "ترکیه", "ترکمنستان"]),
            ("بریانی غذای معروف کدام شهر است؟", "اصفهان", ["اصفهان", "تبریز", "مشهد", "یزد"]),
            ("به کدام یک عروس کوه های ایران می گویند؟", "دنا", ["دنا", "سهند", "سبلان", "دماوند"]),
            ("تعداد خانه های زمین شطرنج چه تعداد است؟", "64", ["64", "36", "81", "49"]),
            ("باهوش ترین حیوان جهان کدام است؟", "شامپانزه", ["موش", "سگ", "فیل", "شامپانزه"]),
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.font_large = ("Helvetica", 14)
        
        self.name_label = tk.Label(root, text="اسم خود را وارد کنید:", font=self.font_large)
        self.name_label.pack()
        
        self.name_entry = tk.Entry(root, font=self.font_large)
        self.name_entry.pack()
        
        self.start_button = tk.Button(root, text="شروع", font=self.font_large, command=self.start_quiz)
        self.start_button.pack()
        
        self.question_label = tk.Label(root, text="", font=self.font_large)
        self.option_buttons = []
        for _ in range(4):
            btn = tk.Button(root, text="", font=self.font_large, command=lambda b=_: self.check_answer(b))
            self.option_buttons.append(btn)
        
        self.score_label = tk.Label(root, text=f"امتیاز: {self.score}", font=self.font_large)
        
    def start_quiz(self):
        self.username = self.name_entry.get()
        if not self.username:
            messagebox.showwarning("هشدار", "لطفا نام خود را وارد کنید")
            return
        
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        
        self.question_label.pack(pady=20)
        for btn in self.option_buttons:
            btn.pack(fill='x', padx=20, pady=5)
        self.score_label.pack(pady=10)
        
        self.show_question()
        
    def show_question(self):
        if self.current_question < len(self.questions):
            q_text, _, options = self.questions[self.current_question]
            self.question_label.config(text=q_text)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
            self.score_label.config(text=f"امتیاز: {self.score}")
        else:
            self.end_quiz()
    
    def check_answer(self, btn_index):
        _, correct_answer, options = self.questions[self.current_question]
        if options[btn_index] == correct_answer:
            self.score += 1
        
        self.current_question += 1
        self.show_question()
        
    def end_quiz(self):
        self.question_label.pack_forget()
        for btn in self.option_buttons:
            btn.pack_forget()
        self.score_label.pack_forget()
        
        half_score = len(self.questions) / 2
        if self.score > half_score:
            result_text = f"آفرین {self.username}! امتیاز شما: {self.score} از {len(self.questions)}. خوب بودی!"
        elif self.score == half_score:
            result_text = f"بدک نبود {self.username}! امتیاز شما: {self.score} از {len(self.questions)}."
        else:
            result_text = f"نیاز به تلاش بیشتری داری {self.username}! امتیاز شما: {self.score} از {len(self.questions)}."
        
        messagebox.showinfo("نتیجه", result_text)
        
        self.play_again_button = tk.Button(self.root, text="بازی مجدد", font=self.font_large, command=self.reset_quiz)
        self.play_again_button.pack(pady=20)
    
    def reset_quiz(self):
        self.play_again_button.pack_forget()
        self.current_question = 0
        self.score = 0
        self.name_label.pack()
        self.name_entry.pack()
        self.start_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
