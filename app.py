import streamlit as st
import itertools as it
st.title("This is a test survey form")


with open("style1.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


list1 = []
first_name = ""
last_name = ""
dob = ""
gender = ""
address = ""
city = ""
country = ""
zip_code = ""
          
# def func_list():
#         list2 = []
#         list2.append(first_name)
#         list2.append(last_name)
#         list2.append(dob)
#         list2.append(gender)    
#         list2.append(address)
#         list2.append(city)
#         list2.append(zip_code)
#         for item in list2:
#             print(item)

# def req_field():
#     st.error("This field is required")



tab1,tab2,tab3= st.tabs(["Your Basic Information", "Additional Information", "Photo Verification"])
current_tab = 0
# def display_tab(tab):
#     if tab1 == 'Your Basic Information':
#         st.write(" ")
#     elif tab2 == 'Additional Information':
#         st.write(" ")
#     elif tab == 'Photo Verification':
#         st.write(' ')
# display_tab(tabs[current_tab])
with tab1:
    first_name = st.text_input("First Name", key = "first_name")
    last_name = st.text_input("Last Name", key= "last_name")
    age = st.number_input("Age", min_value=0, key = "age")
    gender = st.selectbox("Gender", ("Male", "Female", "Rather not say"))
    button_next_tab1 = st.button("Next", on_click=tab2, key ="next_tab1")
    # if button_next_tab1:
    #     current_tab+=1
    #     if current_tab== len(tabs):
    #         current_tab = 0
    #     display_tab(tabs[current_tab])   
        
with tab2:    

    address = st.text_input("Address")
    city = st.text_input("City")
    country = st.selectbox("State",["United States", "Canada", "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and/or Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecudaor", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kosovo", "Kuwait", "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfork Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbarn and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States minor outlying islands", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam", "Virigan Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe"])
    zip_code = st.text_input("ZIP Code")
    button_back_tab2 = st.button("Back", on_click=tab1, key ="back_tab1")
    button_next_tab2 = st.button("Next", on_click=tab3, key = "next_tab2", kwargs="next_tab2")
    
    st.markdown('''
        <style>
        .stButton > .edgvbvh10 {float: right;}
  

        ''', unsafe_allow_html=True)

with tab3:    

    st.subheader("Please Upload your file")
    file_uploader = st.file_uploader("File Uploader")
    button_back_tab3 = st.button("Back", on_click=tab2, key="back_tab3")  
    submitted = st.button("Submit",)
    

if submitted:
    if not first_name:
        st.error("Please enter your first name!")
    elif not last_name:
        st.error("Please enter your last name!")
    elif not age:
        st.error("Please enter your age!")
    elif not gender:
        st.error("Please enter your gender!")
    elif not address:
        st.error("Please enter your address!")
    elif not city:
        st.error("Please enter your city!")
    elif not country:
        st.error("Please enter your country!")
    elif not zip_code:
        st.error("Please enter your ZIP code!")
    elif not file_uploader:
        st.error("Please upload your documents!")
    else:
        list1.append({
            "first_name": first_name,
            "last_name":  last_name,
            "age":  age,
            "gender": gender,
            "address": address,
            "city": city,
            "country": country,
            "zip_code": zip_code,
        })
    st.success("Thank your for submitting the form!")
    st.write("Your responses", list1)
    
with open("results.txt", "w") as file1:
    file1.write("\n". join(str(item) for item in list1))









