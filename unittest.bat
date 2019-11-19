:: ------------- Unittest + coverage --------------------------------------
nosetests --with-coverage --cover-package=v_time --cover-erase --cover-inclusive
pause

:: ------------- Pylint ---------------------------------------------------
pylint test
cd v_time
pylint v_time
cd..
pause
