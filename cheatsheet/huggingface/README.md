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

`RuntimeError: "nll_loss_forward_reduce_cuda_kernel_2d_index" not implemented for 'Int'`
- [Casting label to LongTensor](https://stackoverflow.com/questions/69742930/runtimeerror-nll-loss-forward-reduce-cuda-kernel-2d-index-not-implemented-for)