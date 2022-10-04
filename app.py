#________________________________________________________________________________________________________________________
#installing esential requirements
import streamlit as st
import os 
import subprocess
import geocoder
import pandas as pd 
from csv import writer


#________________________________________________________________________________________________________________________
# import keyboard
# st.title('Dawg Detection 🐶')
st.markdown("<h1 style='text-align: center; color: white;'>Dawg Detection 🐶</h1>", unsafe_allow_html=True)

#________________________________________________________________________________________________________________________

#setting up the cofigure button
jury=True
if 'jury' not in st.session_state:
    st.session_state.jury = False

butt=st.button('Configure',disabled=st.session_state.jury,help='Press This And Wait A Few Seconds If You Are Running The Website For The First Time')
if butt==True:
    os.system('git clone https://github.com/WongKinYiu/yolov7')
    # os.system('%cd yolov7')
    # os.system('pip install -r requirements.txt')
    # os.system('pip install -r yolov7/requirements.txt')


#________________________________________________________________________________________________________________________

    #making essential installs using zhc commands 
    os.system('ls')
    os.system('wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt')
    os.system('pip install opencv_python')
    os.system('conda install pytorch torchvision torchaudio -c pytorch -y')
    os.system('pip install pyyaml')
    os.system('pip install scipy')
    st.session_state.jury = True

#________________________________________________________________________________________________________________________

#bob represents the AI command 
bob='python ../yolov7/detect.py --weights ../yolov7.pt --classes 16 --conf 0.25 --img-size 640 --source  ../Images/seesh.png  --exist-ok --save-conf --save-txt'
# tusk='python /yolov7/detect.py --weights /yolov7.pt --classes 16 --conf 0.25 --img-size 640 --source /Images/seesh.png --exist-ok --save-conf --save-txt'

print('')
#________________________________________________________________________________________________________________________

#getting camera input
pic=st.camera_input('Take A Picture')
if pic:
    with open ('Images/seesh.png','wb') as file:
        file.write(pic.getbuffer())
        # os.system('apt-get update')
        # os.system('apt-get install ffmpeg libsm6 libxext6  -y')
        # os.system('pip install opencv-python')

        os.system(bob)#detecting the dogsss
        st.text('Detected Dawgs')
        img=st.image('runs/detect/exp/seesh.png')# showing the detcted image 
        # print('issue1')

#________________________________________________________________________________________________________________________

        #counting the number of dawgs
        f=open("runs/detect/exp/labels/seesh.txt",'r')
        a=f.readlines()
        b=[]
        for j in range(0,len(a)):
            if a[j][0:2] == '16':
                b.append('yass')
            else:
                continue 
        print(len(b))#printing the number of dogs 
        f=open("runs/detect/exp/labels/seesh.txt",'w')
        st.balloons()
        st.success(f'Total Number Of Dogs Detected: {len(b)}')#printing the number of dogs 
        st.markdown("---")

#________________________________________________________________________________________________________________________

        #map
        g = geocoder.ip('me')
        print(g.latlng)#fetching the cords 
        with open('database/cord.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(g.latlng)
            f_object.close()
        df=pd.read_csv('database/cord.csv')
        cum=len(df['lat'])
        st.text(f'Your Location Coordinates: {g.latlng}')
        st.map(df,use_container_width=True,zoom = 4)#plotting the cords in map
        st.markdown(f"<h5 style='color: red;'>Total Number Of Reports Around The World: {cum}<h5>", unsafe_allow_html=True)

#________________________________________________________________________________________________________________________

clicked= st.button('Click Me For Balloons',help='Click here to feel happy 😁')#adding the baroon button 
if clicked==True:
    st.balloons()

#________________________________________________________________________________________________________________________