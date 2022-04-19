from os import name
import numpy as np
from flask import Flask, request, jsonify, render_template
import urllib.request
from math import cos, expm1
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import csv
import sys

app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template('Efficiency_Calculator.html')

@app.route('/post', methods=['POST'])

def post():
    questionWeight, maxAnswerScore = 4, 4
    maxASMultipleChoice = 10
    answerScore, answerScore2,answerScore3, answerScore4, answerScore5, answerScore6, answerScore7, answerScore8, answerScore9, answerScore10, answerScore11, answerScore12, answerScore13, answerScore14, answerScore15, answerScore16,answerScore17, answerScore18  = ([] for _ in range(18))
    sectionWeight1 = 12
    sectionWeight2 = 16
    sectionWeight3 = 12
    sectionWeight4 = 8
    sectionWeight5 = 8
    sectionWeight6 = 16
    questionScore, questionScore2, questionScore3, questionScore4, questionScore5, questionScore6, questionScore7, questionScore8, questionScore9, questionScore10, questionScore11, questionScore12, questionScore13, questionScore14, questionScore15, questionScore16, questionScore17, questionScore18 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    if request.method == "POST":
        participationOfTrainee = request.form.get('q49_waysTo49')

        if participationOfTrainee == 'Daily Attendance':
            answerScore.append(1)
        
        elif participationOfTrainee == 'Daily attendance plus asking questions to students to check their attentiveness and then mark attendance':
            answerScore.append(2)
        
        elif participationOfTrainee == 'Using platform like Kahoot to take pools, quizzes to check attentiveness and then mark attendance':
            answerScore.append(3)

        elif participationOfTrainee == 'Using digital tool which helps to check daily attendance, integration with platforms like Kahoot and provide dashboard to analyze.':
            answerScore.append(4)

        questionScore = sum(answerScore)/ maxAnswerScore
        weightedQuestionScore = questionScore * questionWeight

        stakeholderCommunication  = request.form.get('q50_whatWays')

        if stakeholderCommunication == 'Verbal communication such as one-to-one meetings, group discussions, classes etc.':
            answerScore2.append(1)
        
        elif stakeholderCommunication == 'Email communication':
            answerScore2.append(2)
        
        elif stakeholderCommunication == 'Email communication and meetings':
            answerScore2.append(3)

        elif stakeholderCommunication == 'Through an LMS or LXP platform which helps to communicate seamlessly using emails, meetings, and announcements for important things':
            answerScore2.append(4)

        questionScore2 = sum(answerScore2)/ maxAnswerScore
        weightedQuestionScore2 = questionScore2 * questionWeight


        bigChallenges  = request.form.get('q51_whatAre51')

        if bigChallenges == 'Using multiple platform for different tasks such as (notify students about content, tests, and analyze quiz response etc.)':
            answerScore3.append(1)
        
        elif bigChallenges == 'Managing course delivery seamlessly.':
            answerScore3.append(2)
        
        elif bigChallenges == 'Assessment of quizzes, tests':
            answerScore3.append(3)

        elif bigChallenges == 'Dealing with feedback and analyzing it':
            answerScore3.append(4)

        questionScore3 = sum(answerScore3)/ maxAnswerScore
        weightedQuestionScore3 = questionScore3 * questionWeight


        sectionScore = sectionWeight1 * (weightedQuestionScore + weightedQuestionScore2 + weightedQuestionScore3)

        #Section 2 

        feedbackTools = request.form.get('q46_whatAre46')

        if feedbackTools == 'Daily feedback using pools and surveys':
            answerScore4.append(1)
        
        elif feedbackTools == 'Only Post Training Survey':
            answerScore4.append(2)
        
        elif feedbackTools == 'Pre- and Post-Training Survey':
            answerScore4.append(3)

        elif feedbackTools == 'Pre- and Post-Training and In the middle of the course':
            answerScore4.append(4)

        questionScore4 = sum(answerScore4)/ maxAnswerScore
        weightedQuestionScore4 = questionScore4 * questionWeight

        realTimeAnalysis  = request.form.get('q19_whatDo')

        if realTimeAnalysis == 'Analyze it yourself by going through each and every feedback':
            answerScore5.append(1)
        
        elif realTimeAnalysis == 'Your team analyze by going through each feedback and use digital tools such as Microsoft Excel':
            answerScore5.append(2)
        
        elif realTimeAnalysis == 'BI Tools such as Power BI, Tableau etc.':
            answerScore5.append(3)

        elif realTimeAnalysis == 'LMS or LXP tools which maintains the feedback data, analyze it for you and provide inferences.':
            answerScore5.append(4)

        questionScore5 = sum(answerScore5)/ maxAnswerScore
        weightedQuestionScore5 = questionScore5 * questionWeight


        surveyCreation  = request.form.get('q20_howDo')

        if surveyCreation == 'Writing down on a paper':
            answerScore6.append(1)
        
        elif surveyCreation == 'Training managing team creating a survey on paper':
            answerScore6.append(2)
        
        elif surveyCreation == 'Feedback form creation tool':
            answerScore6.append(3)

        elif surveyCreation == 'Feedback form creation tool which provides in built and scientific templates for form creation':
            answerScore6.append(4)

        questionScore6 = sum(answerScore6)/ maxAnswerScore
        weightedQuestionScore6 = questionScore6 * questionWeight

        takeFeedback  = request.form.get('q22_name22[]')

        if takeFeedback == 'Monitoring and Analyzing the work and behavior of the employees':
            answerScore7.append(1)
        
        elif takeFeedback == 'One to one feedback':
            answerScore7.append(2)
        
        elif takeFeedback == 'Google forms, Survey Monkey etc.':
            answerScore7.append(3)

        elif takeFeedback == 'Integrated feedback tool in the platform you use which provide in built templates and provides analysis':
            answerScore7.append(4)

        questionScore7 = sum(answerScore7)/ maxASMultipleChoice
        weightedQuestionScore7 = questionScore7 * questionWeight


        sectionScore2 = sectionWeight2 * (weightedQuestionScore4 + weightedQuestionScore5 + weightedQuestionScore6 + weightedQuestionScore7)

        #Section 3 
        # New Way of doing and Evaluating Training

        differentWaysEvaluatingTraining = request.form.get('q25_name25[]')

        if differentWaysEvaluatingTraining == 'Analyze the performance of the employee manually without setting any parameters':
            answerScore8.append(1)
        
        elif differentWaysEvaluatingTraining == 'ROI calculator':
            answerScore8.append(2)
        
        elif differentWaysEvaluatingTraining == 'ROI calculator and through feedback received from the employees':
            answerScore8.append(3)

        elif differentWaysEvaluatingTraining == 'Using training evaluation platform or an efficiency calculator':
            answerScore8.append(4)

        questionScore8 = sum(answerScore8)/ maxASMultipleChoice
        weightedQuestionScore8 = questionScore8 * questionWeight

        toolsEaseTraining  = request.form.get('q26_toolsProvided')

        if toolsEaseTraining == 'Separate profile':
            answerScore9.append(1)
        
        elif toolsEaseTraining == 'Content Accessibility':
            answerScore9.append(2)
        
        elif toolsEaseTraining == 'Recording of sessions':
            answerScore9.append(3)

        elif toolsEaseTraining == 'All of the above':
            answerScore9.append(4)

        questionScore9 = sum(answerScore9)/ maxAnswerScore
        weightedQuestionScore9 = questionScore9 * questionWeight


        toolsProvidedTrainers  = request.form.get('q47_whatAre47')

        if toolsProvidedTrainers == 'Cloud Presentations':
            answerScore10.append(1)
        
        elif toolsProvidedTrainers == 'Engagement tools such as polling tools, google classroom, slack etc.':
            answerScore10.append(2)
        
        elif toolsProvidedTrainers == 'Interactive Dashboards':
            answerScore10.append(3)

        elif toolsProvidedTrainers == 'All of the above':
            answerScore10.append(4)

        questionScore10 = sum(answerScore10)/ maxAnswerScore
        weightedQuestionScore10 = questionScore10 * questionWeight


        sectionScore3 = sectionWeight3 * (weightedQuestionScore8 + weightedQuestionScore9 + weightedQuestionScore10)

        # Section 4

        # Real-time Communication and Collaboration Systems

        meaniningfulCommunication  = request.form.get('q31_name31[]')

        if meaniningfulCommunication == 'Classroom debates':
            answerScore11.append(1)
        
        elif meaniningfulCommunication == 'Discussions offline or online':
            answerScore11.append(2)
        
        elif meaniningfulCommunication == 'Presentation with Q&amp;A':
            answerScore11.append(3)

        elif meaniningfulCommunication == 'A platform where you can have discussion forums, graded discussions as well as video conferencing tools for presentation and Q&amp;A':
            answerScore11.append(4)

        questionScore11 = sum(answerScore11)/ maxASMultipleChoice
        weightedQuestionScore11 = questionScore11 * questionWeight


        collaborativeTraining  = request.form.get('q32_name32[]')

        if collaborativeTraining == 'Offline classroom discussion':
            answerScore12.append(1)
        
        if collaborativeTraining == 'Discussion Forums':
            answerScore12.append(2)
        
        if collaborativeTraining == 'Tools such as slack, Miro':
            answerScore12.append(3)

        if collaborativeTraining == 'A all-in-one platform where you can create discussion forums, use tools like Miro, Google Workspace etc.':
            answerScore12.append(4)

        questionScore12 = sum(answerScore12)/ maxASMultipleChoice
        weightedQuestionScore12 = questionScore12 * questionWeight


        sectionScore4 = sectionWeight4 * (weightedQuestionScore11 + weightedQuestionScore12)


        # Section 5

        # Build Relationship and Growth

        buildCommunity  = request.form.get('q48_doYou48')

        if buildCommunity == 'Yes':
            answerScore13.append(4)
        
        elif buildCommunity == 'No':
            answerScore13.append(0)
        

        questionScore13 = sum(answerScore13)/ maxAnswerScore
        weightedQuestionScore13 = questionScore13 * questionWeight


        marketingPromotion  = request.form.get('q36_whatAre36[]')

        if marketingPromotion == 'Word of mouth':
            answerScore14.append(1)
        
        elif marketingPromotion == 'Webinars':
            answerScore14.append(2)
        
        elif marketingPromotion == 'Emails':
            answerScore14.append(3)

        elif marketingPromotion == 'Marketing campaigns on social media platforms':
            answerScore14.append(4)

        questionScore14 = sum(answerScore14)/ maxASMultipleChoice
        weightedQuestionScore14 = questionScore14 * questionWeight


        sectionScore5 = sectionWeight5 * (weightedQuestionScore13 + weightedQuestionScore14)

        #Section 6

        # Transparency and Access of Content

        provideDetails  = request.form.get('q39_doYou')

        if provideDetails == 'Yes':
            answerScore15.append(4)
        
        elif provideDetails == 'No':
            answerScore15.append(0)
        

        questionScore15 = sum(answerScore15)/ maxAnswerScore
        weightedQuestionScore15 = questionScore15 * questionWeight


        provideRubrics  = request.form.get('q40_doYou40')

        if provideRubrics == 'Yes':
            answerScore16.append(4)
        
        elif provideRubrics == 'No':
            answerScore16.append(0)

        questionScore16 = sum(answerScore16)/ maxAnswerScore
        weightedQuestionScore16 = questionScore16 * questionWeight

        informationToTrainers  = request.form.get('q43_name43[]')

        if informationToTrainers == 'Information about the trainees':
            answerScore17.append(1)
        
        elif informationToTrainers == 'Access to course materials such as presentations, syllabus':
            answerScore17.append(2)
        
        elif informationToTrainers == 'List of courses which can help the trainers to revise for better delivery of course':
            answerScore17.append(3)

        questionScore17 = sum(answerScore17)/ maxASMultipleChoice
        weightedQuestionScore17 = questionScore17 * questionWeight


        informationToTrainees = request.form.get('q44_name44[]')

        if informationToTrainees == 'Course Pre-requirements':
            answerScore18.append(1)
        
        elif informationToTrainees == 'Course syllabus':
            answerScore18.append(2)
        
        elif informationToTrainees == 'Trainer’s details':
            answerScore18.append(3)

        elif informationToTrainees == 'Learnings from the course':
            answerScore18.append(4)

        questionScore18 = sum(answerScore18)/ maxASMultipleChoice
        weightedQuestionScore18 = questionScore18 * questionWeight


        sectionScore6 = sectionWeight6 * (weightedQuestionScore15 + weightedQuestionScore16 + weightedQuestionScore17 + weightedQuestionScore18)



        totalScore = sectionScore + sectionScore2 + sectionScore3 + sectionScore4 + sectionScore5 + sectionScore6
        maxScore = sectionWeight1 + sectionWeight2 + sectionWeight3 + sectionWeight4 + sectionWeight5 + sectionWeight6
        totalScore10 = totalScore/10
    return render_template("resultReport.html", value = round(totalScore10), section1 = round(sectionScore/5), section2 = round(sectionScore2/5), section3 = round(sectionScore3/5), section4 = round(sectionScore4/5), section5 = round(sectionScore5/5), section6 = round(sectionScore6/5))


if __name__=='__main__':
   app.run(debug=True, port=5001)