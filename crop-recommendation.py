import pickle
import streamlit as st

model = pickle.load(open('RandomForest.pkl', 'rb'))

def main():
    st.title('Crop Recommendation System')

    # Input fields
    nitrogen = st.text_input('Nitrogen',placeholder='Enter nitrogen value (0-140)')
    phosphorus = st.text_input('Phosphorous',placeholder='Enter phosphorous value (5-145)')
    potassium = st.text_input('Potassium',placeholder='Enter potassium value (5-205)')
    temperature = st.text_input('Temperature',placeholder='Enter temperature value (8-43)')
    humidity = st.text_input('Humidity',placeholder='Enter humidity value (14-99)')
    ph = st.text_input('Ph Value',placeholder='Enter ph value (3-9)')
    rainfall = st.text_input('Rainfall Value',placeholder='Enter rainfall value (20-298)')

    if st.button('Predict'):
        if 0<=int(nitrogen)<=140 and 5<=int(phosphorus)<=145 and 5<=int(potassium)<=205 and 8<=int(temperature)<=43 and 14<=int(humidity)<=99 and 3<=int(ph)<=9 and 20<=int(rainfall)<=298:
            input_values = [[int(nitrogen), int(phosphorus), int(potassium), float(temperature), float(humidity), float(ph), float(rainfall)]]
            make_prediction = model.predict(input_values)
            output = make_prediction[0]
            st.success('The crop you should harvest is {}'.format(output))

            if output == 'banana':
                st.image('https://www.daysoftheyear.com/cdn-cgi/image/dpr=1%2Cf=auto%2Cfit=cover%2Cheight=675%2Cq=85%2Cwidth=1200/wp-content/uploads/banana-day1-scaled.jpg', caption='Banana', use_column_width=True)
            elif output == 'rice':
                st.image('https://cdn.britannica.com/89/140889-050-EC3F00BF/Ripening-heads-rice-Oryza-sativa.jpg',caption='Rice',use_column_width=True)
            elif output == 'maize':
                st.image('https://myrepublica.nagariknetwork.com/uploads/media/2019/July/Maize-Dependency.jpg',caption='Maize',use_column_widht=True)
            elif output == 'chickpea':
                st.image('https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2022/04/chickpeas_closeup_1296x728_header-1024x575.jpg?w=1155&h=1528',caption='Chickpea',use_column_width=True)
            elif output == 'kidneybeans':
                st.image('https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/kidney-beans-1296x728-feature.jpg?w=1155&h=1528',caption='Kidneybeans',use_column_width=True)
            elif output == 'pigeonpeas':
                st.image('https://gardenerspath.com/wp-content/uploads/2022/02/How-to-Grow-Pigeon-Peas-Feature.jpg',caption='Pigeonpeas',use_column_width=True)
            elif output == 'mothbeans':
                st.image('https://tiimg.tistatic.com/fp/1/006/986/dried-moth-bean-817.jpg',caption='Mothbeans',use_column_width=True)
            elif output == 'mungbean':
                st.image('https://thumbs.dreamstime.com/b/green-bean-mung-beans-wooden-bowl-scoop-isolated-white-background-selective-focus-216833326.jpg',caption='Mungbean',use_column_width=True)
            elif output == 'blackgram':
                st.image('https://upload.wikimedia.org/wikipedia/commons/6/6f/Black_gram.jpg',caption='Blackgram',use_column_width=True)
            elif output == 'lentil':
                st.image('https://upload.wikimedia.org/wikipedia/commons/f/f5/3_types_of_lentil.png',caption='Lentil',use_column_width=True)
            elif output == 'pomegranate':
                st.image('https://cdn.britannica.com/96/201196-050-C0441508/Batch-pomegranate-fruits.jpg',caption='Pomegranate',use_column_widht=True)
            elif output == 'mango':
                st.image('https://www.newbusinessage.com/img/news/20220511014752_1256.750@2x.jpg',caption='Mango',use_column_widht=True)
            elif output == 'grapes':
                st.image('https://urbanbazaar.com.np/wp-content/uploads/2021/05/grapes.jpg',caption='Grapes',use_column_width=True)
            elif output == 'watermelon':
                st.image('https://snaped.fns.usda.gov/sites/default/files/seasonal-produce/2018-05/watermelon.jpg',caption='Watermelon',use_column_width=True)
            elif output == 'muskmelon':
                st.image('https://www.healthifyme.com/blog/wp-content/uploads/2020/04/Muskmelon-cover-1.jpg',caption='Muskmelon',use_column_width=True)
            elif output == 'apple':
                st.image('https://cdn.britannica.com/22/187222-050-07B17FB6/apples-on-a-tree-branch.jpg',caption='Apple',use_column_width=True)
            elif output == 'orange':
                st.imgae('https://assets-api.kathmandupost.com/thumb.php?src=https://assets-cdn.kathmandupost.com/uploads/source/news/2016/others/27112016093148orange.jpg&w=900&height=601',caption='Orange',use_column_width=True)
            elif output =='papaya':
                st.image('https://d2jx2rerrg6sh3.cloudfront.net/image-handler/picture/2018/3/shutterstock_344505437.jpg',caption='Papaya',use_column_width=True)
            elif output == 'coconut':
                st.image('https://i.unu.edu/media/ourworld.unu.edu-en/article/4538/Videobriefs-19.jpg',caption='Coconut',use_column_width=True)
            elif output == 'cotton':
                st.image('https://images.ctfassets.net/3s5io6mnxfqz/4TV7YTCO1DJuMhhn7RD1Ol/b5a6c12340e6529a86bc1b557ed2d8f8/AdobeStock_136921602.jpeg',caption='Cotton',use_column_width=True)
            elif output == 'jute':
                st.image('https://tds-images.thedailystar.net/sites/default/files/feature/images/2021/06/28/jute.jpg',caption='Jute',use_column_width=True)
            else:
                st.image('https://www.tastingtable.com/img/gallery/what-happens-to-your-body-when-you-drink-coffee-before-eating/intro-1651645259.jpg',caption='Coffee',use_column_width=True) 
        
        else:
            st.success("You have entered wrong input ! Please enter correct input again |")
    
if __name__ == '__main__':
    main()
