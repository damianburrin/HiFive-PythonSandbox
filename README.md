# HiFive Python Sandbox

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/c33701bb-a6c9-4037-a7c6-736085977f69)


**CONTEXT**

In 2019 i was lucky enough to be approached by the BBC to help support the development of the HiFive Inventor.  The purpose of this board was meant as a fully supported coding tutorial environment using both block based and python based programming, all supported by the awesome guys at Tynker.  I worked on testing the development through many iterations until the boards final release and I was even able to get some of my Y7 students (who were the target age group) so early version that they could try out in the real world and they loved them.

The development and launch was hit by covid but the board eventually went on sale in 2020.  The Dr Who theme and learning materials were really good and had lots of potential to inspire young coders.

The board was a ARM based board developed by SiFive and was made to be similar in format to the BBC Micro:bit, but this board had the additional features of built in ESP32 wifi chip making it a true IOT device.

In 2024 some of my students who were still activly using the boards reported that the Tynker website (hifiveinventor.com) was no longer there - I reached out to Tynker who responded that the project was only short term and had run its course so they no longer supported the device.  I tried contacting the BBC team but had no reply.

So this left us in a difficult position - all through the development process I was championing the idea of a sandbox environment.  What would students do once they'd finished the tutorials?  The boards were so powerful compared to the standard Micro:bit that it would be a shame if there was no ongoing support.  The coding environement for python and block did allow you to sandbox and create your own programs but you were locked into having a Tynker account and the environemnt was quite restrictive.  Now that had gone these boards are useless.


**June 2024**

Having been bagered by one of my awesome students (JS) now a year 10 and in my GCSE group who wanted to do more with his board I began to look back at my resources from the development and realised I probably have enough stuff to enable people to keep using these boards in python

**Resources**

The resources here are no fully tested, they certainly have no wararanty and may kill your board (doubtful) but as it no use to yopu anyway aznd is just a £70 paper weight what have you got to lose?

**COPYRIGHT**

Some of the resources I have collated here are in my opinion open source.  The Mu Environement for example is open source so the addtions made by the development to this should fall into it's open source remit
Some of the resources here a clearly copyright for the development teams whether these are MicroPython based or not and if asked by the developers i will remove these.  I will also email the contacts i still have to say these are online and if there is an issue I will remove them.  My goal here is to give you back a working device.  Which at the moment, despite buying these in good faith you no longer have.

The following names are people who I recall working on this project under the direction of Kara Iconis at the BBC and are credtited with the work i'm hosting here.
<li>Tynker</li>
<li>SiFive</li>
<li>Sam Grove</li>
<li>Michael Umansky</li>
<li>Jeff Mullhausen/li>
<li>Sarah Rodzevik</li>
<li>Rshishko</li>
<li>David Connelly</li>
<li>Don Robinson</li>
<li>Miodrag Milanovic</li>
<li>Zain Ali</li>
<li>KlikaTech</li>

**Using Your board**

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/040ed882-d376-4cc6-92fe-75ecaf91e58f)


**The first thing you will want to do is update your board.**  
The final version of MicroPython that I have is the version that came with the unreleased HiFive Updater.
Use the update all.  This will not only update the bootloader and micropython firmware but will also importantly update the EPS32 software so it becomes accessible via MicroPython.

**Caveat  
Now a quick caveat here.  I recommend  doing the update and then disconnecting the board and the updating again.  In my recolaections there was a problem with the wifi update saying it had worked but then not actually allowing a connection.  This was due to a bug in the JLink version.  Updating will replace the Jlink version and then the second update should successfully update the wifi correctly.**

If you get "asserion error" while calling the ESP32 this was due to this error and is normally fixed by re-updating.

**Uploading your code**

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/391888a8-1fbb-49ed-b04a-b96a3d0f5f7a)

You cannot put python files onto the HiFive.  They need to be in HEX format.  The tools in the manual upload folder are there to acheive this.  
Simply put the files into a folder, save the python file in the same folder and then edit the docombine.bat file

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/eb36d180-b1c5-44d4-bbcd-05e3b845ca6c)

You will need to change the two highlighted sections.  First to the name of the file you want to convert and the second to what you want to call the hex file
Once you run the docombine.bat file it will combine your python file with micropyhon into a hex file that you can just drag and drop onto your hifive.  (I recommend doing this in shell - CMD as you will see any error messages and completion messages)

**MU for HiFive**

One thing I really tried to get developped was an external programming IDE.  An Alpha resease of MU with HiFive support was forked but never released.

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/de18ef57-6357-43cb-99d1-e215154cdb7c)

If you install this version of Mu you will have a Hifive mode

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/d2e54df6-fe62-4501-a734-4eea3ea52fbf)

Which will let you upload files directly to the HiFive without needing to manually hexify them and also has a built in REPL to aid with testing so you won't be relient on putty

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/97163a7d-647d-45d1-bfb8-a4cb6acb3370)

**EXAMPLE CODE**

![image](https://github.com/damianburrin/Hi5-PythonSandbox/assets/18092613/5adc2f55-a8d7-40a9-bc0a-b21f8521123d)

Finally here is some example code - the code here is tested as working on my hifive with the updates done as per this document

ISSData.py  - This shows you how to connect your WIFI internet and use a GET request.  In this example it gives you a live upate of the people currently onboard the ISS

The two weather data files show you how to use an API, connect to its service and get the current weather.  In my case for Lincoln, UK

SimpleWebServer.py is a really simple example of how you can use the HiFive as a simple Webserver.  In this case it collects the data from the temperature sensor and then displays this to anyone on your network, via a webpage, that has access to the IP address.  With a little work with dynamic DNS and IP forwarding this could be anyone in the world!!

**You Tube Support**

I have a playlist at https://www.youtube.com/playlist?list=PLvZXTXiQDCe7YSpDQmd2ksVSHb431ns7F

**Conclusion**
I do hope this get users of HiFives back up and running.  I hope that the BBC, Tynker and the many developers do not ask for me to remove this material and I will try to support as many HiFive users as I can to make there devices usable for the future.

I provide this only with the intent to help to users out there and for no commercial or personal gain.  If you find this helpful feel free to buy me a coffee or drop me a message

https://www.buymeacoffee.com/damianburrC



