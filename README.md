# NowInStockChecker

### What It Does
Checks Best Buy's website for a particular, often sold out item. When it detects the item being in stock, it will:
* Text you (email-to-mobile services offered by your relevant carrier).
* Print on the console a message saying "**In Stock, Let's GOOOOOOOOOOOOOOOOOO"**".
* Play out loud a voice saying "**IN STOCK**" (assuming you're on Mac and have `say`, a text to speech converter). 

It currently repeatedly checks for the item in a range between 6 and 15 seconds (can be configured).

### Context

At the onset of COVID-19, I was particularly interested in an Oculus Quest (all-in-one VR headset), but the item would often be sold out. I tried using [NowInStock.net](http://www.nowinstock.net), but its notification system was too slow, since by the time I was notified, it'd often be sold out.

Also, I noticed that [NowInStock.net](http://www.nowinstock.net) didn't check Best Buy's inventory for some reason, so I thought Best Buy was a good candidate to find the product I was interested in.

### Additional Challenges
Interestingly, the first day I coded it was also the day I got an order in succesfully.

That being said, I had to encounter several fluctuations in between "In Stock" and "Out of Stock" before I got it, since even when I went to the website and attempted to place an order having seen the item in stock, when it came time to add to the cart, it would disappear, and I'd get a message saying effectively try again. My current working hypothesis is that there were several other people (resellers?) with their own programs attempting to place an order for the Oculus Quest in rapid fire order, and Best Buy's website/system had a hard time keeping balance of what they had in stock.

### Conclusion
While what I wrote was very much tuned to Best Buy, I believe it can be easily adapted for other websites, including Walmart. I was in the process of working to adapt it to Walmart's website, but I ended up getting my Oculus Quest, and my interest died out. I may pick up on this project again for my next "particular, often sold out item."
