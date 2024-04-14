# Huggingface Cheatsheet

## Gated Model/Tokenizer 호출을 위한 Huggingface Hub Login
```python
access_token = "<your_token_generated>"

from huggingface_hub import login
login(token=access_token)
```

`kakaobrain/kogpt` 모델을 호출하려 했으나 `gated model`로 설정되어 있어 Huggingface에서 발급하는 token이 필요하다. VSCODE에서 jupyter notebook을 실행하는 경우, Cell에서 `!huggingface-cli login`을 했을 때 Token을 입력할 수 없는 문제가 발생했다. 대신에 `huggingface_hub` 라이브러리를 활용해서 로그인을 수행했다.

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

### Checkpoint 저장 주기 설정 [`--save_steps`](https://discuss.huggingface.co/t/saving-model-per-some-step-when-using-trainer/11553/2)

BERT/GPT 모델 학습 시 Trainer 함수는 기본적으로 500 Step마다 Checkpoint를 생성하는데, 전체 data 수 대비 batch-size가 작아서 Gradient update가 잦은 경우 매우 빈번하게 모델을 중간 저장하므로 해당 Argument에 적당한 값을 부여해서 저장 주기를 조절할 수 있다.

## Tokenizer

### Tokenizer에 [새로운 토큰 추가](https://huggingface.co/docs/transformers/en/internal/tokenization_utils#transformers.SpecialTokensMixin.add_tokens) 및 [Model에 반영하기](https://huggingface.co/docs/transformers/en/main_classes/model#transformers.PreTrainedModel.resize_token_embeddings)
`밥 -> 반찬`이라는 텍스트를 Tokenizer할 경우
- AS-IS: `밥, <UNK>, 반찬`
- TO-BE: `밥, ->, 반찬`

```python
num_added_tokens = tokenizer.add_tokens(["->"])
model.resize_token_embeddings(len(tokenizer))
# Embedding(51201, 768)
```

1. 사용할 tokenizer의 vocab에 새로운 token을 추가한다.
2. Update된 tokenizer의 vocab_size에 맞게끔 model의 token_embedding_size를 업데이트 한다.


### [BOS, EOS 토큰을 추가하고 싶은 경우](https://discuss.huggingface.co/t/gpt2tokenizer-not-putting-bos-eos-token/27394/2)

Tokenizer가 '안녕하세요'를 Tokenize할 때
- AS-IS: `_안녕, 하, 세, 요`
- TO-BE: `[BOS], _안녕, 하, 세, 요, [EOS]`

```python
from transformers import GPT2TokenizerFast
from tokenizers.processors import TemplateProcessing

tokenizer = GPT2TokenizerFast.from_pretrained(
  'skt/kogpt2-base-v2',
  truncation_side='left' # max_length 초과 시 왼쪽 (Old in time-ascending order) 부터 제거
)

# tokenizer.post_processor = TemplateProcessing(...) <- IT WONT WORK!
tokenizer._tokenizer.post_processor = TemplateProcessing(
  single="<s> $0 <\s>",
  special_tokens=[("<s>", tokenizer.bos_token_id), ("</s>", tokenizer.eos_token_id)]
)

prompt = '안녕하세요'
prompt_tokenized = tokenizer(prompt, padding='max_length', truncation=True, max_length=model.config.n_positions)
tokenizer.convert_ids_to_tokens(prompt_tokenized['input_ids'])
# <s>, _안녕, 하, 세, 요, </s>
```

`post_processor` 함수는 `tokenizers` 라이브러리에 있는 tokenizer에만 존재하고 `transformers` 라이브러리에 있는 tokenizer에는 적용되지 않는다. transformers 라이브러리의 `tokenizer._tokenizer` Object는 tokenizers 라이브러리의 tokenizer이므로 해당 Object를 변경하면 된다.


## Distributed Training
[PyTorch multi-gpu 학습 제대로 하기](https://medium.com/daangn/pytorch-multi-gpu-%ED%95%99%EC%8A%B5-%EC%A0%9C%EB%8C%80%EB%A1%9C-%ED%95%98%EA%B8%B0-27270617936b)
- GPU 4장이 달린 워크스테이션을 가지고 BERT 모델을 Multi-GPU로 학습하는 내용 설명. 본인 작업과 매우 유사하여 참고함. Multi-GPU 활용 방법을 단계적으로 잘 설명함.

[Huggingface를 활용하여 Distributed Training 수행하기](https://github.com/huggingface/transformers/tree/main/examples/pytorch#distributed-training-and-mixed-precision)
- GPU ~~4~~ 3장 (1장 broken) 으로 `torch.nn.Parallel()`을 활용하여 BERT 모델을 Finetuning (1 Epoch) 함에도 약 80시간이 소요. 학습 시간을 대폭 줄이고자 직접 Multi-GPU를 활용한 Distributed Training 방법으로 수행하기 위해 참고한 문서
- Command

```bash
torchrun --nproc_per_node 3 run_mlm.py --model_name_or_path <MODEL_NAME_PATH> --tokenizer_name <TOKENIZER_NAME_PATH> --train_file <LINE_BY_LINE_SEQ_TEXT> --per_device_train_batch_size 64 --do_train --output_dir <MODEL_OUTPUT_PATH> --ddp_timeout 7200 --dataloader_num_workers 3 --dataloader_prefetch_factor 2 --overwrite_output_dir --gradient_checkpointing --gradient_accumulation_steps 2 --line_by_line --optim adamw_hf --num_train_epochs 1 --save_steps 5000
```

## [SOLVED] ERROR

```
RuntimeError: "nll_loss_forward_reduce_cuda_kernel_2d_index" not implemented for 'Int'
```
- MLP 모델 학습을 위해서 (input, label) 형태 데이터를 로드하고, Dataset을 새로 생성했을 때 label에 해당하는 Tensor의 Type이 적합하지 않아 발생했던 에러 메시지.  [Casting label to LongTensor](https://stackoverflow.com/questions/69742930/runtimeerror-nll-loss-forward-reduce-cuda-kernel-2d-index-not-implemented-for)를 참고하여 Dataset 내부에서 Casting을 적용하니 문제 해결.

```
ImportError: This example requires a source install from HuggingFace Transformers (see `https://huggingface.co/docs/transformers/installation#install-from-source`), but the version found is 4.37.1.
Check out https://github.com/huggingface/transformers/tree/main/examples#important-note for the examples corresponding to other versions of HuggingFace Transformers.
```
- `torchrun`을 활용한 Distributed Training 수행 시에 발생했던 에러 메시지. Huggingface를 설치할 때 `pip`로 설치하지 말고 `source`로 설치하여 문제 해결. `source`로 설치하면 __stable__ version이 아닌 up-to-date and latest __main__ version을 활용할 수 있다. 반대로 말하면 stable에서는 발생하지 않던 버그가 main에서는 발생할 수 있다. 그래서, `$ pip install git+https://github.com/huggingface/transformers`

```
NotImplementedError: Using RTX 3090 or 4000 series doesn't support faster communication broadband via P2P or IB. Please set `NCCL_P2P_DISABLE="1"` and `NCCL_IB_DISABLE="1" or use `accelerate launch` which will do this automatically.
```
- RTX 3090 4대가 연결되어 있는 워크스테이션에서 Distributed Training을 수행하려고 할 때 발생했던 에러 메시지. `$ NCCL_P2P_DISABLE="1" && NCCL_IB_DISABLE="1"` 또는 실행할 .py 파일 내에서 `import os; os.environ["NCCL_P2P_DISABLE"]="1"; os.environ["NCCL_IB_DISABLE"]="1"` 적용을 해도 동일 오류가 발생함. Docker Image를 새로 생성하고자 Dockerfile 내에 `ENV NCCL_P2P_DISABLE 1; ENV NCCL_IB_DISABLE 1`를 추가하여 새로 build한 뒤 Container 실행 및 재작업하니 문제 해결.

```
/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py:138: UserWarning: CUDA initialization: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 2: out of memory (Triggered internally at /opt/pytorch/pytorch/c10/cuda/CUDAFunctions.cpp:108.)
  return torch._C._cuda_getDeviceCount() > 0
cpu
```
- GPU 4장이 연결되어 있을 때 문제가 있는 특정 GPU를 포함하고 다음 코드를 실행했을 때 발생했던 에러 메시지. `import torch; device = "cuda" if torch.cuda.is_available() else "cpu"; print(device); print(torch.cuda.current_device()`. GPU 2번을 제외하여 `CUDA_VISIBLE_DEVICES=0,1,3` 를 환경변수로 설정한 이후에는 문제 해결. GPU 2번에 하드웨어적 문제가 있는 것 같음.

```
[Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=880, OpType=ALLREDUCE, NumelIn=1, NumelOut=1, Timeout(ms)=7200000) ran for 7200595 milliseconds before timing out.
```

- 분산 학습을 설정한 상태 [(torchrun으로 Distributed Data Parallel로 학습)](https://velog.io/@codingchild/Huggingface-Transformers-Timeout-Issue-%ED%95%B4%EA%B2%B0)에서 많은 데이터 (약 12M에 달하는 사용자 시퀀스) 를 전처리 (Tokenize) 할 때 timeout으로 인한 에러 발생. [`--ddp_timeout`](https://github.com/huggingface/transformers/issues/17106#issuecomment-1313135141) argument의 default 값은 1800. 값을 증가시켜서 문제를 해결할 수 있음.
