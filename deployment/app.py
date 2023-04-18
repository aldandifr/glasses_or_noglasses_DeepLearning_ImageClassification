import streamlit as st
import pandas as pd
import joblib

with open('bestpipe_xgboost_m2.pkl', 'rb') as file_1:
  xgboost = joblib.load(file_1)


# Define the app header
st.set_page_config(
    layout="wide"
)
header = st.container()
with header:
    st.image('header.png',width=300)
st.title('Please Give Feedback your satisfaction using this Airlines!')

st.subheader('Bio')

Age = st.slider('How Old Are You ? ',7,85)
st.write('Your Age is : ', Age)

df = pd.DataFrame([[Age]], columns=['Age'])

Type_of_Travel = st.selectbox('What Type Of Travel Are You ?', 
                             ('Personal Travel', 'Business travel'), index=0)
st.write(Type_of_Travel)
df['Type_of_Travel'] = Type_of_Travel

Class = st.selectbox('What Class Are You ?', 
                             ('Eco', 'Business', 'Eco Plus'), index=0)
st.write(Class)
df['Class'] = Class

Flight_Distance = st.slider('How Far Is Your Flight ? ',31,4983)
st.write('Your Flight Distance is : ', Flight_Distance)

df['Flight_Distance'] = Flight_Distance

st.subheader('Please Give Us Your Feedback')

Inflight_wifi_service = st.selectbox('How your satisfaction to our wifi service?', 
                             (0,1,2,3,4,5), index=0)
df['Inflight_wifi_service'] = Inflight_wifi_service

Ease_of_Online_booking = st.selectbox('How your satisfaction to our online booking servie?', 
                             (0,1,2,3,4,5), index=0)
df['Ease_of_Online_booking'] = Ease_of_Online_booking

Food_and_drink = st.selectbox('How your satisfaction to our food and drink?', 
                             (0,1,2,3,4,5), index=0)
df['Food_and_drink'] = Food_and_drink

Online_boarding = st.selectbox('How your satisfaction to our online boarding service?', 
                             (0,1,2,3,4,5), index=0)
df['Online_boarding'] = Online_boarding

Seat_comfort = st.selectbox('How your satisfaction to our seat, is it comfortable?', 
                             (0,1,2,3,4,5), index=0)
df['Seat_comfort'] = Seat_comfort

Inflight_entertainment = st.selectbox('How your satisfaction to our inflight entertainment?', 
                             (0,1,2,3,4,5), index=0)
df['Inflight_entertainment'] = Inflight_entertainment

On_board_service = st.selectbox('How your satisfaction to our On-board service?', 
                             (0,1,2,3,4,5), index=0)
df['On-board_service'] = On_board_service

Leg_room_service = st.selectbox('How your satisfaction to our Leg room service?', 
                             (0,1,2,3,4,5), index=0)
df['Leg_room_service'] = Leg_room_service

Checkin_service = st.selectbox('How your satisfaction to our Check-in service?', 
                             (0,1,2,3,4,5), index=0)
df['Checkin_service'] = Checkin_service

Inflight_service = st.selectbox('How your satisfaction to our Inflight service?', 
                             (0,1,2,3,4,5), index=0)
df['Inflight_service'] = Inflight_service


Cleanliness = st.selectbox('How satisfied are you with the cleanliness of this airline?', 
                             (0,1,2,3,4,5), index=0)
df['Cleanliness'] = Cleanliness

st.subheader('Is your airplane delayed?')
delayed = st.checkbox('Yes')
if delayed:
    Departure_Delay_in_Minutes = st.slider('Departure Delay in Minutes ',0.1, 1592.0)
    st.write('Departure Delayed : ', Departure_Delay_in_Minutes)

    Arrival_Delay_in_Minutes = st.slider('Arrival Delay in Minutes ',0.1, 1592.0)
    st.write('Arrival Delayed : ', Arrival_Delay_in_Minutes)
else :
   Departure_Delay_in_Minutes = 0.0
   Arrival_Delay_in_Minutes = 0.0

df['Departure_Delay_in_Minutes'] = Departure_Delay_in_Minutes
df['Arrival_Delay_in_Minutes'] = Arrival_Delay_in_Minutes


def delay_level(delay_time):
    if delay_time == 0:
        return "no delay"
    elif delay_time <= 13:
        return "little delay"
    elif delay_time <= 15:
        return "delayed"
    else:
        return "very delayed"

df['Departure_Delay_in_Minutes'] = df['Departure_Delay_in_Minutes'].apply(delay_level)
df['Arrival_Delay_in_Minutes'] = df['Arrival_Delay_in_Minutes'].apply(delay_level)

if st.button('You Are ? '):
    st.title('We can conclude that you are :')
    pred_xgboost = xgboost.predict(df)
    predictxgboost = pd.DataFrame(pred_xgboost, columns=['Predict'])
    if predictxgboost['Predict'][0] == 0 :
        st.title('DISATISFIED')
        st.write('Thank you for giving your feedback, we will improve our service even better')
    elif predictxgboost['Predict'][0] == 1 :
        st.title('SATISFIED')
        st.write('Thank you for your feedback')



