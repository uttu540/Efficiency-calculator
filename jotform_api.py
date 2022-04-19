from jotform import *

def main():

    jotformAPIClient = JotformAPIClient('b6a98a4a6462823440a3f917821c2994')

    forms = jotformAPIClient.get_forms(None, 1, None, None)

    latestForm = forms[0]

    latestFormID = latestForm["id"]

    submissions = jotformAPIClient.get_form_submissions(latestFormID)

    print(submissions)

if __name__ == "__main__":
    main()