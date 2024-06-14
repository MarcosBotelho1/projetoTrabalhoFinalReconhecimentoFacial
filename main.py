import cv2
import numpy as np
import face_recognition
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import os
import pickle

# Lista para armazenar as faces e os nomes
known_face_encodings = []
known_face_names = []

# Pasta para armazenar as imagens e os dados
if not os.path.exists('faces'):
    os.makedirs('faces')

# Arquivos para armazenar encodings e nomes
encodings_file = 'faces/encodings.pkl'
names_file = 'faces/names.pkl'

# Função para salvar encodings e nomes em arquivos
def save_data():
    with open(encodings_file, 'wb') as ef, open(names_file, 'wb') as nf:
        pickle.dump(known_face_encodings, ef)
        pickle.dump(known_face_names, nf)

# Função para carregar encodings e nomes dos arquivos
def load_data():
    global known_face_encodings, known_face_names
    if os.path.exists(encodings_file) and os.path.exists(names_file):
        with open(encodings_file, 'rb') as ef, open(names_file, 'rb') as nf:
            known_face_encodings = pickle.load(ef)
            known_face_names = pickle.load(nf)

# Carregar dados salvos na inicialização
load_data()

# Função para capturar a imagem e identificar o rosto
def capture_image():
    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
        return
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    if not face_encodings:
        messagebox.showinfo("Sem Rosto", "Nenhum rosto foi detectado.")
        return
    
    for face_encoding in face_encodings:
        known_face_encodings.append(face_encoding)
        name = simpledialog.askstring("Identificação", "Digite o nome da pessoa:")
        if name:
            known_face_names.append(name)
            # Salvar a imagem
            cv2.imwrite(f"faces/{name}.jpg", frame)
            messagebox.showinfo("Sucesso", f"Rosto capturado e salvo como {name}.")
            # Salvar dados atualizados
            save_data()
        else:
            messagebox.showinfo("Cancelado", "A identificação foi cancelada.")
    
    # Exibir a imagem capturada
    img = Image.fromarray(rgb_frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

# Função para exibir o feed da câmera
def show_frame():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

# Função para reconhecer rostos conhecidos
def recognize_faces():
    if not known_face_encodings:
        messagebox.showinfo("Sem Dados", "Nenhum rosto conhecido armazenado.")
        return
    
    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
        return
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    if not face_encodings:
        messagebox.showinfo("Sem Rosto", "Nenhum rosto foi detectado.")
        return

    recognized_faces = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        recognized_faces.append(name)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
    
    # Exibir a imagem com os rostos reconhecidos
    img = Image.fromarray(rgb_frame)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    
    if recognized_faces:
        messagebox.showinfo("Reconhecido", f"Rostos reconhecidos: {', '.join(recognized_faces)}")
    else:
        messagebox.showinfo("Sem Reconhecimento", "Nenhum rosto conhecido foi reconhecido.")

# Configurar a câmera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    messagebox.showerror("Erro", "Não foi possível acessar a câmera.")

# Configurar a interface gráfica
root = tk.Tk()
root.title("Reconhecimento Facial")

lmain = tk.Label(root)
lmain.pack()

btn_capture = tk.Button(root, text="Capturar e Identificar Rosto", command=capture_image)
btn_capture.pack()

btn_recognize = tk.Button(root, text="Reconhecer Rostos", command=recognize_faces)
btn_recognize.pack()

show_frame()
root.mainloop()

# Libere a câmera
cap.release()
cv2.destroyAllWindows()