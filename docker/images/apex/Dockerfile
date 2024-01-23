FROM nvcr.io/nvidia/tensorflow:23.04-tf2-py3

RUN pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

RUN export CUDA_DEVICE_ORDER=PCI_BUS_ID
RUN export CUDA_VISIBLE_DEVICES=0,1,3

RUN git clone https://github.com/NVIDIA/apex

RUN cd apex && pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --global-option="--cpp_ext" --global_option="--cuda_ext" ./

RUN pip install datasets accelerate transformers nvidia-ml-py3

# install bitsandbytes for quantization
RUN export PATH=/usr/local/cuda-11.7/bin${PATH:+:${PATH}}
RUN export LD_LIBRARY_PATH=/usr/local/cuda-11.7/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
RUN export CUDA_HOME=/usr/local/cuda-11.7

RUN pip install bitsandbytes
