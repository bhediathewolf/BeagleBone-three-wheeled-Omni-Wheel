# BeagleBone three-wheeled Omni Wheel
This is the code for 8 axis movement for a three-wheeled omni wheel robot. This was used in ASME E-Fest 2018 Asia Pacific by Team B.E.A.S.T.

## Getting Started
These instructions will help you setup and effectively run the code on your BeagleBone embedded Linux machine. Personally, I was working with BeagleBone Black Wireless. I used `Adafruit_BBIO` which was on Python 2. Hence, I ended up with a Pyhton 2.x code instead of personal preference, Python 3.x

### Prerequisites
I am assuming you have an up-to-date system.
First, you need to install `pygame` on your system. As stated above, I used Python 2.x. For installing `pygame` on Angstorm, you must run the following command.
```
sudo apt-get install python-pygame
```
This command installs it for the default python version. In Case, you are using Python 3.x your pygame will be installed for the same.

You might run into few errors while setting up `pygame`. Bear with it because that is the hard part.

#### ERROR: SDL Config
A common error during installation of `pygame` is SDL config error. Pygame depends on SDL 1.2 which might not be installed on your system. You can install it by:
```
mkdir tmp
cd tmp

# download and install SDL
wget http://www.libsdl.org/release/SDL-1.2.14.tar.gz
tar -xzvf SDL-1.2.14.tar.gz
cd SDL-1.2.14
./configure 
sudo make all
```

#### ERROR: pygame.error: video system not initialized
After installing a headless Debian on my BB, my code threw this error even though it was working on Angstorm. After several failed attempts, I rewrote the code using another library as my motive was to get input from the joystick rather than Pythonic game development. If you find a solution for the same, please share it with me.

### Installing
You can simply clone my repository and start tweaking
```
git clone https://github.com/bhediathewolf/BeagleBone-three-wheeled-Omni-Wheel.git
cd BeagleBone-three-wheeled-Omni-Wheel
python wheel.py
```

For running this code automatically, everytime you boot, there are wo ways to do so.
First, using `crontab`:
```
crontab -e
```
Add a new line to your `crontab` at the end of the file,
```
@reboot python /path/to/file/wheel.py
```

Second, put your file in the Cloud9's autorun folder:
```
cp /path/to/file/wheel.py /var/lib/cloud9/autorun
```
I am not that confident about the second method but you are welcome to try.

## Built With
* [Adafruit BBIO Library](https://github.com/adafruit/adafruit-beaglebone-io-python/) - This is the python library used for interacting with the BeagleBone's pins.
* [PyGame](https://en.wikipedia.org/wiki/Pygame) - This is the Python library used for getting input from the joystick.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
* [YAMEB's post on Gamepad Input using PyGame](https://yameb.blogspot.in/2013/01/gamepad-input-in-python.html) - This page was the inspiration for much of the code structure.
