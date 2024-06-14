Reconhecimento Facial com OpenCV e Tkinter
Este projeto é uma aplicação de reconhecimento facial utilizando as bibliotecas OpenCV, face_recognition e Tkinter. Ele permite capturar imagens através da câmera, identificar e salvar rostos, e reconhecer rostos previamente salvos.

Requisitos
Antes de começar, certifique-se de ter os seguintes requisitos instalados:

Python 3.x
OpenCV
face_recognition
Tkinter
Pillow
numpy
Você pode instalar as dependências necessárias usando o seguinte comando:

bash
Copy code
pip install opencv-python face-recognition Pillow numpy
Estrutura do Projeto
O projeto é composto pelos seguintes arquivos e diretórios:

faces/: Pasta onde as imagens capturadas e os dados de reconhecimento são armazenados.
faces/encodings.pkl: Arquivo que armazena os encodings das faces conhecidas.
faces/names.pkl: Arquivo que armazena os nomes das faces conhecidas.
reconhecimento_facial.py: Script principal que executa a aplicação.
Funcionalidades
Capturar e Identificar Rosto: Captura uma imagem da câmera, detecta rostos, permite que o usuário forneça um nome para cada rosto detectado e salva a imagem e os dados de reconhecimento.

Reconhecer Rostos: Captura uma imagem da câmera, detecta e reconhece rostos previamente salvos, e exibe os nomes dos rostos reconhecidos na imagem.

Como Executar
Execute o script principal:

bash
Copy code
python reconhecimento_facial.py
A interface gráfica será aberta, mostrando o feed da câmera.

Para capturar e identificar um rosto:

Clique no botão "Capturar e Identificar Rosto".
Insira o nome da pessoa quando solicitado.
Para reconhecer rostos:

Clique no botão "Reconhecer Rostos".
Uma mensagem será exibida com os nomes dos rostos reconhecidos, se houver.
Observações
Certifique-se de que a câmera está funcionando corretamente e que tem permissão para acessá-la.
O projeto salva os dados de reconhecimento (encodings e nomes) no diretório faces/. Esses dados são carregados automaticamente quando a aplicação é iniciada.
Se nenhum rosto for detectado durante a captura ou reconhecimento, uma mensagem será exibida informando isso.
Licença
Este projeto é de uso livre. Sinta-se à vontade para modificá-lo conforme suas necessidades.
