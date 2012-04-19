>>> import email.Message, smtplib
>>> apology = email.Message()
>>> apology.add_header('To', 'leopold.moz@pythonchallenge.com')
>>> apology.add_header('From', "your email address")
>>> apology.add_header('Subject', 'Apology')
>>> apology.set_payload('Sorry!')
>>> print apology.as_string()
To: leopold.moz@pythonchallenge.com
From: your email address
Subject: Apology

Sorry!

>>> server = smtplib.SMTP('localhost')
>>> server.sendmail(apology['from'], apology['to'], apology.as_string())
{}
>>> server.quit()
He gives you an md5 for the corrupted zip file you found earler on the maze level (mybroken.zip). Eventually the zip does decompress to give a GIF saying "speed". Combine with the "boat" from the page

