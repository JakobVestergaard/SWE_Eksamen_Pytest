coverage run -m pytest notfailing.py
sleep 1s
coverage report -m
sleep 1s
coverage run -m pytest failtest.py
sleep 1s
coverage report -m
