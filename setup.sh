wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt-get -y update
apt-get install -y google-chrome-stable
apt-get install -yqq unzip
wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
pip install --upgrade pip
pip install -r requirements.txt

streamlit run index.py
