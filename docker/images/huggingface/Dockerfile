# Use NVIDIA Docker Image with pytorch
FROM nvcr.io/nvidia/pytorch:23.12-py3

# Set environment variables (permanent) for GPU Usage
# In this case, there are 4 GPUS but one GPU is broken. (GPU 2)
ENV CUDA_DEVICE_ORDER PCI_BUS_ID
ENV CUDA_VISIBLE_DEVICES 0,1,3

# install pip packages for data analysis
RUN pip install --upgrade pip
RUN pip install umap-learn[plot] \
	scikit-dimension \
	statsmodels \
	kmodes \
	kneed \
	feature_engine \
	tqdm \
	hdbscan \
	ipywidgets

# install huggingface libraries
RUN pip install datasets \
	accelerate \
	transformers \
	evaluate \ 
	nvidia-ml-py3 

# install bitsandbytes library for quantization 
RUN git clone https://github.com/timdettmers/bitsandbytes.git
RUN cd bitsandbytes \
	&& CUDA_VERSION=123 make cuda12x \
	&& python setup.py install

