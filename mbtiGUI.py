import tkinter as tk
from tkinter import messagebox

# 12가지 질문 정의: (질문, 긍정 답변(1)에 해당하는 지표, 부정 답변(2)에 해당하는 지표)
QUESTIONS = [
    ("1. 처음 만나는 사람들과 이야기하는 것이 즐겁다.", 'E', 'I'),
    ("2. 새로운 아이디어에 대해 공상하는 것을 좋아한다.", 'N', 'S'),
    ("3. 결정을 내릴 때 논리적이고 객관적인 분석을 우선한다.", 'T', 'F'),
    ("4. 할 일을 미리 계획하고 체계적으로 진행하는 것을 선호한다.", 'J', 'P'),

    ("5. 혼자만의 시간보다 다른 사람들과 함께하는 시간을 더 중요하게 생각한다.", 'E', 'I'),
    ("6. 현재의 사실이나 경험을 바탕으로 현실적인 해결책을 찾는 편이다.", 'S', 'N'),
    ("7. 다른 사람의 감정을 공감하고 배려하는 것이 중요하다고 느낀다.", 'F', 'T'),
    ("8. 유동적이고 즉흥적인 상황에 더 잘 적응하고 편안함을 느낀다.", 'P', 'J'),

    ("9. 파티나 모임에서 에너지를 얻고 활력을 되찾는 편이다.", 'E', 'I'),
    ("10. 미래에 대한 비전이나 예측에 관심이 많다.", 'N', 'S'),
    ("11. 비판이나 지적을 할 때, 솔직함이 친절함보다 중요하다고 생각한다.", 'T', 'F'),
    ("12. 마감 기한 직전에 집중해서 일을 처리하는 것을 선호한다.", 'P', 'J'),
]

# MBTI 유형별 간략한 요약 (해설 데이터)
MBTI_SUMMARIES = {
    'ISTJ': "청렴결백한 논리주의자. 철저한 계획과 책임감으로 일을 완수합니다.",
    'ISFJ': "용감한 수호자. 조용하고 헌신적이며 타인에게 봉사하는 것을 즐깁니다.",
    'INFJ': "선의의 옹호자. 통찰력이 뛰어나고 사람들의 성장을 돕는 데 열정적입니다.",
    'INTJ': "용의주도한 전략가. 지적인 호기심이 많고, 복잡한 문제를 해결하는 데 능숙합니다.",
    'ISTP': "만능 재주꾼. 조용하고 관찰력이 뛰어나며, 기계나 도구를 다루는 데 소질이 있습니다.",
    'ISFP': "호기심 많은 예술가. 따뜻하고 유연하며, 자신의 가치를 예술로 표현합니다.",
    'INFP': "열정적인 중재자. 상상력이 풍부하고 이상적이며, 깊은 가치관을 추구합니다.",
    'INTP': "논리적인 사색가. 지식에 대한 끝없는 갈망을 가진 독창적인 문제 해결사입니다.",
    'ESTP': "모험을 즐기는 사업가. 에너지 넘치고 행동파이며, 현장에서 빠르게 대처합니다.",
    'ESFP': "자유로운 영혼의 연예인. 사람들과의 상호작용을 즐기며, 삶을 축제로 만듭니다.",
    'ENFP': "재기발랄한 활동가. 창의적이고 사교적이며, 주변 사람들에게 영감을 줍니다.",
    'ENTP': "뜨거운 논쟁을 즐기는 변론가. 똑똑하고 지적인 도전을 즐기는 능동적인 사고가입니다.",
    'ESTJ': "엄격한 관리자. 체계적이고 전통을 중시하며, 질서를 확립하는 데 뛰어납니다.",
    'ESFJ': "사교적인 외교관. 사람들에게 헌신적이며, 사회적 조화를 중시합니다.",
    'ENFJ': "정의로운 사회운동가. 카리스마 넘치고 타인의 성장을 돕는 데 집중합니다.",
    'ENTJ': "대담한 통솔자. 비전을 제시하고, 사람들을 이끌어 목표를 달성합니다.",
}

# 지표별 상세 설명
INDICATOR_EXPLANATIONS = {
    'E': "외향형 (Extraversion): 에너지를 외부 활동과 사람들과의 관계에서 얻습니다.",
    'I': "내향형 (Introversion): 에너지를 내면의 숙고와 혼자만의 시간에서 얻습니다.",
    'S': "감각형 (Sensing): 현재 사실, 구체적인 정보, 경험에 집중합니다.",
    'N': "직관형 (iNtuition): 미래 가능성, 패턴, 이론과 개념에 집중합니다.",
    'T': "사고형 (Thinking): 논리, 진실, 객관적인 분석을 통해 결정합니다.",
    'F': "감정형 (Feeling): 가치, 타인의 감정, 조화를 고려하여 결정합니다.",
    'J': "판단형 (Judging): 체계적이고 조직적이며, 계획에 따라 생활하는 것을 선호합니다.",
    'P': "인식형 (Perceiving): 유연하고 개방적이며, 상황에 따라 즉흥적인 것을 선호합니다.",
}

class MBTITestApp:
    def __init__(self, master):
        self.master = master
        master.title("🧠 MBTI 간이 검사 (GUI)")
        master.geometry("550x300") # 창 크기 설정

        self.current_q_index = 0
        # 4가지 MBTI 지표를 위한 점수 초기화
        self.scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

        # 1. 질문 레이블 (화면에 질문을 표시)
        self.question_label = tk.Label(master, text="", wraplength=500, font=('Helvetica', 12, 'bold'))
        self.question_label.pack(pady=30)

        # 2. 버튼 프레임 (버튼을 묶는 컨테이너)
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=20)

        # 3. '매우 그렇다' 버튼 (1번 응답)
        self.button_yes = tk.Button(self.button_frame, text="1. 매우 그렇다", 
                                    command=lambda: self.record_answer(1), 
                                    bg='lightblue', font=('Helvetica', 10))
        self.button_yes.pack(side=tk.LEFT, padx=20, ipadx=10, ipady=5)

        # 4. '그렇지 않다' 버튼 (2번 응답)
        self.button_no = tk.Button(self.button_frame, text="2. 그렇지 않다", 
                                   command=lambda: self.record_answer(2), 
                                   bg='lightcoral', font=('Helvetica', 10))
        self.button_no.pack(side=tk.RIGHT, padx=20, ipadx=10, ipady=5)
        
        # 5. 진행 상황 레이블
        self.progress_label = tk.Label(master, text="", font=('Helvetica', 10))
        self.progress_label.pack(pady=10)

        self.display_question()

    def display_question(self):
        """현재 인덱스의 질문을 화면에 표시합니다."""
        if self.current_q_index < len(QUESTIONS):
            q_text = QUESTIONS[self.current_q_index][0]
            # 질문 번호와 함께 질문 내용을 표시
            full_text = f"Q{self.current_q_index + 1}. {q_text}"
            self.question_label.config(text=full_text)
            
            # 진행 상황 업데이트
            progress_text = f"{self.current_q_index + 1} / {len(QUESTIONS)} 진행 중"
            self.progress_label.config(text=progress_text)
        else:
            self.calculate_result()

    def record_answer(self, choice):
        """사용자의 응답을 기록하고 다음 질문으로 넘어갑니다."""
        
        # 현재 질문의 지표 정보 가져오기
        question_data = QUESTIONS[self.current_q_index]
        positive_trait = question_data[1]  # 1번 응답 지표
        negative_trait = question_data[2]  # 2번 응답 지표
        
        # 점수 업데이트
        if choice == 1:
            self.scores[positive_trait] += 1
        else: # choice == 2
            self.scores[negative_trait] += 1
            
        # 다음 질문으로 이동
        self.current_q_index += 1
        self.display_question()

    def calculate_result(self):
        """최종 MBTI 유형을 계산하고 결과를 새 창에 표시합니다."""
        
        # 최종 지표 결정
        e_i = 'E' if self.scores['E'] >= self.scores['I'] else 'I'
        s_n = 'S' if self.scores['S'] >= self.scores['N'] else 'N'
        t_f = 'T' if self.scores['T'] >= self.scores['F'] else 'F'
        j_p = 'J' if self.scores['J'] >= self.scores['P'] else 'P'

        final_mbti = e_i + s_n + t_f + j_p
        
        # 결과 해설 메시지 구성
        summary = MBTI_SUMMARIES.get(final_mbti, "해설을 찾을 수 없습니다.")
        
        explanation = f"1. E/I (에너지 방향): {INDICATOR_EXPLANATIONS[e_i]}\n"
        explanation += f"2. S/N (정보 인식): {INDICATOR_EXPLANATIONS[s_n]}\n"
        explanation += f"3. T/F (의사 결정): {INDICATOR_EXPLANATIONS[t_f]}\n"
        explanation += f"4. J/P (생활 양식): {INDICATOR_EXPLANATIONS[j_p]}\n\n"
        explanation += f"💡 **{final_mbti}** 유형 요약:\n{summary}"

        # 결과 창 (Tkinter Toplevel) 표시
        self.show_result_window(final_mbti, explanation)

    def show_result_window(self, mbti_type, explanation):
        """최종 결과를 보여주는 새 창을 띄웁니다."""
        
        result_window = tk.Toplevel(self.master)
        result_window.title("🌟 검사 결과")
        result_window.geometry("500x350")

        # 제목
        tk.Label(result_window, text="===== 최종 결과 =====", font=('Helvetica', 14, 'bold')).pack(pady=10)
        
        # MBTI 유형
        tk.Label(result_window, text=f"당신의 유형은: {mbti_type}", 
                 font=('Helvetica', 20, 'bold'), fg='blue').pack(pady=10)
        
        # 해설
        tk.Label(result_window, text="--- 지표별 상세 해설 및 요약 ---", 
                 font=('Helvetica', 12, 'underline')).pack(pady=5)
        
        # 해설 내용 (멀티라인으로 표시)
        explanation_text = tk.Text(result_window, height=12, width=60, wrap='word', font=('Helvetica', 10))
        explanation_text.insert(tk.END, explanation)
        explanation_text.config(state=tk.DISABLED) # 텍스트 수정 불가
        explanation_text.pack(pady=10, padx=10)

        # 경고 메시지
        tk.Label(result_window, text="* 이 검사는 간이 검사이므로, 재미로 참고하세요.", 
                 fg='gray', font=('Helvetica', 8)).pack(pady=5)
        
        # 원본 창은 비활성화
        self.master.withdraw() 
        # 결과 창 닫을 때 원본 창도 닫기
        result_window.protocol("WM_DELETE_WINDOW", self.master.destroy)


# 메인 루프 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = MBTITestApp(root)
    root.mainloop()
  