# logic.py
def get_reply(message):
    message = message.lower()
    if message in ['hi','hello','hey']:
        return "Hello! Welcome to the College Helpdesk. How can I assist you today?"
    elif message in ['admission','admission details','how to apply']:
        return "Admissions are currently open. You can apply online through the college website by filling out the admission form."
    elif message in ['courses','courses offered','programs']:
        return "We offer B.Tech, M.Tech, MBA, and MCA programs across various specializations."
    elif message in ['fees','fee structure','college fees']:
        return "The annual fee for undergraduate programs is ₹75,000."
    elif message in ['contact','phone number','helpdesk number']:
        return "You can contact the college helpdesk at +91-9876543210 or email helpdesk@college.edu"
    elif message in ['bye','exit','quit']:
        return "Thank you for contacting the College Helpdesk. Have a great day!"
    else:
        return "I didn't get it. Kindly mail helpdesk@college.edu for more details."


