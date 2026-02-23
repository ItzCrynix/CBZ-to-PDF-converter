python -m venv venv

if [ -f "./venv/bin/activate" ]; then
	source ./venv/bin/activate
elif [ -f "./venv/Scripts/activate" ]; then
	source ./venv/Scripts/activate
else
	echo "No python enviroment was found."
fi

pip install --quiet pillow
pip install --quiet pypdf