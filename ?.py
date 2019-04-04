import math
import random
import time

# HW3: exercise 100 questions
# HW4 score at least 80.
if __name__ == "__main__":
    score = 0
    questions = 0
    total_t = 0
    total_rel = 0
    while True:
        question_decider = random.randint(0,1)
        if question_decider == 1:
            operation_decider = random.randint(0, 1)
            if operation_decider == 1:
                x = random.randint(100000, 999999)
            else:
                x = random.randint(1000000, 9999999)
            z = pow(x, 1 / 2)
        else:
            y = random.randint(10000,99999)
            operation_decider = random.randint(0, 2)
            if operation_decider == 0:
                x = random.randint(100, 999)
                z = x*y
            elif operation_decider == 2:
                x = random.randint(10, 99)
                z = y / x
            else:
                x = random.randint(100, 999)
                z = y/x
        time_t = 0
        rel = 0
        a = 0.95 * z
        b = z * 1.05
        forever = True
        estimation = 0
        t = time.time()
        while forever:
            if question_decider == 1:
                print(f'Estimate the square root of {x}')
            else:
                if operation_decider == 0:
                    print(f'Estimate the product of {x} and {y}')
                else:
                    print(f'Estimate {y} divided by {x}')
            estimation = input()
            time_t = time.time() - t
            if estimation == "exit":
                avg_t = int(total_t/questions)
                avg_rel = int(total_rel/questions)
                print(f'Congratulations! You got a score of {score} out of {questions} or {int(100*score/questions)}%. Your average time was {avg_t}. Your average percent off was {avg_rel}.')
                exit(0)
            try:
                estimation = int(estimation)
            except:
                continue
            questions += 1
            total_t += time_t
            rel = math.fabs(100 - 100 * float(estimation) / float(z))
            total_rel += rel
            forever = False
        if int(a) <= estimation <= int(b):
            print(f'Good estimation! It took you {time_t} seconds. You answered between {int(a)} and {int(b)}! Your relative error is {int(rel)}%.')
            score += 1
        else:
            print(f'Not even close! It took you {time_t} seconds. You were supposed to answer between {int(a)} and {int(b)}! Your relative error is {int(rel)}%.')
        print(f'You have been through {questions} questions')