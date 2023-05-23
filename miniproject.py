print("***************EMPLOYEE EVALUATION SYSTEM***************")
name=input("\nEnter Employee name: \n")
id=input("Enter Employee ID: \n")
score=[]
communication_score=0
Questions=["\n1.Quality of Work:\nRegularly and accurately completes the work given and posseses proffesionalism & technical proficiency",
          "\n2.Work Habits: \nPlans & organises work; takes care of equipment & supplies",
          "\n3.Relationship with People:\nHas the ability to get along with there others & effectively deals with the public",
          "\n4.Dependability:\nCan be relied upon to work steadily, effectively & puntually",
          "\n5.Quantity of Work:\nAmount of work performed",
          "\n6.Initiative:\nShows initiative , resourcefulness & has a positive response towards work assigned",
          "\n7.Creativity:\nPosseses creativity, versatality, originality & isn't afraid to think out of the box",
          "\n8.Analytical Ability:\nCarries out analysis of data, facts, laws, rules & procedures, thoroughly and accurately",
          "\n9.Ability as a Supervisor:\nProficient in employee training as well as planning, organizing & laying work for work unit",
          "\n10.Administrative Ability:\nPromptness of action, soundness of decision, application of good management principles"]


communication_skills=["Can the employee communicate their ideas clearly?",
                      "Can the employee host meetings and seminars?",
                      "Is the employee proficient in english?"]

print("\n\nRate each of the question below on a scale of 1-5 where:")
print("1 - Unsatisfactory")
print("2 - Fair")
print("3 - Good")
print("4 - Very Good")
print("5 - Excellent")

for question in Questions:
    print(question)
    score.append(int(input()))

sum=sum(score)
percent_score=sum*2

print("\n\nAnswer the below questions as yes or no:")
for question in communication_skills:
    print(question)
    ans=input()
    if(ans=="yes"):
        communication_score=communication_score+1

print("\n\n******************** EMPLOYEE REPORT ********************")
print(f'\n\nEmployee performance score of {name} (ID:{id}): ',percent_score,"%\n")

if(percent_score>=75):
    print("Employee has shown excellent performance throughout the year!!")
elif(percent_score>=50 and percent_score<75):
    print("Employee has shown fairly good performance through the year. There is room for improvement.")
elif(percent_score>=25 and percent_score<50):
    print("Employee has shown average performance throughout the year.Has to start taking the job more seriously.")
else:
    print("Employee performance is exceedingly bad. Please report to your supervisor for a detailed evaluation.")

print()

if(communication_score==3):
    print("Employee posseses excellent communcation skills.")
elif(communication_score==2):
    print("Employee posseses good communication skills.Can be better.")
else:
    print("Employee communication skills require lot of work. Report to HR for further instructions.")

if(score[2]<3):
    print("\nEmployee has to work on their relationship with their collegues.\nPlease refer to this article to improve relationship with your collegues \"https://www.betterup.com/blog/building-good-work-relationships\"")

if(score[5]<3):
    print("\nEmployee shows low initiative at work.\nPlease refer to this article to improve initiative quality \"https://www.indeed.com/career-advice/career-development/ways-to-take-initiative-at-work\"")

if(score[6]<3):
    print("\nEmployee has shown low creativity.\nPlease refer to this article to show more creativity at work\"https://www.sefe-mt.com/careers/blog/how-to-be-creative-at-work-11-tips-for-more-innovative-ideas/\"\n")
print()
