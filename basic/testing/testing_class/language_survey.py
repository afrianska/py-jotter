from survey import AnonymousSurvey

question = "What language did you first learn to speak? "
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break

    language_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")

no_responses = language_survey.isResponsesEmpty()
if no_responses:
    print("No Responses")
else:
    language_survey.show_results()
