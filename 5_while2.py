questions_and_answers = {"Как дела?": "Норм!", 
                        "Что делаешь?": "Код пишу", 
                        "Спать пойдёшь?": "Пойду", 
                        "Работать будешь?": "А есть предложения?"
                        }

def ask_user(answers_dict):
    while True:
        ask = input('Привет. Спрашивай что угодно!  ')
        print(questions_and_answers.get(ask, 'Спроси что то другое'))
        
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
