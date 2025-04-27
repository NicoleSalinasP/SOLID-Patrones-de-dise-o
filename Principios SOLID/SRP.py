""" Parte  1 principios SOLID:

    Este còdigo contiene 3 responsabilidade ùnicas y son :
    
"""

class ReportMaker :
    def maker_Report(self, data):
        return f"Generating report with {data}"
    

class SaveToFile:
    def save_file(self, content):
        print (f"Saving report to file: {content}")
    

class SendEmail:
    def senf_email(self , email, content):
        print(f"Sending report to email :{email}")


