import streamlit as st
import requests
import json

from uritemplate import variables

st.title("Ticket Classification App")

TicketSubject  = st.text_input("Enter the subject of your ticket:")

	
if st.button("Submit"):
	url = "http://127.0.0.1:8000/predict"
	response = requests.post(url=url, json={"subject": TicketSubject})
	output_dict = json.loads(response.text)
	st.write(output_dict['message' \
	''])