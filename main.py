import requests
from datetime import datetime, timedelta


# age = 20
# pincodes = ["700054"]
# num_days = 3

print_flag = 'Y'

def search(age,pincodes,num_days):
    print("Starting search for Covid vaccine slots!")

    actual = datetime.today()
    list_format = [actual + timedelta(days=i) for i in range(num_days)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

    while True:
        counter = 0   
        details=list()

        for pincode in pincodes:   
            for given_date in actual_dates:

                URL = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={given_date}"
                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
                
                result = requests.get(URL, headers=header)
                
                if result.ok:
                    response_json = result.json()
                    if response_json["centers"]:
                        if(print_flag.lower() =='y'):
                            for center in response_json["centers"]:
                                for session in center["sessions"]:
                                    if (session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                        detail_keys=['pincode','given_date','center_name','block_name','fee_type','availability','Vaccine']
                                        detail = dict.fromkeys(detail_keys,None)
                                        detail['pincode']=pincode
                                        detail['given_date']=given_date
                                        detail["center_name"]=center["name"]
                                        detail['block_name']=center["block_name"]
                                        detail['fee_type']=center["fee_type"]
                                        detail["availability"]=session["available_capacity"]
                                        detail["Vaccine"]=session["vaccine"]
                                        details.append(detail)
                                        counter = counter + 1
                else:
                    print("No Response!")
                    
        # if counter:
        #     print("Search Completed!!\nGo to: https://selfregistration.cowin.gov.in/ to book your slots.\nHappy Vaccination!!")
        # else:
        #     print("No Vaccine slots available.")
        
        return details
# print(search(18,['700019'],3))
