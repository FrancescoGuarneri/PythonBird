PythonBird
==========

A Twitter tool written in Python for Unix systems

=============
LICENSE

This code is relased under the GPL version 3 license. See license.txt
License is available at http://www.gnu.org/licenses/gpl-3.0.txt

=============
EXTERNAL DEPENDANCIES

This code requires Tweepy package available at https://github.com/tweepy/tweepy
Simply get it and paste it in the same directory of this README.md file.
If you want to install it directly in your system using pip: 

pip install tweepy

=============
USAGE

Open your Unix shell, enter the same directory of this readme file and type:

python pythonbird.py

Follow the instructions. Actually you can unfollow people who don't follow you or send mass-DM to all your followers. You can also save a file with the last 1000 tweets of an user.
The code is not optimized and is a little bit slow. There are many things to do to make it better. 

=============
ISSUES

The Auth system will sometimes fail opening twitter's auth page if the browser is already opened.
Some tweets won't be saved due to carachters encoding issues. 
Code is really bad at this time, use it at your own risk. Many issues will be fixed in the next version.

=============
DISCLAIMER

I am not responsible for bad usage of this software, damages to systems or unlawful action.
This software is provided as is, the responsibility relies ONLY on the usage by the final user.
