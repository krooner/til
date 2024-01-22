FROM jupyter/datascience-notebook:latest

USER root

# install konlpy and other libraries for data analysis
RUN pip3 install konlpy umap-learn hdbscan

# download malgun-gothic font for hangul visualization
RUN wget https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun-gothic.zip && unzip malgun-gothic.zip

# install mecab-ko
RUN wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
RUN tar xvfz mecab-0.996-ko-0.9.2.tar.gz
RUN cd mecab-0.996-ko-0.9.2/ && \
./configure && \
make && \
make check && \
ldconfig && \
make install

RUN cd ../

# install mecab-ko-dic
RUN wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
RUN tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
RUN echo "/usr/local/lib" >> /etc/ld.so.conf && ldconfig
RUN cd mecab-ko-dic-2.1.1-20180720/ && \
./configure && \
make && \
make install

RUN cd ../

# mecab-python
RUN pip install mecab-python
