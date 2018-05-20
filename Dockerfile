FROM python:3

ADD patchalerts ./patchalerts/
ADD requirements.txt ./

RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python", "-u", "./patchalerts/scanner.py"]