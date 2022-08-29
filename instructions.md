
1 - Run:  
bash build.sh  
  
Jpgs will be found in data/apod.  
If you don't have the .tar bitorrent client will download them for you.  
  
2 - Activate venv:  
source venv/bin/activate  
  
3 - Install python module:  
cd src  
pip install .  
  
4 - Test python module.  Has to be run from src/:  
python setup.py test  
cd ../  
  
Please note that test will end in errors until database is full loaded.  
Can use pytest to check progress.  
  
5 - Start postgres:  
bash start.sh  
  
6 - From root load data into database:  
python src/main/assignment/load_database.py  
  
7 - Get random image as image file download:  
python src/main/assignment/main.py  
  
8 - At end of session deactivate venv  
deactivate  
  
9 - Close down docker:  
bash stop.sh  
