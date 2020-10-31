import scrapy
from myproject.items import MyprojectItem
from scrapy.loader import ItemLoader
import itertools

class MySpyder(scrapy.Spider):
    name="spidy1"

    custom_settings = {
        'ITEM_PIPELINES': {
            'myproject.pipelines.MyprojectPipeline': 300
        }
    }

    start_urls=['https://www.moneycontrol.com/financials/zeeentertainmententerprises/balance-sheet/ZEE#ZEE', 'https://www.moneycontrol.com/financials/eichermotors/balance-sheet/EM', 'https://www.moneycontrol.com/financials/larsentoubro/balance-sheet/LT', 'https://www.moneycontrol.com/financials/icicibank/balance-sheet/ICI02#ICI02', 'https://www.moneycontrol.com/financials/adaniportsandspecialeconomiczone/balance-sheet/MPS#MPS', 'https://www.moneycontrol.com/financials/bajajauto/balance-sheet/BA10#BA10', 'https://www.moneycontrol.com/financials/drreddyslaboratories/balance-sheet/DRL', 'https://www.moneycontrol.com/india/financials/hdfcbank/balance-sheet/HDF01', 'https://www.moneycontrol.com/financials/tataconsultancyservices/balance-sheet/TCS#TCS', 'https://www.moneycontrol.com/financials/statebankindia/balance-sheet/SBI', 'https://www.moneycontrol.com/financials/hindustanunilever/balance-sheet/HU#HU', 'https://www.moneycontrol.com/india/financials/cipla/balance-sheet/C', 'https://www.moneycontrol.com/financials/housingdevelopmentfinancecorporation/balance-sheet/HDF#HDF', 'https://www.moneycontrol.com/financials/infosys/balance-sheet/IT', 'https://www.moneycontrol.com/financials/hcltechnologies/balance-sheet/HCL02#HCL02', 'https://www.moneycontrol.com/financials/heromotocorp/balance-sheet/HHM#HHM', 'https://www.moneycontrol.com/financials/hindalcoindustries/balance-sheet/HI#HI', 'https://www.moneycontrol.com/financials/bajajfinserv/balance-sheet/BF04#BF04', 'https://www.moneycontrol.com/financials/bajajfinance/balance-sheet/BAF#BAF', 'https://www.moneycontrol.com/india/financials/nestleindia/balance-sheet/NI', 'https://www.moneycontrol.com/financials/upl/balance-sheet/UP04#UP04', 'https://www.moneycontrol.com/financials/asianpaints/balance-sheet/AP31#AP31', 'https://www.moneycontrol.com/financials/tatamotors/balance-sheet/TM03#TM03', 'https://www.moneycontrol.com/financials/kotakmahindrabank/balance-sheet/KMB#KMB', 'https://www.moneycontrol.com/india/financials/techmahindra/balance-sheet/TM4', 'https://www.moneycontrol.com/india/financials/wipro/balance-sheet/W', 'https://www.moneycontrol.com/financials/sunpharmaceuticalindustries/balance-sheet/SPI#SPI', 'https://www.moneycontrol.com/india/financials/relianceindustries/balance-sheet/RI', 'https://www.moneycontrol.com/financials/ultratechcement/balance-sheet/UTC01#UTC01', 'https://www.moneycontrol.com/india/financials/powergridcorporationofindia/balance-sheet/PGC', 'https://www.moneycontrol.com/financials/jswsteel/balance-sheet/JSW01#JSW01', 'https://www.moneycontrol.com/financials/marutisuzukiindia/balance-sheet/MS24#MS24', 'https://www.moneycontrol.com/india/financials/bhartiinfratel/balance-sheet/BI14', 'https://www.moneycontrol.com/india/financials/vedanta/balance-sheet/SG', 'https://www.moneycontrol.com/india/financials/britanniaindustries/balance-sheet/BI', 'https://www.moneycontrol.com/india/financials/grasimindustries/balance-sheet/GI01', 'https://www.moneycontrol.com/india/financials/titancompany/balance-sheet/TI01', 'https://www.moneycontrol.com/india/financials/indianoilcorporation/balance-sheet/IOC', 'https://www.moneycontrol.com/financials/yesbank/balance-sheet/YB#YB', 'https://www.moneycontrol.com/india/financials/ntpc/balance-sheet/NTP', 'https://www.moneycontrol.com/financials/axisbank/balance-sheet/AB16#AB16', 'https://www.moneycontrol.com/financials/mahindraandmahindra/balance-sheet/MM#MM', 'https://www.moneycontrol.com/financials/itc/balance-sheet/ITC#ITC', 'https://www.moneycontrol.com/india/financials/indusindbank/balance-sheet/IIB', 'https://www.moneycontrol.com/india/financials/oilandnaturalgascorporation/balance-sheet/ONG', 'https://www.moneycontrol.com/india/financials/tatasteel/balance-sheet/TIS', 'https://www.moneycontrol.com/financials/coalindia/balance-sheet/CI11#CI11', 'https://www.moneycontrol.com/india/financials/gailindia/balance-sheet/GAI', 'https://www.moneycontrol.com/india/financials/bharatpetroleumcorporation/balance-sheet/BPC', 'https://www.moneycontrol.com/financials/bhartiairtel/balance-sheet/BA08#BA08', 'https://www.moneycontrol.com/financials/shreecements/balance-sheet/SC12#SC12']
    #start_urls=['https://www.moneycontrol.com/india/financials/indusindbank/balance-sheet/IIB']

    def parse(self,response):
        selector= response.css(".mctable1 tr td::text").getall()
        selector1=list(map(lambda x:x.strip().lower().replace(',',''),selector))
        

        
        lst1=[]
        lst2=[]
        lst3=[]
        lst4=[]
        years=[]

        l=ItemLoader(item=MyprojectItem(),selector=response)

        ind=0
        for line in selector1:
            if line == 'total share capital':
                for i in range(1,6):
                    lst1.append(float(selector1[ind+i]))
            elif line == 'networth':
                for i in range(1,6):
                    lst2.append(float(selector1[ind+i]))
            elif line == 'net worth':
                for i in range(1,6):
                    lst2.append(float(selector1[ind+i]))
            elif line == 'reserves':
                for i in range(1,6):
                    lst3.append(float(selector1[ind+i]))
            elif line == 'total debt':
                for i in range(1,6):
                    lst4.append(float(selector1[ind+i]))
            ind+=1

        for i in range(1,6):
            data=response.css("tr.lightbg td::text")[i].get()
            years.append(data)

        if len(lst4)==0:
            lst4.extend(itertools.repeat(0.0,5))

        
        l.add_value('cmp_name',response.css(".pcstname::text").get())
        l.add_value('tsc',lst1[::-1])
        l.add_value('net',lst2[::-1])
        l.add_value('res',lst3[::-1])
        l.add_value('debt',lst4[::-1])
        l.add_value('years',years[::-1])
        yield l.load_item()
            

