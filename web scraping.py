import requests
from bs4 import BeatifulSoup
import pandas
import argaparse
import connect



parser = argaparse.ArgumentParser()
parser.add_argument("--page_num_max", help='Enter the number of pages to parse', type=int)
parser.add_argument("--dbname", help,"Enter the name of db", type=str)
args= parser.parse_args()



oyo_url="https://www.oyorooms.com/hotels-in-banglore/?page="
page_num_max=args.page_num_max
scrapped_info_list=[]
connect.connect(args.dbname)



for page_num in range(1,page_num_max):
  url=oyo_url+str(page_num)
print("GET Request for: " + url)
req= requests.get(url)
content=req.content



soup=BeatifulSoup(content,"html.parser")



all_hotels=soup.find_all("div",{"class": "hotelCardListing"})



for hotel in al_hotels:
   hotel_dict={}
hotel_dict["name"]=hotel.find("h3",{"class": "ListingHotelDescription_hotelName"}).text
hotel_dict["adress"]=hotel.find("span", {"itemprop": "streetAddress"}).text
hotel_dict["price"]=hotel.find("span", {"class": "ListingPrice_finalPrice"}).text



try:
     hotel_dict["rating"]=hotel.find("span", {"class": "hotelRating_ratingSummary"}).text
except AttributeError:
         hotel_dict["rating"]=None



parent_amenities_element=hotel.find("div",{"class": "amenitywrapper"})

amenities_list=[]
for ammenity in parent_amenties_element.find_all("div", {"class": "amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

hotel_dict["amenities"]=','.join(amenities_list[:-1])

scrapped_info_list.append(hotel_dict)
connect.insert_into_table(args.dbname,tuple(hotel_dict.values{}))

dataFrame=pandas.DataFrame(scrapped_info_list)
print("creating csv file...")
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)

