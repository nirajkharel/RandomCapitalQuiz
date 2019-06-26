# This program gives 50 different random questions for the desired number of students.
# Author of the program = Niraj Kharel
# To start the program first create a folder named "QUIZ" on you current working directory otherwise you will get error.

import random


# The quiz data. Keys are states and values are their capitals.
# Country: Capitals
capitals = {'Nepal': 'Kathmandu', 'Albania': 'Tirana', 'Algeria': 'Algiers',
'Andorra': 'Andorra la Vella', 'Afghanistan': 'Kabul', 'Malaysia': 'Kuala Lumpur',
'Argentina': 'Buenos Aires', 'Australia': 'Canberra', 'Bangladesh': 'Dhaka',
'Mexico': 'Mexico City', 'Monaco': 'Monaco', 'Morocco': 'Rabat', 'Bhutan':
'Thimphu', 'Namibia': 'Windhoek', 'Bolivia': 'Sucre', 'Brazil':
'Brazil', 'Nigeria': 'Abuja', 'North Korea': 'Pyongyang', 'Burundi':
'Gitega', 'Niger': 'Niamey', 'Netherlands': 'Amsterdam', 'New Zealand':
'Wellington', 'Norway': 'Oslo', 'Colombia': 'Bogotá', 'Costa Rica':
'San Jose', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'Philippines': 'Manila', 'Portugal': 'Lisbon', 'Poland': 'Warsaw',
'Croatia': 'Zagreb', 'Denmark': 'Copenhagen',
'Egypt': 'Cairo', 'Estonia': 'Tallinn', 'Ethiopia': 'Addis Ababa',
'Finland': 'Helsinki', 'France': 'Paris', 'South Africa': 'Pretoria',
'Germany': 'Berlin', 'Spain': 'Madrid', 'Sudan':
'Khartoum', 'Indonesia': 'Jakarta', 'Tonga': 'Nukuʻalofa', 'Ireland':
'Dublin', 'Turkey': 'Ankara', 'Italy': 'Rome', 'Japan': 'Tokyo', 
'India': 'New Delhi', 'Zimbabwe': 'Harare'}


# Ask the number of question sheets to be made.
student_number = int(input("Enter the number of students: "))

for question_sheet in range(student_number):
	sheet_details = 0
	# Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)
	# Generate the quiz questions accordint to the key values in the dictionary capitals..
	for quizNum in range(len(capitals)):

		# Create the quiz and answer key files.
		quizFile = open('QUIZ/Question{}.txt'.format(question_sheet+1), 'a')
		answerKeyFile = open('QUIZ/Answer{}.txt'.format(question_sheet+1), 'a')

		if sheet_details == 0: 
			# Write out the header for the quiz.
			quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
			quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (question_sheet + 1))
			quizFile.write('\n\n')
			sheet_details = 1
			
		# Get right and wrong answers.
		correctAnswer = capitals[states[quizNum]]
		wrongAnswers = list(capitals.values())
		# delete the right answer from the list of wrong answer.
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		# Pick up any three random answers from thw wrongAnswers list
		wrongAnswers = random.sample(wrongAnswers, 3)
		# Add the correct answer to those three wrong answers to make 4 options all together
		answerOptions = wrongAnswers + [correctAnswer]
		# Shuffle the list answerOptions so that right answer would not stay on the last index always.
		random.shuffle(answerOptions)


		# Write the question and the answer options to the quiz file.
		quizFile.write('%s. What is the capital of %s?\n' % (quizNum + 1, states[quizNum]))
		for i in range(4):
			quizFile.write('%s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		# Write the answer key to a file.
		answerKeyFile.write('%s. %s\n' % (quizNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
		
quizFile.close()
answerKeyFile.close()