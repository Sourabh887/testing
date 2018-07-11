import requests
import json
import calendar
import time
from pages.base_page_object import BasePage
from environment import url,API_URL,email_before_gmail_domain



dict1 = {"first_name2" : "", "api_email" : "","password" :""}
API_ENDPOINT = API_URL + "/user"
user_details = API_URL + "/user/details/bytoken/claim"
headers = {'Content-type': 'application/json'}
API_Login = API_URL + "/login"
API_OrgList = ''
API_OrgList1 = ''
API_OrgList2 = ''
EditEmployeeEmail = ''
EditEmployeeEmail1=''
AdminEmail = ''
OrgAdminEmail = ''
OrgAdminEmail1 = ''
EmployeeEmail = ''
BenemaxAdminEmail = ''
AdminFname = ''
AdminFname1 = ''
org5 = ''
org6 = ''
org7 = ''
BenemaxAdminEmail1 = ''
BenemaxAdminEmail2 = ''
AdminFname2 = ''
BenemaxAdminEmail3 = ''
AdminFname3 = ''
benemaxadmin_email = ''

class Create_user(BasePage):
 orgs = None
 @classmethod
 def setOrgs(cls):
        if not(cls.orgs):
            cls.orgs = {
                'org1': str(calendar.timegm(time.gmtime())) + "Capgemini",
                'org2': str(calendar.timegm(time.gmtime())) + "Capgemini1",
                'org3': str(calendar.timegm(time.gmtime())) + "Capgemini2",
                'org4': str(calendar.timegm(time.gmtime())) + "Capgemini3",
                'org5': str(calendar.timegm(time.gmtime())) + "Capgemini4",
                'org6': str(calendar.timegm(time.gmtime())) + "Capgemini5",
                'org7': str(calendar.timegm(time.gmtime())) + "Capgemini6",
                'BenemaxAdminEmail1': email_before_gmail_domain+"+"+"1"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'BenemaxAdminEmail2': email_before_gmail_domain+"+"+"2"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'BenemaxAdminEmail3': email_before_gmail_domain+"+"+"3"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'EditEmployeeEmail': email_before_gmail_domain+"+"+"4"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'EditEmployeeEmail1': email_before_gmail_domain+"+"+"5"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'AdminEmail': email_before_gmail_domain+"+"+"6"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'OrgAdminEmail': email_before_gmail_domain+"+"+"7"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'OrgAdminEmail1': email_before_gmail_domain+"+"+"8"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'EmployeeEmail': email_before_gmail_domain+"+"+"9"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'EmployeeEmail1': email_before_gmail_domain+"+"+"10"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'BenemaxAdminEmail': email_before_gmail_domain+"+"+"11"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                "AdminFname": str(calendar.timegm(time.gmtime())) + "Nainsi1",
                "AdminFname1": str(calendar.timegm(time.gmtime())) + "Nainsi2",
                "AdminFname2" : str(calendar.timegm(time.gmtime())) + "Nainsi3",
                "AdminFname3": str(calendar.timegm(time.gmtime())) + "Nainsi4",
                "AdminFname4": str(calendar.timegm(time.gmtime())) + "Nainsi5",
                "AdminFname5": str(calendar.timegm(time.gmtime())) + "Nainsi_enroll",
                'benemaxadmin_email': email_before_gmail_domain+"+"+"33"+str(calendar.timegm(time.gmtime()))+"@gmail.com",
                'benemaxadmin_email1': email_before_gmail_domain + "+" + "34" + str(calendar.timegm(time.gmtime())) + "@gmail.com"


            }

 @classmethod
 def getOrgs(cls):
        if not(cls.orgs):
            cls.setOrgs()
        return cls.orgs


 def __init__(self, context):
     from steps.group_class_division import orgs
     self.API_OrgList = API_URL + "/org?status=1&search=" + orgs['org1']
     self.API_OrgList1 = API_URL + "/org?status=1&search=" + orgs['org3']
     self.API_OrgList2 = API_URL + "/org?status=1&search=" + orgs['org4']
     self.EditEmployeeEmail = orgs['EditEmployeeEmail']
     self.EditEmployeeEmail1 = orgs['EditEmployeeEmail1']
     self.AdminEmail = orgs['AdminEmail']
     self.OrgAdminEmail = orgs['OrgAdminEmail']
     self.OrgAdminEmail1 = orgs['OrgAdminEmail1']
     self.EmployeeEmail = orgs['EmployeeEmail']
     self.EmployeeEmail1 = orgs['EmployeeEmail1']
     self.BenemaxAdminEmail = orgs['BenemaxAdminEmail']
     self.BenemaxAdminEmail1 = orgs['BenemaxAdminEmail1']
     self.AdminFname = orgs['AdminFname']
     self.AdminFname1 = orgs['AdminFname1']
     self.org5 = API_URL + "/org?status=1&search=" + orgs['org5']
     self.org6 = API_URL + "/org?status=1&search=" + orgs['org6']
     self.org7 = orgs['org7']
     self.BenemaxAdminEmail2 = orgs['BenemaxAdminEmail2']
     self.AdminFname2 = orgs['AdminFname2']
     self.BenemaxAdminEmail3 = orgs['BenemaxAdminEmail3']
     self.AdminFname3 = orgs['AdminFname3']
     self.AdminFname4 = orgs['AdminFname4']
     self.benemaxadmin_email = orgs['benemaxadmin_email']
     self.AdminFname5 = orgs['AdminFname5']
     self.benemaxadmin_email1 = orgs['benemaxadmin_email1']

     BasePage.__init__(
            self,
            context.browser
            )


 def create_user_post(context) :
    showtime = calendar.timegm(time.gmtime())
    global first_name2
    global pastebin_url
    first_name2 = str(showtime)+"Nainsi"
    data = {

        "role": "1",
        "email": str(showtime)+"nainsitest@gmail.com",
        "password": "12345678",
        "first_name": first_name2,
        "last_name": "Jain",
        "permission": "1"

    }

    # sending post request and saving response as response object
    r = requests.post(API_ENDPOINT, json=data)

 def create_user_gettoken(context):

     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] =  email_before_gmail_domain+"+"+"12"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": dict1["api_email"],
         "password": dict1["password"],
         "first_name": dict1["first_name2"],
         "last_name": "Jain",
         "permission": "1"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details+"/"+d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" +c1 + "/" + d)

 def create_universal_benemax_admin_owner_permission(self,context):
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": self.benemaxadmin_email,
         "password": dict1["password"],
         "first_name": self.AdminFname4,
         "last_name": "Jain",
         "permission": "1"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_owner_permission(self,context):
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": self.BenemaxAdminEmail,
         "password": dict1["password"],
         "first_name": self.AdminFname,
         "last_name": "Jain",
         "permission": "1"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_owner_permission1(self, context):
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": self.BenemaxAdminEmail1,
         "password": dict1["password"],
         "first_name": self.AdminFname1,
         "last_name": "Jain",
         "permission": "1"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_owner_permission2(self, context):
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": self.BenemaxAdminEmail2,
         "password": dict1["password"],
         "first_name": self.AdminFname2,
         "last_name": "Jain",
         "permission": "1"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_owner_permission3(self, context):
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": self.BenemaxAdminEmail3,
         "password": dict1["password"],
         "first_name": self.AdminFname3,
         "last_name": "Jain",
         "permission": "1"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_owner_permission4(self, context):
    dict1["password"] = "12345678"
    global pastebin_url
    data = {

             "role": "1",
             "email": self.benemaxadmin_email1,
             "password": dict1["password"],
             "first_name": self.AdminFname5,
             "last_name": "Jain",
             "permission": "1"

    }

    # sending post request and saving response as response object
    r = requests.post(API_ENDPOINT, json=data)
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)
    b = json.loads(pastebin_url)
    print(b['data']['token'])
    d = b['data']['token']

    r1 = requests.get(user_details + "/" + d, json=data)
    pastebin_url1 = r1.text
    b1 = json.loads(pastebin_url1)
    c1 = b1['data']['token']
    context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_editpermission_gettoken(context):
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"13"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": dict1["api_email"],
         "password": dict1["password"],
         "first_name": dict1["first_name2"],
         "last_name": "Jain",
         "permission": "2"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)

 def create_benemax_admin_editpermission_gettoken1(self,context):
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"14"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     global pastebin_url
     data = {

         "role": "1",
         "email": self.AdminEmail,
         "password": dict1["password"],
         "first_name": dict1["first_name2"],
         "last_name": "Jain",
         "permission": "2"

     }

     # sending post request and saving response as response object
     r = requests.post(API_ENDPOINT, json=data)
     pastebin_url = r.text
     print("The pastebin URL is:%s" % pastebin_url)
     b = json.loads(pastebin_url)
     print(b['data']['token'])
     d = b['data']['token']

     r1 = requests.get(user_details + "/" + d, json=data)
     pastebin_url1 = r1.text
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['token']
     context.browser.get(url + "/invitation/" + c1 + "/" + d)
 def login_with_created_user_get_token(context) :
    global pastebin_url
    data = {

        "email": dict1["api_email"],
        "password": dict1["password"]

    }

    # sending post request and saving response as response object
    r = requests.post(API_Login, json=data)
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)
    b = json.loads(pastebin_url)
    print(b['data']['token'])

    c = "/" + b['data']['token']
    context.browser.get(url + "/resetPassword" + c)


 def create_org_admin_with_edit_permission(self,context):
     global pastebin_url
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"15"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     data2 = {

         "email": self.benemaxadmin_email,
         "password": "12345678"

     }

     # sending post request and saving response as response object
     r4 = requests.post(API_Login, json=data2)
     pastebin_url4 = r4.text
     print("The pastebin URL is:%s" % pastebin_url4)
     b4 = json.loads(pastebin_url4)
     print(b4['data']['token'])
     c = b4['data']['token']
     headers1 = {
         "Content-Type":"application/json", "Authorization":"Token "+c,"role-type":"1"
     }
     print("ganu",self.API_OrgList)
     r1 = requests.get(self.API_OrgList,headers=headers1)
     pastebin_url1 = r1.text
     print("The pastebin URL is:%s" % pastebin_url1)
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['result'][0]['id']
     print(c1)

     data1 = {

         "role": "6",
         "email": dict1["api_email"],
         "password": dict1["password"],
         "first_name": "Nainsi4",
         "last_name": "Jain4",
         "permission": "2",
         "org": c1

     }

     # sending post request and saving response as response object
     r2 = requests.post(API_ENDPOINT, json=data1)
     pastebin_url2 = r2.text
     print("The pastebin URL is:%s" % pastebin_url2)
     b2 = json.loads(pastebin_url2)
     print(b2['data']['token'])
     d1 = b2['data']['token']

     r3 = requests.get(user_details + "/" + d1)
     pastebin_url13 = r3.text
     b3 = json.loads(pastebin_url13)
     c3 = b3['data']['token']
     context.browser.get(url + "/invitation/" + c3 + "/" + d1)

 def create_org_admin_with_edit_permission1(self,context):
     global pastebin_url
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"16"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     data2 = {

         "email": self.benemaxadmin_email,
         "password": "12345678"

     }

     # sending post request and saving response as response object
     r4 = requests.post(API_Login, json=data2)
     pastebin_url4 = r4.text
     print("The pastebin URL is:%s" % pastebin_url4)
     b4 = json.loads(pastebin_url4)
     print(b4['data']['token'])
     c = b4['data']['token']
     headers1 = {
         "Content-Type":"application/json", "Authorization":"Token "+c,"role-type":"1"
     }
     print("ganu",self.API_OrgList)
     r1 = requests.get(self.API_OrgList1,headers=headers1)
     pastebin_url1 = r1.text
     print("The pastebin URL is:%s" % pastebin_url1)
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['result'][0]['id']
     print(c1)

     data1 = {

         "role": "6",
         "email": self.EditEmployeeEmail,
         "password": dict1["password"],
         "first_name": "Nainsi4",
         "last_name": "Jain4",
         "permission": "2",
         "org": c1

     }

     # sending post request and saving response as response object
     r2 = requests.post(API_ENDPOINT, json=data1)
     pastebin_url2 = r2.text
     print("The pastebin URL is:%s" % pastebin_url2)
     b2 = json.loads(pastebin_url2)
     print(b2['data']['token'])
     d1 = b2['data']['token']

     r3 = requests.get(user_details + "/" + d1)
     pastebin_url13 = r3.text
     b3 = json.loads(pastebin_url13)
     c3 = b3['data']['token']
     context.browser.get(url + "/invitation/" + c3 + "/" + d1)

 def create_org_admin_with_edit_permission2(self, context):
     global pastebin_url
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"17"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     data2 = {

         "email": self.benemaxadmin_email,
         "password": "12345678"

     }

     # sending post request and saving response as response object
     r4 = requests.post(API_Login, json=data2)
     pastebin_url4 = r4.text
     print("The pastebin URL is:%s" % pastebin_url4)
     b4 = json.loads(pastebin_url4)
     print(b4['data']['token'])
     c = b4['data']['token']
     headers1 = {
         "Content-Type": "application/json", "Authorization": "Token " + c, "role-type": "1"
     }
     print("ganu", self.API_OrgList)
     r1 = requests.get(self.org5, headers=headers1)
     pastebin_url1 = r1.text
     print("The pastebin URL is:%s" % pastebin_url1)
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['result'][0]['id']
     print(c1)

     data1 = {

         "role": "6",
         "email": self.OrgAdminEmail,
         "password": dict1["password"],
         "first_name": "Nainsi4",
         "last_name": "Jain4",
         "permission": "2",
         "org": c1

     }

     # sending post request and saving response as response object
     r2 = requests.post(API_ENDPOINT, json=data1)
     pastebin_url2 = r2.text
     print("The pastebin URL is:%s" % pastebin_url2)
     b2 = json.loads(pastebin_url2)
     print(b2['data']['token'])
     d1 = b2['data']['token']

     r3 = requests.get(user_details + "/" + d1)
     pastebin_url13 = r3.text
     b3 = json.loads(pastebin_url13)
     c3 = b3['data']['token']
     context.browser.get(url + "/invitation/" + c3 + "/" + d1)

 def create_employee(self,context):
     global pastebin_url
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"18"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     data2 = {

         "email": self.benemaxadmin_email,
         "password": "12345678"

     }

     # sending post request and saving response as response object
     r4 = requests.post(API_Login, json=data2)
     pastebin_url4 = r4.text
     print("The pastebin URL is:%s" % pastebin_url4)
     b4 = json.loads(pastebin_url4)
     print(b4['data']['token'])
     c = b4['data']['token']
     headers1 = {
         "Content-Type":"application/json", "Authorization":"Token "+c,"role-type":"1"
     }
     print("ganu",self.API_OrgList)
     r1 = requests.get(self.API_OrgList1,headers=headers1)
     pastebin_url1 = r1.text
     print("The pastebin URL is:%s" % pastebin_url1)
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['result'][0]['id']
     print(c1)

     a1 = requests.get(API_URL + "/group/" + str(c1), headers=headers1)
     a2 = a1.text
     print("Group response is:%s" % a2)
     a3 = json.loads(a2)
     a4 = a3['data']['result'][0]['id']
     print(a4)

     e1 = requests.get(API_URL + "/divison/" + str(c1), headers=headers1)
     e2 = e1.text
     print("Division response is:%s" % e2)
     e3 = json.loads(e2)
     e4 = e3['data']['result'][0]['id']
     print(e4)

     f1 = requests.get(API_URL + "/class/" + str(c1), headers=headers1)
     f2 = f1.text
     print("Class response is:%s" % f2)
     f3 = json.loads(f2)
     f4 = f3['data']['result'][0]['id']
     print(f4)

     data1 = {

     "role":"7",
     "email":dict1["api_email"],
     "password":"12345678",
     "first_name":"Nainsi2",
     "last_name":"Jain2",
     "permission":"3",
     "ssn":str(calendar.timegm(time.gmtime())),
     "group": a4,
     "class":f4,
     "divison":e4,
     "hiring_date": "2017-12-01T07:01:46Z",
     "org":c1

}

     # sending post request and saving response as response object
     r2 = requests.post(API_ENDPOINT, json=data1)
     pastebin_url2 = r2.text
     print("The pastebin URL is:%s" % pastebin_url2)
     b2 = json.loads(pastebin_url2)
     print("Ganu in json loads ",b2)
     #print(b2['data']['token'])
     d1 = b2['data']['token']

     r3 = requests.get(user_details + "/" + d1)
     pastebin_url13 = r3.text
     b3 = json.loads(pastebin_url13)
     c3 = b3['data']['token']
     context.browser.get(url + "/invitation/" + c3 + "/" + d1)

 def create_employee1(self, context):
     global pastebin_url
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"19"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     data2 = {

         "email": self.benemaxadmin_email,
         "password": "12345678"

     }

     # sending post request and saving response as response object
     r4 = requests.post(API_Login, json=data2)
     pastebin_url4 = r4.text
     print("The pastebin URL is:%s" % pastebin_url4)
     b4 = json.loads(pastebin_url4)
     print(b4['data']['token'])
     c = b4['data']['token']
     headers1 = {
         "Content-Type": "application/json", "Authorization": "Token " + c, "role-type": "1"
     }
     print("ganu", self.API_OrgList)
     r1 = requests.get(self.org6, headers=headers1)
     pastebin_url1 = r1.text
     print("The pastebin URL is:%s" % pastebin_url1)
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['result'][0]['id']
     print(c1)

     a1 = requests.get(API_URL + "/group/" + str(c1), headers=headers1)
     a2 = a1.text
     print("Group response is:%s" % a2)
     a3 = json.loads(a2)
     a4 = a3['data']['result'][0]['id']
     print(a4)

     e1 = requests.get(API_URL + "/divison/" + str(c1), headers=headers1)
     e2 = e1.text
     print("Division response is:%s" % e2)
     e3 = json.loads(e2)
     e4 = e3['data']['result'][0]['id']
     print(e4)

     f1 = requests.get(API_URL + "/class/" + str(c1), headers=headers1)
     f2 = f1.text
     print("Class response is:%s" % f2)
     f3 = json.loads(f2)
     f4 = f3['data']['result'][0]['id']
     print(f4)

     data1 = {

         "role": "7",
         "email": self.EmployeeEmail,
         "password": "12345678",
         "first_name": "Nainsi2",
         "last_name": "Jain2",
         "permission": "3",
         "ssn": str(calendar.timegm(time.gmtime())),
         "group": a4,
         "class": f4,
         "divison": e4,
         "hiring_date": "2017-12-01T07:01:46Z",
         "org": c1

     }

     # sending post request and saving response as response object
     r2 = requests.post(API_ENDPOINT, json=data1)
     pastebin_url2 = r2.text
     print("The pastebin URL is:%s" % pastebin_url2)
     b2 = json.loads(pastebin_url2)
     print(b2['data']['token'])
     d1 = b2['data']['token']

     r3 = requests.get(user_details + "/" + d1)
     pastebin_url13 = r3.text
     b3 = json.loads(pastebin_url13)
     c3 = b3['data']['token']
     context.browser.get(url + "/invitation/" + c3 + "/" + d1)

 def create_orgadmin_and_employee(self, context):
     global pastebin_url
     dict1["first_name2"] = str(calendar.timegm(time.gmtime())) + "Nainsi"
     dict1["api_email"] = email_before_gmail_domain+"+"+"20"+str(calendar.timegm(time.gmtime()))+"@gmail.com"
     dict1["password"] = "12345678"
     data2 = {

         "email": self.benemaxadmin_email,
         "password": "12345678"

     }

     # sending post request and saving response as response object
     r4 = requests.post(API_Login, json=data2)
     pastebin_url4 = r4.text
     print("The pastebin URL is:%s" % pastebin_url4)
     b4 = json.loads(pastebin_url4)
     print(b4['data']['token'])
     c = b4['data']['token']
     headers1 = {
         "Content-Type": "application/json", "Authorization": "Token " + c, "role-type": "1"
     }
     print("ganu", self.API_OrgList)
     r1 = requests.get(self.API_OrgList1, headers=headers1)
     pastebin_url1 = r1.text
     print("The pastebin URL is:%s" % pastebin_url1)
     b1 = json.loads(pastebin_url1)
     c1 = b1['data']['result'][0]['id']
     print(c1)

     a1 = requests.get(API_URL + "/group/" + str(c1), headers=headers1)
     a2 = a1.text
     print("Group response is:%s" %a2)
     a3 = json.loads(a2)
     a4 = a3['data']['result'][0]['id']
     print(a4)

     e1 = requests.get(API_URL + "/divison/" + str(c1), headers=headers1)
     e2 = e1.text
     print("Division response is:%s" % e2)
     e3 = json.loads(e2)
     e4 = e3['data']['result'][0]['id']
     print(e4)

     f1 = requests.get(API_URL + "/class/" + str(c1), headers=headers1)
     f2 = f1.text
     print("Class response is:%s" % f2)
     f3 = json.loads(f2)
     f4 = f3['data']['result'][0]['id']
     print(f4)

     data1 = {
 "first_name": "Nainsi6",
 "email": dict1['api_email'],
 "last_name": "Jain6",
 "middle_name": "a",

 "employment": [{
   "permission": 3,
   "org": c1,
   "role": 7,
   "hiring_date": "2017-12-01T07:01:46Z",
   "group": a4,
   "class":f4 ,
   "division": e4,
   "ssn":str(calendar.timegm(time.gmtime()))

  },
  {
   "permission": 2,
   "org": c1,
   "role": 6


  }
 ]
}

     # sending post request and saving response as response object
     r2 = requests.post(API_ENDPOINT, json=data1)
     pastebin_url2 = r2.text
     print("The pastebin URL is:%s" % pastebin_url2)
     b2 = json.loads(pastebin_url2)
     print(b2['data']['token'])
     d1 = b2['data']['token']

     r3 = requests.get(user_details + "/" + d1)
     pastebin_url13 = r3.text
     b3 = json.loads(pastebin_url13)
     c3 = b3['data']['token']
     context.browser.get(url + "/invitation/" + c3 + "/" + d1)

