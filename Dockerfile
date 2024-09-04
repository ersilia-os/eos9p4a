FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2024.3.5
RUN pip install torch==2.4.0
RUN pip install omegaconf==2.3.0

WORKDIR /repo
COPY . /repo
