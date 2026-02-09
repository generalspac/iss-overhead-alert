import smtplib
def send_mail(*args,**kwargs):
    """args are the names of users and kwargs is the dict where we have their mails"""
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    user=os.getenv("USER")
    password=os.getenv("PASSWORD")
    connection.login(user=user,password=password)
    for name in args:
        connection.sendmail(from_addr=user,to_addrs=kwargs[name],msg=f"Subject:iss\n\n hey,{name} look up,iss is in the sky")
    connection.close()