# Exciting Trends in Machine Learning

|Speaker|TL;DR|
|---|---|
|Jeff Dean (Chief Scientist at Google Research and Google DeepMind)|Google에서 진행한 작업들을 소개|

## Observations
- 지난 수년 간, ML은 컴퓨터로 할 수 있는 것에 대한 기대를 완전히 바꾸어놓음
- 규모 (연산, 데이터, 모델 사이즈) 의 증가는 더 나은 결과를 가져옴
- 필요한 Computation (연산) 과 이를 수행하는 HW는 엄청나게 변화함

## 컴퓨터로 할 수 있는 것이 엄청나게 발전함
- Image Classification (Top-1 Accuracy)
  - Before NN (SIFT+FVs - 50.9%) ➡️ Now (CoAtNet-7 - 90.9%)
- Speech Recognition (Word Error Rate, WER)
  - Jan'16 (DeepSpeech2 - 13.25%) ➡️ Jul'21 (Conformer + Wav2Vec 2.0 + ... - 2.5%)
 
더 많은 연산량 (Computational power) 은 모델의 성능을 대폭 향상시킨다. 딥러닝은 우리가 컴퓨터를 설계하는 방식을 변화시켰다. ML에 최적화된 HW는 효율적이며 세대를 거듭할수록 주된 변화를 만들어왔고, 낮은 비용 (에너지 포함) 으로 거대 모델을 활용하는 것을 가능하게 했다. 딥러닝 모델 학습/추론에 필요한 특수 연산 (Reduced precision and Specific operation) 을 수행하는 Google의 TPU chips and pods를 소개한다.

## 지난 15년 간 언어모델의 발전
* Large-scale N-gram models (07')
  - `Large Langauge Models in Machine Translation, EMNLP 2007`
    - 20조 개 (2T, Trillion) 의 토큰을 학습하여 3000억 개 (300B) 의 n-gram을 갖는 모델을 만듦
    - `Stupid Backoff`라는 스무딩 기법으로 대용량 데이터를 학습할 때의 연산량을 대폭 낮춤
  - **대용량 데이터에 대한 간단한 방법론을 적용하여 매우 효과적인 모델을 개발.**
* Word2Vec (13')
  - `Efficient Estimation of Word Representations in Vector Space, ICLR 2013 Workshop`
  - `Distributed Representations of Words and Phrases and their Compositionality, NeurIPS 2013`
  - **분산 표현 (Distributed representations) 은 매우 유용함**
* Sequence-to-sequence (14')
  - `Sequence to Sequence Learning with Neural Networks, NeurIPS 2014`
  - **입력 시퀀스에 대한 Neural encoder를 사용하여 State를 생성하여 이를 Neural decoder의 State를 초기화하는데 사용. LSTM으로 Scale-up하여 적용.**
* Neural Chatbot (15')
  - `A Neural Conversational Model, ICML 2015 Deep Learning Workshop`
  - **Neural Language Model을 이용하여 효과적인 Multi-turn interaction을 구현. 입력 시퀀스를 Context로 활용하고, 여기서 생성된 State를 활용하여 Reply를 생성함.**
* Transformer model (17')
  - `Attention Is All You Need, NeurIPS 2017`
  - **Single Recurrent Distributed Representation에 State를 담아두지 말자. 대신, 이전 단계에서의 Representation을 모두 저장하여 이를 활용하자. 10~100배 적은 연산을 통해 높은 정확도를 보임.**
* Transformer-based Neural Chatbot (Meena, 20')
  - `Towards a Human-like Open-Domain Chatbot, Arxiv 2020`
  - **대화 형식의 데이터를 대규모로 학습하여 좋은 성능을 보임.**

> 신경망 기반 언어모델의 발전
>> Seq2seq (14'), Transformer (17'), GPT-2 (19': 1.5B), T5 (20': 11B), GPT-3 (20': 175B), Gopher (21': 280B), PaLM (22': 540B), Chinchilla (22': 70B), PaLM-2, GPT-4, Gemini (23')

> 신경망 기반 챗봇
>> A Neural Conversational Model (15'), Meena (20'), ChatGPT (22'), Bard (23')

## Gemini
`Gemini: A Family of Highly Capable Multimodel Models, Arxiv 2023`
- Feb 2023에 프로젝트 시작. 구글 딥마인드 및 구글 리서치 등 협업
- 목적: 세계 최고의 멀티모달 모델을 학습시켜 구글 전반에 걸쳐 이 모델을 활용하자
- 사이즈: Ultra (Largest), Pro (Medium), Nano (Small)
- 학습 방식: `Pathways (MLSys 2022)`
  - 연산의 일부를 물리적 연산 기계 (TPU) 에 유연하게 맵핑할 수 있고, 실행 중인 시스템에 Dynamic하게 리소스를 추가/삭제할 수 있다. 다양한 네트워크 트랜스포트 (Inter-Chip Interconnect, DCN 등) 를 통해 연산을 관리할 수 있다.
  - Failure를 최소화하고 복구 시간을 분 단위에서 초 단위로 최소화했다. 
  
![gemini](https://www.marktechpost.com/wp-content/uploads/2023/12/Screenshot-2023-12-06-at-11.41.53-PM.png)

Chain-of-Thought (CoT)
- `Chain of Thought Prompting Elicits Reasoning in Large Language Models, Arxiv 2022`
- 학습에서만 아니라, 모델에 질문을 하는 방식에서도 발전이 있었다. 작업 과정을 모델에 보여주는 것은 정확도 및 해석 능력에 대한 향상을 가져왔다.

## Trend
- Foundation 모델을 정제하여 도메인 특화 모델로 만듦
  - Med-PaLM: `Towards Expert-Level Medical Question Answering with Large Language Models` 
- 생성형 모델로 실제와 같은 이미지, 비디오, 오디오를 생성
  - Imagen:
    - 텍스트만 입력: `64x64 (=4096)` 이미지로 변환
    - 텍스트 + `64x64` 이미지 입력: `256x256` 이미지로 변환
    - 텍스트 + `256x256` 이미지 입력: `1Kx1K (1024x1024)` 이미지로 변환
  - 모델의 크기가 클 수록 일관된 성능을 보인다.

![imagen](https://api.wandb.ai/files/geekyrakshit/images/projects/37332147/6077a846.png)

- 카메라 및 포토 기능 향상: 인물 사진 모드, 야간 모드, 천체 사진 등
- 모바일 경험을 변화: 라이브 캡션, 번역 기능, TTS (Text-to-speech) 등
- 엔지니어링, 과학, 건강, 지속가능성에서의 영향
  - 날씨, 재료 과학, 의료 이미지/영상   

