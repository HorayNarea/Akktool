## Setup  
  
get the code:  
```sh
git clone https://github.com/HorayNarea/Akktool  
cd Akktool  
```
  
or  
  
```sh
wget https://github.com/HorayNarea/Akktool/archive/master.zip  
unzip master.zip  
cd Akktool-master  
```  
  
optional, use a virtual environment:  
```sh
sudo apt-get install python-virtualenv  
virtualenv .venv  
source .venv/bin/activate  
```  
  
install and run:  
```sh
pip install -r requirements.txt  
python manage.py syncdb  
python manage.py runserver  
```  
  
  
open [http://localhost:8000/](http://localhost:8000/) in your browser  
  
  
## License  
see LICENSE-File  
  
--------
  
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=HorayNarea&url=https://github.com/HorayNarea/Akktool&title=Akktool&language=en_GB&tags=github&category=software)
