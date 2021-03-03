import smtplib 
import progress.bar

#Keep Your Emails in this text file
inputfile = open("emails.txt")
mail_ids = inputfile.read().split("\n") 


pbar = progress.bar.Bar("Mail Sent : ",max=len(mail_ids))

# Change this values

EMAIL_ID = '' # Enter your gmail address (abc@gmail.com)
EMAIL_PASS = '' # Enter your gmail password (abc123)
message = "Hello, This is Testing"


for dest in mail_ids: 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(EMAIL_ID, EMAIL_PASS)
    s.sendmail(EMAIL_ID, dest, message) 
    s.quit()
    pbar.next()
pbar.finish()