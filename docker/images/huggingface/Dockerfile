FROM nvcr.io/nvidia/tensorflow:23.04-tf2-py3

# install pytorch
RUN pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

# install pip packages for data analysis
RUN pip install --upgrade pip
RUN pip install umap-learn[plot] \
&& pip install scikit-dimension \
&& pip install statsmodels \
&& pip install kmodes \
&& pip install kneed \
&& pip install feature_engine \
&& pip install tqdm \
&& pip install hdbscan \
&& pip install ipywidgets

# default: use GPU 0
RUN export CUDA_DEVICE_ORDER=PCI_BUS_ID
RUN export CUDA_VISIBLE_DEVICES=0

# install huggingface libraries
RUN pip install datasets accelerate transformers nvidia-ml-py3 -q

# install bitsandbytes for quantization
RUN export PATH=/usr/local/cuda-11.7/bin${PATH:+:${PATH}}
RUN export LD_LIBRARY_PATH=/usr/local/cuda-11.7/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
RUN export CUDA_HOME=/usr/local/cuda-11.7

RUN pip install bitsandbytes
