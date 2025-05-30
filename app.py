import streamlit as st
import pandas as pd
import altair as alt


st.logo('Chocos logo.png',size='large')
st.title("Breakfast Nutritional Comparison")
st.image('Chocos logo.png')

df1 = pd.read_excel('NutritionalInfo.xlsx')
df2 = pd.read_excel('NutritionalInfo.xlsx',sheet_name='Sheet3')
food_list = ['Idli Sambar (2 idlis + 1 cup sambar + 1 tbsp chutney)',
'Plain Dosa (1 dosa + 1 cup sambar + 1 tbsp chutney)',
'Masala Dosa (1 dosa + 1 cup sambar + 1 tbsp chutney)',
'Poha (1 bowl)',
'Besan Chilla (1 chilla)',
'Moong Dal Chilla (1 chilla)',
'Suji/Rava Upma (1 bowl)',
'Veg Upma (1 plate)',
'Methi Thepla (1 thepla)',
'Puri Bhaji (2 puris + 1 bowl aloo sabzi)',
'Plain Paratha (1 paratha)',
'Aloo Paratha (1 paratha)',
'Gobhi Paratha (1 paratha)',
'Aloo Matar Sandwich (1 sandwich)',
'Tomato Cheese Sandwich (1 sandwich)',
'Omelette (1 omelette)',
'Veg Poha (1 bowl)',
'Egg Bhurji (1 egg bhurji)',
'Rava Dosa (1 dosa + 1 cup sambar + 1 tbsp chutney)',
'Medu Vada (2 vadas + 1 cup sambar + 1 tbsp chutney)']
sel_food = st.selectbox('Choose a breakfast food',food_list)
fil_df1 = df1[(df1.Dish=='Chocos (1 bowl with milk)') | (df1.Dish==sel_food)]
fil_df2 = df2[(df2.Dish=='Chocos (1 bowl with milk)') | (df2.Dish==sel_food)]
st.bar_chart(fil_df1,x='Key Nutrients',y='Value',color="Dish",stack=False)
#st.bar_chart(fil_df1,x='Key Nutrients',y='Value',color=["#f60b45","#0070c0"],stack=False)
st.bar_chart(fil_df2,x='Vitamins & Minerals',y='Value',color="Dish",stack=False)
if st.checkbox ('Show data'):
    pivot_table1 = fil_df1.pivot_table(index='Dish',columns='Key Nutrients',values='Value') 
    st.dataframe(pivot_table1,use_container_width=True)
    pivot_table2 = fil_df2.pivot_table(index='Dish',columns='Vitamins & Minerals',values='Value') 
    st.dataframe(pivot_table2,use_container_width=True,column_config={
        "Calcium (%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Iron (%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Vitamin B1(%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Vitamin B2(%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Vitamin B3(%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Vitamin B6 (%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Vitamin B9 (%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Vitamin C (%RDA)":st.column_config.NumberColumn(format="%.0f%%"),
        "Zinc (%RDA)":st.column_config.NumberColumn(format="%.0f%%")
    })
st.caption("Data was compiled from the Indian Council of Medical Research-National Institute of Nutrition (ICMR-NIN) Indian Food Composition Table (IFCT) 2017 and 2004, covering a total of 528 and 369 raw food items, respectively.")
st.caption("Additionally 144 raw foods were United Kingdom FCT (UKFCT) and 54 raw foods were referenced from the United States Department of Agriculture (USDA) food composition database. Nutrient content per 100g and serving was calculated by summing individual ingredients, primarily using IFCT 2017 and IFCT 2004 data, with supplementary data from the UK FCT (144 ingredients) and USDA food composition database (54 ingredients).")
st.caption("Source: Indian Nutrient Data Bank (INDB)")
