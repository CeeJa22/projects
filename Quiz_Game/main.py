from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from prettytable import PrettyTable

question_bank = []
for i in range(len(question_data)):
    new_q = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

x = PrettyTable()
x.add_column('Score', [f'Your ending score was: {quiz.score}/{len(question_bank)}'])
print(x)    
    
                 
                 
                 
                 
                