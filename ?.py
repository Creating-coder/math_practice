import math
import random
import time

# HW2: add a random other TYPE of question: e.g. find square root of x, where x=y^2 for y between 10 and 40
# HW3: exercise 100 questions
# HW4 score at least 80.
if __name__ == "__main__":
    score = 0
    questions = 0
    total_t = 0
    total_rel = 0
    while True:
        x = random.randint(100,999)
        y = random.randint(10000,99999)
        z = x*y
        time_t = 0
        rel = 0
        a = 0.85 * z
        b = z * 1.15
        forever = True
        estimation = 0
        t = time.time()
        while forever:
            print(f'Estimate the product of {x} and {y}')
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
            rel = math.fabs(100 - 100 * estimation / z)
            total_rel += rel
            forever = False
        if estimation >= a and estimation <= b:
            print(f'Good estimation! It took you {time_t} seconds. You answered between {int(a)} and {int(b)}! Your relative error is {int(rel)}%.')
            score += 1
        else:
            print(f'Not even close! It took you {time_t} seconds. You were supposed to answer between {int(a)} and {int(b)}! Your relative error is {int(rel)}%.')
        print(f'You have been through {questions} questions')