import booking

booking_data = booking.handle()
URL,headers = booking_data.url(main="Hotels",sub="Data_hotel")

booking_data.query(main="Hotels",sub="Data_hotel",paramete={'hotel_id':'12345','locale_num':1})

booking_main = booking.query()


querystring =booking_main.params

print(querystring)