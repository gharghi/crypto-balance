# Crypto Balance

This is a simple application written in Django to demonstrate how to give a crypto wallet balance. \


## How to Install

You may Install Python, create a Virtualenv after cloning the project and change the source to it:\
brew install python3 python3-pip \
pip3 install virtualenv \
virtualenv venv \
source venv/bin/activate 


Install the required packages: \
pip install -r requirements.txt 



python manage.py test \
python manage.py runserver 0.0.0.0:8000 


## How to Test
Call the post method of http://127.0.0.1:8000/api/v1/balance with a body like below as json to see the result\
{\
    "network": "ETH",\
    "address": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"\
}

Application is also available on https://balance.gharghi.com/. So, you can call it by https://balance.gharghi.com/api/v1/balance
