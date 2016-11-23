# AWDeals-Notifier

Simple Python script that will alert you via text message when 'Amazon Warehouse Deals' shows up in the sellers section of a listing. Very basic right now and only supports watching one item. Requires python3.0+

Refreshes the page every 60 seconds - when AMWDeals is found in the seller's section, it will send you a text message and wait for 7 minutes before refreshing again (I found this to be a good time for the item I was using, feel free to switch this depending on how fast your item sells out).

####To run:
Requires the 'twilio' and 'requests' python libraries (get via pip or easy install). To run, input your twilio info and the product's seller page (use a link shortening serivce to shorten this as this will be texted to you) and a custom name in the config.py. Then run the driver.

####To do:
* Multiple item support
* More config settings (e.g. time intervals)
* Price changes
