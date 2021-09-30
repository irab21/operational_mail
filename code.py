import streamlit as st
import pandas as pd 
import numpy as np 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,ssl
from tabulate import tabulate

st.title("Operational Mails")
uploaded_file = st.file_uploader("Choose a file")
st.markdown('### Upcoming Joining')

temp_file3 = st.file_uploader("Enter The File here!")
if temp_file3: 
	temp_file_contents3 = temp_file3.read()

if st.button("Save This As a working file"):
    with open("ON_DISK_FILE3.extension","wb") as file_handle3:
        file_handle3.write(temp_file_contents3)

result3= st.button('Send the Mail')
if result3:
	my_email= "datateamposterity@gmail.com"
	password= "posterity@123"

	server = smtplib.SMTP_SSL('smtp.gmail.com' ,465)
	server.ehlo()
	server.login(my_email, password)
	email_list = pd.read_excel("ON_DISK_FILE3.extension") 

	email_list['Mutual Joining Date']=email_list['Mutual Joining Date'].astype(str)
	email_list['Sourcer']=email_list['Sourcer'].astype(str)
	email_list['Sourcer Email']=email_list['Sourcer Email'].astype(str)
	email_list['Name']=email_list['Name'].astype(str)
	email_list['Mutual Joining Date']=email_list['Mutual Joining Date'].astype(str)
	email_list['Client']=email_list['Client'].astype(str)
	email_list['Comment']=email_list['Comment'].astype(str)
	email_list['Last update/revert']=email_list['Last update/revert'].astype(str)




	names=email_list['Sourcer']
	emails=email_list['Sourcer Email']
	ccs=email_list['CC']
	candidates=email_list['Name']
	joining_dates=email_list['Mutual Joining Date']
	clients=email_list['Client']
	comments=email_list['Comment']
	last_reverts=email_list['Last update/revert']


	for i in range(len(emails)):
		name=names[i]
		email=emails[i]
		candidate=candidates[i]
		joining_date=joining_dates[i]
		client=clients[i]
		comment=comments[i]
		cc=ccs[i]
		last_revert=last_reverts[i]


		msg = MIMEMultipart()
		msg["Subject"] = "Upcoming Joining |"+candidate+" | "+joining_date
		msg["From"] = my_email
		msg["To"] = email
		msg["Cc"] = cc

		text="Hello "+name+",\n\nPFB the details of your upcoming joining:"+"\n\n1.Candidate Name: "+candidate+"\n\n2.For Client: "+client+"\n\n3.Date of Joining: "+joining_date+"\n\n4.Comments/ Last revert: "+comment+" "+last_revert

		part1 = MIMEText(text, "plain")
		msg.attach(part1)
		try:
			server.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
			st.write('Email to {} successfully sent!\n\n'.format(email))
		except Exception as e:
			st.write('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))
	server.close()


st.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


st.markdown("### Daily Productivity Mail")
temp_file = st.file_uploader("Enter the file here!")
if temp_file: 
	temp_file_contents = temp_file.read()

if st.button("Save as working file"):
    with open("ON_DISK_FILE.extension","wb") as file_handle:
        file_handle.write(temp_file_contents)

result= st.button('Send Daily Productivity Mail')
if result:

	my_email= "datateamposterity@gmail.com"
	password= "posterity@123"
	server = smtplib.SMTP_SSL('smtp.gmail.com' ,465)
	server.ehlo()
	server.login(my_email, password)
	data= pd.read_excel("ON_DISK_FILE.extension") 
	st.write(data)

	data['Date']= data['Date'].astype(str)
	data['Target']=data['Target'].astype(str)
	data['CV Submitted']=data['CV Submitted'].astype(str)


	recruiters=data['Recruiter']
	dates=data['Date']
	targets=data['Target']
	cv_subs=data['CV Submitted']
	email_ids=data['Email Id']
	ccs=data['CC']

	for i in range(len(data)):
		recruiter=recruiters[i]
		date=dates[i]
		target=targets[i]
		cv_sub=cv_subs[i]
		email_id=email_ids[i]
		cc=ccs[i]

		if target<=cv_sub:
			st.write('target met for {}'.format(recruiter,str()))
		else:

			msg=MIMEMultipart()
			msg["Subject"]=cv_sub+' CVs submitted for '+date+'| Daily Target- '+target
			msg["From"]=my_email
			msg["To"]= email_id
			msg["Cc"]=cc

			text="Hello "+recruiter+"\n\nThis is to inform you that your CV submission for "+date+" was "+cv_sub+", which is lower than your daily target of "+ target+" CVs."+"\n\nIf you have sourced CV, but not uploaded on ATS, it’s strongly requested that you do so every day before EOD the same day, because the data is collated and sent every morning for the previous day."+"\n\nTeam Convener, you’re requested to keep an eye on the engagement of the recruiter so that he/she is not highlighted in any further emails."+"\n\nWe expect better work ethics, self-discipline and unwavering integrity and dedication towards your work, so that working through these difficult times, feel like a collective initiative from both your end and ours."+"\n\nWe’ll monitor the performance daily, and request you to improve your performance so as to not get highlighted again."+"\n\nRegards,\nData Team"

			part2= MIMEText(text,"plain")
			msg.attach(part2)
			try:
				server.sendmail(msg["From"],msg["Cc"].split(",")+msg["To"].split(","),msg.as_string())
				st.write('Email to {} successfully sent!\n\n'.format(email_id))
			except Exception as e:
				st.write('Email to {} could not be sent :( because {}\n\n'.format(email_id,str(e)))

	server.close()

st.write('------------------------------------------------------------------------------------------------------------------------------------------------')


st.markdown('### No Selection Mail- Fortnightly')
temp_file1 = st.file_uploader("Enter the file Here!")
if temp_file1: 
	temp_file_contents1 = temp_file1.read()

if st.button("Save as a working file"):
    with open("ON_DISK_FILE1.extension","wb") as file_handle1:
        file_handle1.write(temp_file_contents1)

result1= st.button('Send No Selection Mail')
if result1:

	my_email= "automatedmail.posterity@gmail.com"
	password= "Chandra2021"



	server = smtplib.SMTP_SSL('smtp.gmail.com' ,465)
	server.ehlo()
	server.login(my_email, password)
	email_list = pd.read_excel("ON_DISK_FILE1.extension") 
	st.write(email_list)

	names=email_list['Name']
	emails=email_list['Email']
	ccs=email_list['CC']


	for i in range(len(emails)):
		name=names[i]
		email=emails[i]
		cc=ccs[i]


		msg=MIMEMultipart()
		msg["Subject"]="0 Selections in the fortnight 01-09-2021 to 15-09-2021"
		msg["From"]=my_email
		msg["To"]= email
		msg["Cc"]=cc

		text="Hello "+name+"\nGreetings!\n\nBased on our records we have noticed that you have not had any Selections in the last two weeks. We feel it's important to highlight this to you.\n\nSeletions might not have happened due to a variety of reasons such as the lack of feedback, Interview No Shows, Quality, Conversion, lesser Client Engagement,Lack of Role Understanding, Lack of Role briefing or training at your level, or Possibly the fact that you deserve more diversified assignments.\n\nWe want you to assess and discuss these factors with close consultation of your Team Convener, Supervisor, and skip-level Supervisor and come with a solution on how can we overcome this as getting selections at regular intervals is critical to achieve your performance metric and eventually adding revenue to the team and the organization.\nWe hope that you will see this gap objectively, and be informed that the whole organization is there to assist you in your endeavor. We want you to stay motivated, and this should not be taken as any kind of stressed or escalation mail.\nHowever we feel very confident that if we all work closely together we can address it.\n\nWe do not believe in looking at performance in isolation, we look at performance as a bigger picture starting from the CV Submissions, Productivity, Conversions, etc. We also understand that you are not the only factor for either failure or success even sometimes including fallacies at the client end.\n\nWe will be happy to hear you back, you can speak to the Team Conveneror or the supervisor supervisor openly or confidentially.\n\nData Team\nPosterity"

		part2= MIMEText(text,"plain")
		msg.attach(part2)
		try:
			server.sendmail(msg["From"],msg["Cc"].split(",")+msg["To"].split(","),msg.as_string())
			st.write('Email to {} successfully sent!\n\n'.format(email))
		except Exception as e:
			st.write('Email to {} could not be sent :( because {}\n\n'.format(email,str(e)))

	server.close()
st.write('------------------------------------------------------------------------------------------------------------------------------------------------')
st.markdown('### Candidate Mail-Monthly')
temp_file2 = st.file_uploader("Enter the File here!")
if temp_file2: 
	temp_file_contents2 = temp_file2.read()

if st.button("Save this as a working file"):
    with open("ON_DISK_FILE2.extension","wb") as file_handle2:
        file_handle2.write(temp_file_contents2)

result2= st.button('Send Mail')
if result2:
	my_email= "automatedmail.posterity@gmail.com"
	password= "Chandra2021"

	server = smtplib.SMTP_SSL('smtp.gmail.com' ,465)
	server.ehlo()
	server.login(my_email, password)
	email_list = pd.read_excel("ON_DISK_FILE2.extension") 
	st.write(email_list)
	email_list["Submission Date"]= email_list["Submission Date"].astype(str)
	email_list["Selection Date"]= email_list["Selection Date"].astype(str)
	email_list["Offer Date"]= email_list["Offer Date"].astype(str)
	email_list["Mutual Joining Date"]= email_list["Mutual Joining Date"].astype(str)

	names = email_list['Name']
	emails= email_list['E-mail id']
	soucer_emails= email_list['sourcer email']
	clients= email_list['Client']
	offer_dates = email_list['Offer Date']

	for i in range(len(emails)):
		name = names[i]
		email = emails[i]
		Cc = soucer_emails[i]
		client= clients[i]
		offer_date= offer_dates[i]

		msg = MIMEMultipart()
		msg["Subject"] = "Team Posterity : Regarding your Joining cum Onboarding with our Client-"+client
		msg["From"] = my_email
		msg["To"] = email
		msg["Cc"] = Cc

		text="Hello "+name+"\nGreetings from Posterity!"+"\nThis is follow-up cum engagement communication mail to know the status of your Joining/onboarding process with our client- " + client +",  we are happy that you have been found suitable by our client and they have proposed an offer to you. The purpose of mail is to have close communication with you and provide assistance & intervene wherever required, this will help to avoid the communication gap."+"\nPlease help with the following information and if you  have finished following steps.\n\n•Have you given a written offer Acceptance to TA/HR team, please share your comment.\n\n•Resignation Initiation (please mention date), if you can forward a resignation email or screenshot to us or the client, please share your comment?\n\n•Resignation Acceptance, please share your comment.\n\n•Last working day given by your current employer, please share your comment.\n\n•Mutual freezing on the specific Date of Joining over email, please share your comment.\n\n•If Applicable: Initiation of Background verification Process and your cooperation in it, please share your comment.\n\n•Welcome Mail or onboarding email with details from the client which come few days before the onboarding date and contains all details regarding joining details, please share your comment.\n\n•If you are contemplating any other opportunity or anticipating any other offer, please let us know or engage us so that we can do a needful intervention.\n\n•If you are being pursued by your current employer to retain you, please let us know or engage us so that we can do a needful intervention.\n\n•Are you able to communicate with the Staffing /HR Team of our client regarding any of your query or doubt."+"\n\nFor any reason if you have decided to let go of this opportunity and you are 100% certain about your decision, you may let us know your decision with absolute transparency and clarity, we will be appreciative of your gesture as this will help us and our client to identify an alternative candidate to fill this vacancy as we are of the view that business of the company should not hamper in absence of clarity."+"\nAlso, we being part of a democratic country, you have the absolute right to decline any opportunity with or without giving any justifications and we will fully respect your decision. You can communicate your decision to say no without feeling any moral or guilt dilemma however your open & transparent communication is key to this."+"\nPlease write us back or to the concerned recruiter who assisted you in this selection process or approach us at ayushi.kanojia@posterity.in in case, any activities are pending or you need any intervention, a timely communication will ensure a smooth joining process.\n\nSoliciting your revert.\nStaffing Operations Team\nPosterity Consulting Pvt Ltd"
		part1 = MIMEText(text, "plain")
		msg.attach(part1)
		try:
			server.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
			st.write('Email to {} successfully sent!\n\n'.format(email))
		except Exception as e:
			st.write('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))
	server.close()


st.write('------------------------------------------------------------------------------------------------------------------------------------------------')
st.markdown('### Pending Offers')
temp_file4 = st.file_uploader("Enter The File Here!")
if temp_file4: 
	temp_file_contents4 = temp_file4.read()

if st.button("Save this As A working file"):
    with open("ON_DISK_FILE4.extension","wb") as file_handle4:
        file_handle4.write(temp_file_contents4)

result4= st.button('Send Pending Offers Mail')
if result4:
	my_email= "automatedmail.posterity@gmail.com"
	password= "Chandra2021"

	server = smtplib.SMTP_SSL('smtp.gmail.com' ,465)
	server.ehlo()
	server.login(my_email, password)
	email_list = pd.read_excel("ON_DISK_FILE4.extension") 
	#st.write(email_list)
	email_list['Offer Aging']=email_list['Offer Aging'].astype(str)
	#email_list['Resignation Aging']=email_list['Resignation Aging'].astype(str)
	#email_list['Resignation Accepted']=email_list['Resignation Accepted'].astype(str)


	names = email_list['Name']
	sourcers=email_list['Sourcer']
	emails= email_list['Sourcer Mail']
	ccs=email_list['CC']
	clients= email_list['Client']
	offer_ages=email_list['Offer Aging']
	crs=email_list['Client Recruiter']
	spocs=email_list['SPOC']

	for i in range(len(emails)):
		name=names[i]
		sourcer=sourcers[i]
		email=emails[i]
		Cc=ccs[i]
		client=clients[i]
		offer_age=offer_ages[i]
		cr=crs[i]
		spoc=spocs[i]

		msg = MIMEMultipart()
		msg["Subject"] = "Your Candidate Offer Update | "+name+" | "+offer_age+" days pending"
		msg["From"] = my_email
		msg["To"] = email
		msg["Cc"] = Cc

		text="Hello "+ sourcer+" Your candidate "+name+" has not been offered by "+client+" for "+offer_age+" days."+"\n\nKindly connect with "+cr+" and "+spoc+" for the update."+"\n\nDo needful proactive communication at client and candidate end to bridge expectations and communication gaps."+"\n\nKindly keep the invoice team, SPOC, Team Convener, and other stakeholders in copy when sending the update."+"This is an automated mail, Please DO NOT REPLY to this mail."+"\n\nRegards,\nData Team"
		part1 = MIMEText(text, "plain")
		msg.attach(part1)
		try:
			server.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
			st.write('Email to {} successfully sent!\n\n'.format(email))
		except Exception as e:
			st.write('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))
	server.close()
