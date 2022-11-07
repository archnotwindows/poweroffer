# Poweroffer

<p align="center">
  <br>
  <a href="https://github.com/archnotwindows/poweroffer/">
    <img alt="Repo Size" src="https://img.shields.io/github/repo-size/archnotwindows/poweroffer?logo=github">
  </a>
  <a href="https://github.com/archnotwindows/poweroffer/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/archnotwindows/poweroffer?logo=github">
  </a>
  <a href="https://github.com/archnotwindows/poweroffer/pulls">
    <img alt="Pull requests" src="https://img.shields.io/github/issues-pr/archnotwindows/poweroffer?logo=github">
  </a>
</p>
<p align="center">
  <br>
  <a href="https://github.com/archnotwindows/poweroffer/fork">
    <img alt="Forks" src="https://img.shields.io/github/forks/archnotwindows/poweroffer?logo=github">
  </a>
  <a href="https://img.shields.io/github/stars/archnotwindows/poweroffer">
    <img alt="Stars" src="https://img.shields.io/github/stars/archnotwindows/poweroffer?logo=github">
  </a>

Whith this simple python program you will be able to not procrastinate during the day in some sort of website (like Youtube) that you can choose! so try it out!!
## Getting Started
  **WARNING!! to make this software work you must use a debian based linux distro and the Firefox web browser**
  
0 - Install **[Python](https://python.org)** on your machine. **Version 3.10 or higher is required!**
  
1 - Clone the repository on your machine.
  
2 - Put the poweroffer extracted folder in the Desktop

3 - Rename the folder in to poweroffer
  
4 - Install tkinter with these commands 
  
      sudo apt-get install python3-tk 
      pip install tk

5 - Install os,json and time ( but probably these libraries are already installed on your system)

6 - become a root user ( with " su " command and continue to do all the operations with root)

7 - Install lz4.block with this command 
      pip install lz4

8 - open a terminal emulator and write 
  
      crontab -e
  
  NOTE:if is your first time you may have to choose witch editor you wanna use

9 - write at the end of the file this string " * * * * * /bin/bash /home/your-username/Desktop/poweroffer/executable.sh "

10 - close the editor and save the changes

11 - search for this file "recovery.jsonlz4" and copy it's path

12 - edit the main.py file and scroll down until the line 48 

![Istantanea_2022-07-21_14-07-03](https://user-images.githubusercontent.com/108471111/180209819-e4a4d0e0-80db-4a75-8689-e00b6b1ed44a.png)


13 - replace the selected area with the path you have copied 

14 - replace int the path at the lines 39,46 and 66 the word "your-username" with your username

15 - exit from the root user and login to your everyday user 

16 - open a terminal and run the index.py file using " python3 index.py " to execute the program ( use this command every time you wanna run my program :)



## License

This project is licensed under either of:
- [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

## Contact

[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:lorenzo020406@gmail.com)
[![github](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/archnotwindows)
[![twitter](https://img.shields.io/badge/Twitter-007fff?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Lollopro59_)
[![stackoverflow](https://img.shields.io/badge/StackOverFlow-FF8000?style=for-the-badge&logo=stackoverflow&logoColor=white)](https://stackoverflow.com/users/19628082/archnotwindows)
