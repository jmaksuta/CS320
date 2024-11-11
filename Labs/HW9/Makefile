CURRENT_DATE=$(shell date +%Y-%m-%d-%H-%M)
FILE_SUFFIX=John-Maksuta-CS320-801-HW9-1
TARGET_DIR=./
zip:
	zip -r "$(CURRENT_DATE)-$(FILE_SUFFIX).zip" $(TARGET_DIR)

date:
	echo $(CURRENT_DATE)

run:
	python testmain.py

style:
	python pycodestyle.py main.py