FROM python:3.9.13

WORKDIR /manhpv3_tabai
COPY requirements.txt /manhpv3_tabai

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip install gdown

#STEP6: Download file weight
RUN gdown "https://drive.google.com/uc?export=download&id=1VIplhJoaKPI08Qcdq6FhPk_dMvGOfDMp"

COPY . /manhpv3_tabai
RUN chmod +x run.sh
CMD ./run.sh