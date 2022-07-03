# CTI-110
# P4HW1 - Score List
# Silas Stary 
# 07/3/2022
# Making a score list

#first ask the user to input how many scores
num_scores = int(input('How many scores do you want to enter?'))
#next assign the variables that make the loop function
x = 0
y = x + 1
user_scores = []
#the loop bellow allows user to input scores and provides an error if an invalid score is inputted
while x < num_scores:
    score_y = int(input('Enter score #' + str(y) +':'))
    if 0 <= score_y <= 100:
        x = x + 1
        y = x + 1
        user_scores.append(score_y)
    else:
         print('INVALID Score entered!!!!')
         print('Score should be between 0 and 100')
         int(input('Enter score #' + str(y) +' again:'))
         x = x + 1
         y = x + 1
         user_scores.append(score_y)
#assigns variables to grading scale
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50
#bellow displays the results of the list made 
print('---------------Results---------')
print('Lowest score  :',min(user_scores))
user_scores.remove(min(user_scores))
print('Modified List :', user_scores)
print('Scores Average:', sum(user_scores) / len(user_scores))
avg_score = sum(user_scores) / len(user_scores)
if avg_score >= A_score:
    print('Grade         : A')
else:
    if avg_score >= B_score:
        print('Grade         : B')
    else:
        if avg_score >= C_score:
            print('Grade         : C')
        else:
            if avg_score >= D_score:
                print('Grade         : D')
            else:
                print('Grade         : F')
print('-------------------------------')

        
      
        
