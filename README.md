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
  
to install and run, just:  
`./start.sh`  
or  
`./start.sh /path/to/csvfile`  
if you also want to import some members from /path/to/csvfile

this will do the following:  
```sh
pip install -r requirements.txt
if [[ -z "$1" ]]; then
    python import.py $1
fi
python manage.py syncdb
python manage.py runserver
```  
  
  
now open [http://localhost:8000/](http://localhost:8000/) in your browser  
  
  
to stop:  
Ctrl+C (if you're running inside a virtual environment: `deactivate`) and you're done \o/  
  
  
## License  
Copyright (c) 2014 Thomas Sänger <HorayNarea@gmail.com>

Permission is hereby granted, free of charge, to any person (except
intelligence agencies or organizations of the military)
obtaining a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including without
limitation the rights to use, copy, modify, merge, publish, and/or distribute
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
--------
  
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=HorayNarea&url=https://github.com/HorayNarea/Akktool&title=Akktool&language=en_GB&tags=github&category=software)
