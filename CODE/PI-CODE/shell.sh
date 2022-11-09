#bin/bash


curl --silent https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/ControllerClass.py | md5sum > https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/ControllerClass.py
if ! cmp https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/ControllerClass.py https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/ControllerClass.py > /dev/null; then
    
	wget https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/Controller.py
	wget https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/ControllerClass.py
	rm https://raw.githubusercontent.com/Phosvan/PAPI/main/CODE/PI-CODE/Controller*
    sudo python3 /PAPI/CODE/PI-CODE/Controller.py
fi
