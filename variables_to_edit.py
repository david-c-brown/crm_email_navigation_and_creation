from datetime import date, timedelta

recipient = 'patient' 
# recipient = 'active'

today = date.today()
date_str = today.strftime("%m-%d")
recipient_list = f"{date_str}_{recipient}"

# sending to only patients that are not currently seeing us
three_months_calc = today - timedelta(90)
three_months = three_months_calc.strftime("%b %d, %Y")

email_campaign_name = f'{date_str} {recipient.title()}' 

company = ''

closed_clinics = ['', '']


## FORMATTING EMAIL BODY
# new line <br>
# emoji: \U00002705
# bold <b>text</b>
# link <a href='https://example.com'>text</a>"

subject = 'Something snappy that I NEED to open'

email_body = """
Hello World,

<br><br> 
This program runs smoothly and avoids the common pitfalls of selenium usage.
<br><br>

<br><br>
\U00002705 <b>Bullet 1:</b> 
<a href=''>Check it out by clicking here!</a>

<br><br>Goodbye Cruel World,
<br> david-c-brown
"""