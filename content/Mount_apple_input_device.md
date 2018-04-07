Title: How to pair apple input devices
Slug: apple-input-devices
Date: 2018-04-07 08:00
Category: raspberry pi
Tags: mouse, keyboard, raspberry pi, wifi, bluetooth
author: S.-H. Dan Shim

## How to pair bluetooth Apple keyboard and mouse with raspberry pi

I found that the on-board wifi causes issues with Apple wireless keyboard and mouse.  Only way to make them work with raspberry pi 3 is to turn it off.

I found the following tip from: <https://raspberrypi.stackexchange.com/questions/43720/disable-wifi-wlan0-on-pi-3>

I turn off on-board wifi by the following command

```bash
sudo iwconfig wlan0 txpower off
```
This one seems to turn off completely and take the additional wifi dongle as `wlan0`.

I believe to turn the on-board wifi on, I have to do the following.  But it is also possible that I need to do for `wlan1` instead.

```bash
sudo iwconfig wlan0 txpower on
```