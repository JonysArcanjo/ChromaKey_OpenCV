# Chroma key com OpenCV

## Sobre o Projeto

Este projeto utiliza técnicas de visão computacional para manipular e combinar dois vídeos: um vídeo principal e um vídeo de fundo. Ele extrai os pixels do vídeo principal que correspondem a uma faixa específica de cores verdes e os substitui pelos pixels correspondentes do vídeo de fundo. O resultado é exibido em tempo real.


## Estrutura do projeto
- Readme.md
- data
  - fundo_canva.mp4
  - shakira_modnet_com.mp4
- main.py
- requirements.txt

## Bibliotecas Utilizadas

As seguintes bibliotecas são utilizadas neste projeto:
- OpenCV (cv2): Utilizada para processamento de imagem e vídeo.
- Numpy


## Aplicação em PRD

Este projeto de visão computacional pode ser aplicado em várias aplicações, tais como:

1. Videoconferência: Pode ser usado para substituir o fundo de um vídeo principal durante videoconferências, fornecendo um fundo virtual.
2. Realidade Aumentada: Ao substituir a cor verde por objetos ou cenas virtuais, pode melhorar a experiência de realidade aumentada.
3. Efeitos Especiais: Pode ser usado na produção de vídeos para adicionar efeitos especiais ou mesclar várias fontes de vídeo.

## Conclusão

Este projeto demonstra o uso de técnicas de visão computacional para substituir uma faixa específica de cor em um vídeo principal pelos pixels correspondentes de um vídeo de fundo. Ele pode ser estendido e personalizado com base em requisitos e aplicações específicas.

## Licença

Este projeto está licenciado sob a Licença MIT.