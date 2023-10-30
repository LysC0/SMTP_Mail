
PY = python3
PATH_MAIN = data/main.py
EXE=SMTP_MAIL

SMTP_LAUNCH : $(EXE) 

$(EXE):
	$(PY) $(PATH_MAIN)
