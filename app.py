import streamlit as st
import BondGraphTools as bgt
st.title("Bond Graph")
st.set_option('deprecation.showPyplotGlobalUse', False)
import SessionState

session_state = SessionState.get(name='', img=None)

text_input = st.text_input(label='Enter System w/ Elements, e.g. "RC"')
if st.button("Submit parameters"): 
	session_state.model = bgt.new(name=text_input)
	st.success(session_state.model)

if st.button("Create"):
	C = bgt.new("C", value=1)
	R = bgt.new("R", value=1)
	zero_law = bgt.new("0")
	
	model_new = session_state.model
	bgt.add(model_new, R, C, zero_law)
	
	bgt.connect(R, zero_law)
	bgt.connect(zero_law, C)
	
	session_state.model = model_new
	
	st.pyplot(bgt.draw(model_new))

#text_input_2 = st.text_input(label='Enter a Source Element, e.g. "Sf"')
#if st.button("Submit sources"):
#	zero_law = bgt.new("0")
#	Sf = bgt.new(text_input_2)
#	model_new = session_state.model
#	print(model_new.components)
#	bgt.add(model_new, Sf)

#	bgt.connect(Sf, zero_law)

#	st.pyplot(bgt.draw(model_new))	
