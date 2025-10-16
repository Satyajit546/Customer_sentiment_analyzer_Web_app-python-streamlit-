import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px

st.title("Sentiment Analysis Web Platform")
choice=st.sidebar.selectbox("My Menu",("Home","Analysis","Visualization"))
if(choice=="Home"):
   
    st.image("https://miro.medium.com/v2/resize:fit:1400/0*tkL20Gt31dYYigyV")
    st.markdown(
    """
    <div style='text-align: center; background-color: #E6F3FF; padding: 10px; border-radius: 10px;'>
        <h1 style='color: #007BFF;'>Welcome Home! 🎉</h1>
        <p style='font-size: 20px; color: #333;'>Check Your Feedback and Dive into the Analysis.</p>
    </div>
    """,
    unsafe_allow_html=True
)
elif(choice=="Analysis"):
    st.write("This Is Your Analysis & Check Your Results")
    st.image("https://editor.analyticsvidhya.com/uploads/61727sentiment-fig-1-689.jpeg")
    url=st.text_input("Enter your Google Sheet URL")
    cn=st.text_input("Enter Your column Name To Be Analyzed")
    btn=st.button("Analyze")
    if btn:
       df=pd.read_csv(url)
       x= df[cn]
       mymodel= SentimentIntensityAnalyzer()
       l=[]

       for k in x:
          pred=mymodel.polarity_scores(k)
          if(pred['compound']>0.01):
             l.append("Positive")
          elif(pred["compound"]<-0.01):
               l.append("Negative")
          else:
               l.append("Neutral")

       df["Sentiment"]=l

       df.to_csv("results.csv",index=False)
 
       st.write("Analysis Successfull & Check Your Shocking Results")
elif(choice=="Visualization"):
     st.image("https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/202/619/datas/original.gif")
     st.write("This Is your Final Destination")
     df=pd.read_csv("results.csv")
     choice2=st.selectbox("Choose Your Visualiztion Charts",("None","Table","Pie","Histogram"))
     if(choice2=="Table"):
        st.subheader("Full Analyzed Data Table")
        st.dataframe(df)
     elif(choice2=="Pie"):
         posper=(len(df[df['Sentiment']=="Positive"])/len(df))*100
         negper=(len(df[df['Sentiment']=="Negative"])/len(df))*100
         neuper=(len(df[df['Sentiment']=="Neutral"])/len(df))*100
         fig=px.pie(values=[posper,negper,neuper],names=['Positive','Negative','Neutral'])
         st.plotly_chart(fig)


     elif(choice2=="Histogram"):
         c=st.selectbox("Choose Column",df.columns)
         fig=px.histogram(x=df[c],color=df["Sentiment"])
         st.plotly_chart(fig)
