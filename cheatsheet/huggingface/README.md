# Huggingface Cheatsheet

## Tensor
### [`torch.Tensor.{detach(), cpu(), numpy()}`](https://iambeginnerdeveloper.tistory.com/211)

|API|Description|
|---|---|
|[`torch.Tensor.detach()`](https://pytorch.org/docs/stable/generated/torch.Tensor.detach.html)|현재 (Tensor 연산) 그래프에서 떼어낸, 새로운 Tensor를 반환. 반환된 결과는 Gradient를 필요로 하지 않음.|
|[`torch.Tensor.cpu()`](https://pytorch.org/docs/stable/generated/torch.Tensor.cpu.html)|CPU 메모리에 Tensor의 복사본을 반환. 이미 CPU 메모리에 있는 경우, 복제는 발생하지 않고 원본이 반환됨.|
|[`torch.Tensor.numpy()`](https://pytorch.org/docs/stable/generated/torch.Tensor.numpy.html)|Tensor를 NumPy 배열로 반환한다. Parameter 중 `force=False` (default) 인 경우에는 Tensor가 CPU에 있는 경우에만 수행된다.|

## Logging
### [`torch.utils.tensorboard`](https://pytorch.org/docs/stable/tensorboard.html)
공부해야됨

## DataLoader
[DataLoader 저장](https://discuss.pytorch.org/t/how-to-save-dataloader/62813/4)

## Loss
### [`torch.nn.CrossEntropyLoss`](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html)
- [Multiclass Classification](https://076923.github.io/posts/Python-pytorch-13/)


## Optimizer
### [`torch.optim.Adam`](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html)
- [PyTorch Weight decay](https://sanghyu.tistory.com/88)

## Model
- [PyTorch 모델 저장 및 로드](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_models_for_inference.html)


## Distributed Training
[PyTorch multi-gpu 학습 제대로 하기](https://medium.com/daangn/pytorch-multi-gpu-%ED%95%99%EC%8A%B5-%EC%A0%9C%EB%8C%80%EB%A1%9C-%ED%95%98%EA%B8%B0-27270617936b)

## ERROR
Error message and description

```
RuntimeError: "nll_loss_forward_reduce_cuda_kernel_2d_index" not implemented for 'Int'
```

[Casting label to LongTensor](https://stackoverflow.com/questions/69742930/runtimeerror-nll-loss-forward-reduce-cuda-kernel-2d-index-not-implemented-for)

```
ImportError: This example requires a source install from HuggingFace Transformers (see `https://huggingface.co/docs/transformers/installation#install-from-source`), but the version found is 4.37.1.
Check out https://github.com/huggingface/transformers/tree/main/examples#important-note for the examples corresponding to other versions of HuggingFace Transformers.
```

`torchrun`을 활용한 Distributed Training 수행 시에 발생하는 에러 메시지. Huggingface를 설치할 때 `pip`로 설치하지 말고 `source`로 설치하자. `source`로 설치하면 __stable__ version이 아닌 up-to-date and latest __main__ version을 활용할 수 있다. 반대로 말하면 stable에서는 발생하지 않던 버그가 main에서는 발생할 수 있다. 그래서, `$ pip install git+https://github.com/huggingface/transformers`

```
NotImplementedError: Using RTX 3090 or 4000 series doesn't support faster communication broadband via P2P or IB. Please set `NCCL_P2P_DISABLE="1"` and `NCCL_IB_DISABLE="1" or use `accelerate launch` which will do this automatically.
```

RTX 3090 4대가 연결되어 있는 워크스테이션에서 Distributed Training을 수행하려고 할 때 발생하는 에러 메시지. `$ NCCL_P2P_DISABLE="1" && NCCL_IB_DISABLE="1"` 또는 실행할 .py 파일 내에서 `import os; os.environ["NCCL_P2P_DISABLE"]="1"; os.environ["NCCL_IB_DISABLE"]="1"` 적용을 해도 동일 오류가 발생함.

```
/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py:138: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 2: out of memory (Triggered internally at /opt/pytorch/pytorch/c10/cuda/CUDAFunctions.cpp:108.)
  return torch._C._cuda_getDeviceCount() > 0
cpu
```

GPU 4장이 연결되어 있을 때 문제가 있는 특정 GPU를 포함하고 다음 코드를 실행했을 때 발생하는 에러 메시지. `import torch; device = "cuda" if torch.cuda.is_available() else "cpu"; print(device); print(torch.cuda.current_device()`. GPU 2번을 제외하여 `CUDA_VISIBLE_DEVICES=0,1,3` 를 환경변수로 설정한 이후에는 해당 에러가 발생하지 않음.

