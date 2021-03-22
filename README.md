# PrayerWheel
Micropython code for the Internet Prayer Wheel.

3D Printer files are at: https://www.thingiverse.com/thing:4787030

The Internet Prayer Wheel is designed to put good energies into the world when it is spun. Each Prayer Wheel is on the net, and the software is designed so that when one wheel is turned, all the wheels turn. The goal is to have all the wheels continuously turning because someone, somewhere in the world is making good thoughts.

The wheel is turned by a 40mm fan at the base, which drives a slave fan at the top of the wheel. The main spindle is a basic ball point pen. The reason for choosing this is that it has a tiny, precision ball bearing on the end which is perfect for the wheel to balance on.

Although you can run the software on any board running Micropython, I've used a Wemos D1 mini and a relay shield. I've set up an open MQTT broker for the wheels to listen to at prayerwheel.world. The same domain has a web page with a live live video of my wheel, and a button on the page to start the wheels turning. If you contact me I will give you an MQTT login which will allow you to put a switch on your wheel to start it, and all the others turning.

