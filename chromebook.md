## Data Science on a Chromebook

# My notes on using chrome os with crouton as a data scientist 

Specs / Architecture
-------------
- Samsung Chromebook Pro ($550 at the time)
- x86 architecture: Intel m3 6Y30 - 2 cores @ 0.9 GHz (Max 2.2 GHz)
- Chrome OS version 58
- RAM: 4 GB LPDDR3
- MicroSD: 64 GB
- Integrated graphics: Intel HD Graphics 515
- Stylus (galaxy style)

- You can see most of these via `chrome://system` on chrome os.
- The x86 processor is very different from most chromebooks on the market which are ARM processors, I wanted an x86 because I wasn't sure if julia would work with ARM.

Developer Mode
------------
- The first thing I did was put the chromebook into developer mode.  To do this, you should hit esc, refresh, and the power button at the same time.  This will reset into Recovery mode, and you will probably see some warning.  This is apparently not for the faint of heart.
- Hit CTRL-D at the Recovery screen.  Then when you see 'To turn OS verification OFF, press Enter'.  You want OS verification off so that changing something will not cause your machine to fail to boot.  Henceforth, every time that you boot, you will see a screen saying that OS verification is OFF and you should turn it on.  Do NOT press the space bar here, it can rewrite all of your hard work.
- You will have to wait 15 min or so to get developer mode installed.  I recall seeing an opportunity to Enable Debugging Features in the first startup in developer mode.  Then you can set a root password, and Enable.
- Now you can start a terminal, by hitting Ctrl-Alt-t, which will open a chrome window with a crosh shell.  In this type `shell` and you will get a bash shell.

Conda and Chromebrew
-------------
In the bash shell, I did several things.  I wanted to be able to run jupyter, ipython, git, ssh, etc in the chrome OS, as opposed to relying on crouton.

- [chromebrew](https://github.com/skycocker/chromebrew) will install various packages on chrome os.  Follow the instructions on the README.
- [anaconda](https://www.continuum.io/downloads#linux) will lead you to the installation page for anaconda.  The x86 installer will only work on chromebooks with x86 processors, so you will need to be sure that if you are using an ARM processor that you use the ARM installer.  Once you have downloaded the file, in your Downloads folder, you need to run `sh Anaconda_[version stuff].sh`.
- I [set git credentials](https://help.github.com/articles/caching-your-github-password-in-git/) so that I don't have to keep typing in my username and password.
- I can now use the jupyter notebook in my code folders by `jupyter notebook` and navigate to the link that it displays.

SD Card
-------------
So that I don't gum up the works on my SSD, I wanted to install crouton and keep all of my projects on my SD Card.

- My SD Card device is mmcblk1 (which I found by looking at the size of those devices).  Be very careful that you have the SD Card, because if you format another device such as your solid state drive then you will have very big issues.
- I needed to format the SD Card and make it Ext4 format: You can follow [this tutorial](http://www.aaronbell.com/sd-card-performance-tuning-on-chromebook/) but I ended up using `mkfs.ext4` and `fdisk`.
- I found that when I mount the SD Card, it will get unmounted when I close the lid and at other times, so I ended up following [this answer](http://wuyuanyi.blogspot.com/2015/09/chrome-os-crouton-suspendresume-causes.html) which runs `echo 1 | sudo tee /sys/bus/usb/devices/1-7/power/persist`.  I am not sure if I will see other issues relating to this.  You can mount your SD Card with `sudo mount /dev/mmcblk1 /media/removable/SD\ Card`.
- I created a folder `Projects` on the SD Card root directory (it is in `cd /media/removable/SD\ Card`) which contains all of my project repositories.  I also created a symbolic link to this `ln -s /media/removable/SD\ Card/Projects/ ~/Projects`.
- One annoying issue is that the Files app will not let you navigate wherever you want.  And after formatting my card, I can't see it mounted (even though it is).  So I actually use chrome to navigate and open files.  So I created a bookmark for `file:///media/removable/SD\ Card/Projects/` on chrome.
- By using `hdparm`, I can see that the read speed from my SD Card is `40 MB/sec` and for my SSD is `200 MB/sec` so the latency ratio is 1:5.  Because I do not plan to work with large datasets on this machine then that is fine with me.

Crouton
--------------
I partially followed the [crouton installation instructions](https://github.com/dnschneid/crouton) but wanted to install on the SD Card:
- `mkdir /media/removable/SD\ Card/chroots` where crouton will be installed
- `ln -s /media/removable/SD\ Card/chroots/ /usr/local/chroots` since this is the default install location for crouton
- Download crouton and run `sudo sh ~/Downloads/crouton -t unity` (I wanted to install unity - although I wont use it much).
- Upgrade crouton with xiwi, `sudo sh ~/Downloads/crouton -u -t xiwi`,  which makes it so that you can use the chrome os clipboard.
- Now I can enter into chroot with `sudo enter-chroot` and I am now in ubuntu.

Linux Installations
--------------
- I installed emacs with `sudo apt-get install emacs` and `sudo apt-get install elpa-markdown-mode` (I will probably also install python-mode).
- I installed julia with `sudo apt-get install julia`

