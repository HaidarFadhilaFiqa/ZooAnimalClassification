import streamlit as st
import streamlit.components.v1 as stc 
from PIL import Image
import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier

st.write("""
# Zoo Animal Classification

This app predicts the type of Animal

Data obtained from the [Zoo Animal UCI Machine Learning](https://archive.ics.uci.edu/dataset/111/zoo)
""")

# Load the pickled model
model = pickle.load(open('model_decision_tree1.pkl','rb'))

def ipm_predict(input_data):
    # Membuat dictionary konversi nilai string ke numerik
    label_to_numeric = {
        'Iya': 1,
        'Tidak': 0
    }

    # Mengonversi nilai string ke numerik
    input_data_numeric = [label_to_numeric.get(value, value) for value in input_data]
    id_np_array = np.asarray(input_data_numeric)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = model.predict(id_reshaped)
    
    if prediction[0] == 1:
        return "Hasil: Mamalia"
    elif prediction[0] == 2:
        return "Hasil: Burung"
    elif prediction[0] == 3:
        return "Hasil: Reptil"
    elif prediction[0] == 4:
        return "Hasil: Ikan"
    elif prediction[0] == 5:
        return "Hasil: Amfibi"
    elif prediction[0] == 6:
        return "Hasil: Serangga"
    elif prediction[0] == 7:
        return "Hasil: Invertebrata"
    else:
        return "Hasil: Tidak Diketahui"

def main():
    # ...

    Rambut = st.sidebar.selectbox('Berambut',('Iya', 'Tidak'))
    Bulu = st.sidebar.selectbox('Berbulu',('Iya', 'Tidak'))
    Bertelur = st.sidebar.selectbox('Bertelur',('Iya', 'Tidak'))
    Susu = st.sidebar.selectbox('Menyusui',('Iya', 'Tidak'))
    Terbang = st.sidebar.selectbox('Dapat Terbang',('Iya', 'Tidak'))
    Berenang = st.sidebar.selectbox('Dapat Berenang',('Iya', 'Tidak'))
    Predator = st.sidebar.selectbox('Predator',('Iya', 'Tidak'))
    Gigi = st.sidebar.selectbox('Memiliki Gigi',('Iya', 'Tidak'))
    Tulang_belakang = st.sidebar.selectbox('Tulang Belakang',('Iya', 'Tidak'))
    Bernafas = st.sidebar.selectbox('Bernafas',('Iya', 'Tidak'))
    Berbisa = st.sidebar.selectbox('Berbisa',('Iya', 'Tidak'))
    Sirip = st.sidebar.selectbox('Sirip',('Iya', 'Tidak'))
    Kaki = st.sidebar.selectbox('Jumlah Kaki',(0, 2, 4, 6, 8))
    Ekor = st.sidebar.selectbox('Ekor',('Iya', 'Tidak'))
    Domestik = st.sidebar.selectbox('Domestik',('Iya', 'Tidak'))
    Catsize = st.sidebar.selectbox('Catsize',('Iya', 'Tidak'))

    prediksi = ''
    
    if st.button('PREDICT'):
        prediksi = ipm_predict([Rambut,
                                Bulu,
                                Bertelur,
                                Susu,
                                Terbang,
                                Berenang,
                                Predator,
                                Gigi,
                                Tulang_belakang,
                                Bernafas,
                                Berbisa,
                                Sirip,
                                Kaki,
                                Ekor,
                                Domestik,
                                Catsize])
        
    st.success(prediksi)
    
if __name__=='__main__':
    main()