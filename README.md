How to use:
=====================

To retrieve the results, copy the iwo.sh and iwo.py files into a personal directory on karora (for example, create a directory called iwo/).
To make sure it will run, run the following commands:

$ chmod a+x iwo.sh
$ chmod a+x iwo.py

To run the iwo.sh script, you can use either of the following commands:

$ ./iwo.sh
$ nohup ./iwo.sh

The second command writes the output of the terminal to an extra file called nohup.out, 
which ensures that the command will keep running after the terminal is closed.
This may be useful because the script has to go over a large dataset so it may take some time, 
and may otherwise stop running if the terminal is accidentally closed or if the user loses connection.

The dataset used is the following:

/net/corpora/twitter2/Tweets/ (on karora)

This script only needs the data from December (directory 12) of 2019 to June (directories 01, 02, 03, 04, 05, 06) of 2020.

The script creates a list of files:

n12.txt
n01.txt
n02.txt
n03.txt
n04.txt
n05.txt
n06.txt

After retrieving this data, the script of iwo.py can be used. 
To run the script, use the following command:

$ Python3 iwo.py

The output of this file will not be stored in a serperate file, 
but can be read directly from the terminal window. It should give
the following output:

________________________________________________________
               01-12-2019 - 15-03-2020:
Total: 54113279
Tweets containing search terms: 75747

Percentage: 0.14%
________________________________________________________
               16-03-2020 - 30-06-2020:
Total: 67056248
Tweets containing search terms: 91717

Percentage: 0.14%
________________________________________________________
