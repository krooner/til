# 한국어 기반 BERT/GPT 오픈소스 모델

## 목적
문제 해결을 위해 사용자의 행동 데이터에 언어 모델을 활용한다. 기존에는 `bert-base-cased` 와 같은 영문을 입력으로 하는 모델을 Fine-tuning하였다. 그러다보니 사용자 데이터를 영문으로 변환해야 하는 과정에서 정보 손실이 발생할 수 있다. 이번에는 한글 기반 언어 모델을 활용하고, 데이터 또한 기존의 전처리 방식을 변경하여 좀 더 효율적인 데이터 활용 및 Fine-tuning을 하고자 했다. Fine-tuning의 목적은 사용자 데이터에 대한 임베딩을 추출하여 Downstream Task의 성능을 높이는 것이다.


## 선정 기준

1. 학습 및 추론 시간을 고려하여 GPU 1대 (RTX 3090, RAM 24GB) 에서 학습 및 추론할 수 있는 모델이어야 한다.
2. 시간적 제약을 고려하여 모델을 비교적 쉽게 불러올 수 있어야 한다. 

## 후보 모델

|Architecture|Tag|Description|
|---|---|---|
|GPT|[kakaobrain/kogpt](https://huggingface.co/kakaobrain/kogpt)|❌ [base는 32GB 요구 되며, mixed-precision은 Volta, Turing, Ampere 구조 기반의 GPU가 요구됨](https://github.com/kakaobrain/kogpt?tab=readme-ov-file#hardware-requirements)|
|BERT|[SKTBrain/kobert-base-v1](https://huggingface.co/skt/kobert-base-v1)|❌  다른 라이브러리 설치 및 환경 구축 과정에서 이슈가 있었음. 환경을 구축하긴 했으나 PASS|
|ELECTRA|monologg/koelectra-base-v3-{[discriminator](https://huggingface.co/monologg/koelectra-base-v3-discriminator)/[generator](https://huggingface.co/monologg/koelectra-base-v3-generator)|❌ 효과적인 학습을 위해서는 generator와 discriminator 모두 학습이 필요했고, generator만 학습하는 것은 기존 MLM 학습과 큰 차이가 없는 것으로 판단하여 PASS|
|BigBird|[monologg/kobigbird-bert-base](https://huggingface.co/monologg/kobigbird-bert-base)|❌ Sparse한 Attention 사용으로 토큰 수를 크게 증가시킬 수 있으나, 일부 Outlier를 제외하면 토큰 수가 매우 큰 데이터가 적어서 이득을 얻지 못한다고 판단하여 PASS|
|RoBERTa|[klue/roberta-base](https://huggingface.co/klue/roberta-base)|✅ BERT 관련 모델로는 비교적 SOTA 모델이고 Huggingface에서 쉽게 활용 가능해서 선택함|

## 고려 사항

1. Single-GPU  또는 Multi-GPU로 DataParallel을 활용한 학습을 하여도 학습 시간이 너무 오래 걸린다. 효율적인 학습 방법을 적용하여 학습 시간을 크게 단축시킬 순 없을까?

2. 사용자 데이터의 용량이 너무 크다. 이것을 Resource-efficient하게 처리할 수 없을까?
