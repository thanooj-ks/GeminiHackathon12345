from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import google.generativeai as genai


# for Audio Video
from pathlib import Path
import hashlib
from vertexai.generative_models import GenerativeModel, Part
from moviepy.editor import *




app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Call Successfull"

# Get Route
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "user_name" : "John",
        "User_email" : "j@abc.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# POST Route
@app.route("/post_and_get_data", methods =["POST"])
def create_user():
    print("Inside POST Executed")
    geminiOutput = geminiMethod()
    data = {"gemini_val": geminiOutput}
    # data = request.get_json()
    print(data)
    print("POST Executed")
    return jsonify(data), 201

####### Gemini Start #######
# method for text
def geminiMethod():
    print ("Inside Gemini")
    # genai.configure(api_key="AIzaSyDSPnAruCOszgDjbWXbvGPqHvTpaxX2YXk")
    genai.configure(api_key="AIzaSyDMPte9Urqo0_tH91cFyBgZh4lFqdW3eQY")
    

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    
    convo = model.start_chat(history=[])

     
    #audioVideo()
    #imageMethod()
    # create a variable for the feedback input from both the above methord > invoke above metheod for the Audio, video and image description and trsanscription > Append it with the text text reviews > pass it as it as the one input to the below query aong with the prompt. 

    convo.send_message("As a market research analyst looking at a particular Al Taza Restuarant, here's how I would approach the task: **Overall Sentiment:** - I would start by calculating the **average star rating** from the customer reviews. - I would categorize the reviews to determine if there are more **positive, negative, or neutral** sentiments. - I would analyze the sentiment over time to identify any trends, such as a recent improvement or decline in customer satisfaction. **Customer Feedback:** - I would identify the most frequently mentioned **keywords or phrases** in the reviews. - For positive feedback, I would look for recurring themes like **product quality, customer service, or value for money**. - For negative feedback, I would note common issues such as **long wait times, product malfunctions, or staff attitude**. - I would also assess how the business is **responding to negative reviews** to gauge their customer service responsiveness. **Comparison:** - I would compare the star ratings and sentiment with **similar businesses in the area** to see how this Shell Retail station stacks up. - I would look for areas where this business **stands out from the competition**, as highlighted in the reviews. **Actionable Insights:** - Based on the review analysis, I would suggest areas for improvement, such as enhancing customer service or addressing product issues. - I would identify opportunities to improve the **customer experience** based on the feedback. - I would consider leveraging the positive aspects mentioned in the reviews for **marketing or branding efforts**. **Additional Considerations:** - I would be on the lookout for **fake reviews**, checking for patterns in language or inconsistencies. - I would consider the **volume of reviews** to ensure a comprehensive analysis. - I would prioritize **recent reviews** to reflect the current state of the business. Please provide the customer reviews so I can conduct a detailed analysis and offer more specific insights and suggestions. Find the reviews below - The shawarma here is one of the best that I had. The fries even were surprisingly good. The combo with mayyonise has a delightful taste. Tried the al taza special shawarma, full meat shawarma,plate shawarma and falafel. There are lavish seating facilities. The rates are slightly on the higher side. Also tried the Alphonso mango kombucha,which had a unique taste. First time visiting any of the Al taza restaurants. This is the central kitchen I think, Good parking space and good and spacious ambiance. We had different kinds of shawarmas All were good in taste. I had a plate of shawarma from al taza, it's tasty no doubt, but it's not worth that price. You can go for al taza spcl shwarma instead of plate shawarma. Pickle is very sour🥲 it's not good as their stadium branch Al-Taza: Hands Down, One of Kochi's Top Shawarma Spots If you're a shawarma fanatic in Kochi, then Al-Taza is an absolute must-try. Tucked away near Kaloor Stadium, this place consistently delivers some of the most satisfying and flavorful shawarmas I've ever had. The chicken is always perfectly marinated and cooked to tender perfection. They carve generous portions right off the spit, ensuring every bite is juicy and packed with that classic Middle Eastern spice blend. The bread is soft, the garlic sauce is on point, and the pickled vegetables add a delightful tanginess that cuts through the richness. I always go for the plate shawarma if I'm feeling extra hungry – it's a mountain of deliciousness! But their regular rolls are just as satisfying. The service is friendly, the prices are reasonable, and the atmosphere is unpretentious – basically, just perfect for a satisfying shawarma experience. Honestly, Al-Taza is a contender for the title of the best shawarma in all of Kochi. Tips: Get there early in the evening, as it can get crowded later. Highly recommend Al-Taza for any shawarma lover visiting Kochi! Awesome Shawarma point with quality and tasty foods. Tried: 1. Plate shawarma max … Food quality is great. One of the best shawarmas available in kochi. I would personally prefer dine out or takeaway rather than ordering in since there's a decent price difference online and offline. Great service overall. I recently tried the shawarma from Altaza in Edappally. While the flavor of the shawarma was commendable, I was disappointed with the overplacement of rumali roti in the plate, affecting the overall balance. Additionally, the Watermelon juice fell short of expectations due to an unexpected taste difference. Overall, the shawarma experience had its ups and downs, with room for improvement. Bought a Special Shawarma from here yesterday evening 9:00pm. It was the driest most tasteless shawarma I’ve ever had in my life. No sauses or mayonise inside it. Extremely disappointed and I suggest anyone reading this to not to visit there. Instead visit Haji Ali. We don’t mind Al - Thaza trying to manipulate Haji Ali’s shawarma customers but at least try to make a 3-10 shawarma. Extremely disappointed about this. Never visit this shop. By the way It is the second time im having this experience. Also on top of that they wont give ketchup for this dry paper like shawarma.200₹ gone. In my personal opinion, the Altaza Special Chicken Shavarma Roll is the best shavarma I've ever had. The Fries were really good and have great quality. I'll recommend this place to anyone who loves shavarma. Food is very tasty. Good ambience. And quick service. Had: Shawarma (Roll and Plate) and Shawarma Pizza. Shawarma is the best. Shawarma Pizza Crust was a bit hard. Still 5 Star. Will visit again. Dining here was a delightful experience, particularly for shawarma enthusiasts. The exclusive focus on perfecting this signature dish shines through in every aspect, from the quality of the meat to the delectable sauces. The ambiance adds an extra layer of charm to the dining experience, making it a place worth revisiting. Brilliant... not the usual shawarma with lods of cabbage. This was all meat! The mojitos are a perfect pair. Highly recommended! The shawarma here is good. The price range is affordable. They have some varieties of Shawarma and their french fries and their mayonnaise is tasty. Al Taza Edappilly exceeded my expectations with their flavorful shawarma. Highly recommended for shawarma enthusiasts! Al taza is my all time fav shawarma destination in Kerala. I ordered their infamous chicken plate shawarma and passion fruit mojito to wash it down. I really really loved the crispiness of the chicken and the quantity is worth the price. The ambience is really spot on without much disturbance from outside commotion. Shawarma was exceptionally good, may be the best i had till date Located within the petrol pump, and it doesn’t offer a great ambience, but definitely a must go spot for shawarma lovers. Staffs are also very welcoming and both chicken and beef shawarma are available along with some combos like rice. The prices are on higher side but its worth every penny. Tried this famous Al-Taza shwarma and it is one of the best shawarma shops. Tried their special shawarma and it was really nice. As it is a shwarma outlet, they have a limited menu but the shawarma brings you the joy. Really tasty and worthy. The outlet was very clean and nice. The service was also good. They have a good seating and a amble car parking space. They also have various juices along with the shawarma. Must try spot in kochi. Located near indian oil petrol station. One of the best shawarma shops. Good service and good-quality food. We tried their special shawarma, and it was good. The dine-in facility was a nice and very neat place. Along with shawarma, we tried a green apple mojito, which was also good. I would recommend this for shawarma lovers. We tried the taza special, which was too good as compared to other shawarma in town. They got spacious seating area and car parking. Must try This place is located just close to the petrol pump.Even in this location,they have a plenty of dining space and customer service is also good. The full meat beef shawarma I tried had good content and was well cooked.I really liked their presentation.Nice place to come with family and friends. But I heard this place is a must try shawarma joint in town, but it didn't meet my expectations.(maybe it was because I tried the full meat shawarma or I don't know🤷‍♂️) Overall I had an average experience✌🏻 Even in this hectic location, they have plenty of dinning space, and if you have once had their Shawarma you know the taste , and I've been eating several times now and I became a fan of their beef whole meat Shawarma. However we feel like less quantity if you order the plate Shawarma. And to be honest the real taste can be felt in the roll Shawarma not in plate Shawarma because the filling. In plate Shawarma we get meat Mayo and all other things seperately and it's hard to get the real taste so I suggest their roll Shawarma . And as you can see you will have parking space inside the fuel station which something I have never seen here in Kochi. A business inside a very busy Fuel station. Disappointing Experience Today, [11/04/24], my family and I visited Restaurant for a casual dinner. Unfortunately, our experience was far from enjoyable. Upon arrival, we were informed of a wait time despite several vacant tables. After some time, we were offered a shared table, which we accepted. However, no server approached us for at least 10 minutes. After requesting service, it took another 25 minutes to receive a single plate and a single roll. We then ordered a lime drink, but after waiting another 10 minutes with no sign of it, we decided to cancel and request the bill. Here's where things went downhill. At the counter, the staff member who initially greeted us became confrontational. He loudly questioned the what delay in front of other patrons and my family. To avoid escalating the situation, I simply suggested reviewing the camera footage to verify the wait times. We then left without further conversation. While I understand restaurants can get busy, the lack of communication and the staff member's aggressive behavior were unacceptable. Service industry staff should be trained in basic courtesy and conflict resolution. It's important for customers to feel welcome and respected, not like beggars. Overall, this experience left us feeling frustrated and disrespected. Unfortunately, we cannot recommend to others. Quantity very less , 250+ rate , Only veggies 75% Not recommended Located across Lulu in the Indian Oli Pump premises. Sufficient parking space if you wish to dine in. A drive through counter is available if you wish to pack. This place is for you if you are a shawarma afficionado. Reasonably priced. … One of the best shawarma spot in our home town .Maintaining their standard in food preparation and quality. Must try spot in Ernakulam Had a very bad experience! We ordered diet shawarma after enquiring on the quantity, the boy who took order confirmed that there will enough quantity of meat, but later when we got our food, the quantity was too less and the item is … This place is simply overrated. The taste and quantity of the food are not up to the mark👎. I ordered a Plate Shawarma 🍗for 237/- Rs, including GST, but it was not worth the money. The Shawarma plate includes 2 large rumali rotis, but the … Visited last night. The shawarma we had was good. The food was really yummy. Ingredients were fresh and the Mayo was top notch but the menu could've been a bit elaborate. Shawarma is tasty , but if you want to feel it all, have it hot. Cuz, many a time when we order a take-out and have it cold, the real taste is lost and felt bland ! … I really don’t know why this place is worth so much hype. They have limited menu and food was ok. Whole meet shawarma was good and chefs special shawarma was not that great. Washroom is so untidy and overall cleanliness of the restaurant is not acceptable from a brand which has many outlets across Kerala. I came here for the Doner Kabab, cause you won't get that in the Kaloor outlet. So I got the Beef Doner Kabab Burger. It was really good, that was obvious. But the quantity wasn't enough. It didn't fill me. So overall it's not worth the … I've had so many shawarma's from different places before but this is the best ever I had so far. SO DAMN DELICIOUS!!! 😋. Must try the Al-Taza Special Chicken Shawarma, it's the best. It has a combination of mayonnaise and cheese(heavenly … I had one AL- taza special shawarma 195/- and one normal shawarma 121/- chicken. … Chicken and beef doner kebab, beef burger Beef doner might have been the most authentic of the three dishes, neutral … Al Taza is one of the best shawarma serving place in kochi. It was my first time visiting the Edapally outlet. The outlet has one parcel counter were you can park the vehicle and go for dining which is around 50 metres away from parcel … Aa you all know there is no compromise in taste or quality of food.The shawarma was great , absolutely tasty.The shop was near to a petrol pump you have to climb the stairs. So we ordered an Al Taza special shawarma which is known for it's … As a Shawarma lover this place was on my list for a long time and this place delivered. … Costly but tasty, size could have been better Delicious food. Their Shawarma is best in town. Location is easily accessible. Located inside Indian Oil Petrol Pump, Edapally opp to Lulu Mall. Restaurant is on first floor. … The food quality is really good and very fresh , the freshness of chicken is outstanding but the service is poor and the food is not served hot which effect the taste for me , the juice are overpriced and don’t recommend mojitos they are … The best shawarma i ever had.. Its LIT 🔥 Personally i felt lyk the normal chicken shawarma is better compared to the special shwarma. … Had their new Altaza Jumbo Shawarma. It is a larger version of their Special Chicken Shawarma and the portion size was perfect! Tasty food with great ambience and service. Prices are at an above average level for an Arab food place but justified for the taste and service. One thing to improve is that normal water could be provided instead of mineral water Popular place for Shawarmas🌯. Tried their Al Taza Special Chicken & Beef Shawarmas. Tasted really good. Infact one of the best Shawarmas I ever had. 😋 … Spacious ambiance and very quick service..I wanted to convey my appreciation for the excellent service I received from Mr.Nirmal. One of the best places to get shawarmas in Kochi. They quality of the food they serve is a must say. They have a good dining space too. This place is located in a petrol Pump in edappally. And has parking space available too. The server very tasty shawarmas. Have sufficient parking also. Edit:- i really disappointed during my last visit. We have ordered normal chicken shawarma and beef shawarma first of all they reduced quality and increased price for their shawarma rolls. Now I feel it doesn't worth for the money. And the … I visited your establishment, Al Taza, located opposite Lulu Mall in Ernakulam on 13th February 2024, at approximately 3:30 p.m. and was appalled by the abysmal customer service I encountered. Upon arrival in my scooter, I adhered to the … went from being one of the go to shawarma joints to not to cus of the food I really love the their Club Sandwich, The time onwards when I came to Kochi, I would have ordered at least 50+ time for the same, they will give you suggestions too, for how much hungry you would feeling. It's really good for Dine-in and as Take away too We had beef shawarma which was good in taste, but the quantity was less than before and the waiting time is too high for the delivery. Since dining in is not allowed we need to get the parcel, but their one room is open and who really wants to have a seat to have food can utilise it. Had Al-taza plate shawarma. It's good in taste and well served. The Shawarma they make is really awesome.the View from the top is also super cool. … It was excellent Actually service man Nirmal was so good and kind hearted person,he helped us more, … One of the best shawarma places in Cochin so far... We had ordered 3 full meat chicken shawarma, 1 altaza special chicken shawarma roll, 1 chicken plate shawarma and 1 chicken burger shawarma. … Situated right beside the fuel pump! The altaza special shawarmas were excellent! They are open till 12! While the shawarmas were excellent the club sandwich was just shawarma fillings instead of patty/nuggets so not recommended Good seating space and good service, tried their Jumbo Shawarma, it was good and good quantity. Only issue is the parking space. Tried a Grape Juice and I loved that. We had two whole meeat shawarma roll and one mint lime. Whole meat shawarma was superb. But the mint lime was sugar water. One of the best shawarma joints in town. Great sauce, great filling. Also tried the shawarma burger. It's great at first but it gets tiring and it was kinda hard to finish alone. But still must try atleast once. The location is in edapally nearby Indian oil petrol pump. The dining space was spacious and good ambience as we took the top floor the place was neat and tidy. We ordered their al taza special shawarmas and a passion fruit mojito the taste … I ordered normal shawarma and the taste was good. Not a big fan of porotta shawarma. I personally feel sad giving 1 star now bcoz Al Taza is the only place from where I get shawarma and it's my all time favourite but recently they got my order wrong. I ordered a falafel shawarma but the shawarma came without falafel inside and just mayo and veggies... ☹️ It's just fine. Many of my friends told me that Al Taza offers one of the best shawarmas in Ernakulam, but this one did not impress me. We went there at 9 PM and we wanted to have the Al Taza special Beef Shawarma, but apparently it was … I’ve been having shawarmas from the very beginning and the taste has been consistent all through out. Easily one of the best shawarma places in kochi. Haven’t had the chance to try the new items in menu but I guess they are pretty good as well. The food at Al Taza restaurant is delicious, and the atmosphere is really nice too. The service was also top-notch. Overall, I had a fantastic dining experience there! 👍 … Shawarma which i ate at Al Taza was good and shawarma served here is in Romani Rotti. Nice place to hangout with friends. Surprisingly they have setup a dine in spot near to the outlet. And the place is nice and ambient. They serve … Burger Shawarma is a must try ! Club sandwich 🥪 too ! AlTaza Plate Shawarma Max 🔥 … The plates in which shawarma roll served is very inconvenient. I am aware that this plate is AlTaza’s brand identity however it is difficult for customers. Really nice food. In my opinion it's better to go for the roll Shaverva rather than plate shavarma. Because in plate shavarama we have to assemble like fries meat etc and the cost is high too. So prefer plate shavarma only if you are extremely hungry Good shawarma, parking inside indian oil pumb , the hotel is on the first floor , we can give car for wash if needed since there is shop near , the hotel have good space and clean , staff deliver parcel in cars Very tasty shawarma you can get from here. Also many varieties of other shawarma things are also found here. They serve with less waiting time. The only problem i found is for parking the vehicle..the area is a little congested. This the one of the best place in ernakulam for shawarma. They give a very decent quantity and extremely spicy shawarma. Personally I love al taza more than other shavarma shop only because al taza shwarma is really really spicy. They also … Never believe in hype. Touted as the best shawarma in kochi, i gave this restaurant chain a try and a simple shwarma roll itself made me realise its not even close to shawarmas we can get in kannur or north malabar. The chopped vegetables were bland no masala in the meat, no flavour, no tinge , the bread is the only saving grace. I would have given 5 stars but the waiters will leave you unattended minimum for 15 min without taking order. Food is good and fresh. Tried Donor Kebab(Beef). Meat veggies jalapeños and mayonnaise inside pitta bread. Tastes good. They also have chicken option but using the same shawarma chicken. Beef costs 230/- and 210/- for chicken. Feels bit overpriced. Eventhough Al-Taza shawarma is my personal favorite. Shawarma burger & iskender kebab with pita bread was very tasty 😋 and heavy , Doner kebab beef was tastier than chicken.. … Delicious shawarma very tasty falafel ambience superb neat and clean affordable prices shawarma and falafel,burger ( juices, shake's price too high) ഞങ്ങൾ പോയപ്പോ കഴിച്ചത് ഫുൾ മീറ്റ് ചിക്കൻ ശവർമയും ഫലഫിൽ റോളും ആണ് കഴിച്ചത് നല്ല കിടു ഐറ്റം … If you are going with Less expectations you may like it. Because I don't see any wow factor in that shawarma. Infact i liked fries more than shawarma. This may be totally my personal choice. … Al taza is famous for its shawarma This time i tried iskinder beef Kebab with pita bread , loved the taste you can try once . Their shawarma rolls are good. My personal favorite is their Altaza special beef shawarma roll. Seems like quantity of plate shawarma reduced. Mint lime was good. Service was decent. Great service and good food. Al Taza special shawarma and Falafel roll is a must try. The restaurant is highly economical. As usual, the best shawarma in kerala. Tried all meet beef this time. This is a must try !! I used to visit any of the Al-Taza branch near me when I plan a kochin trip. (Bang opposite to lulu mall main entrance.) Best place for best-selling shawarmas in Kochi. If you love shawarma, please try Al Taza. This place was good. But now overpriced and good for nothing. The food is below average and lacks tastes.long waiting time. We ordered al taza special(195₹), diet shawrma plate (255₹)and plate shawarma(240₹).The price is not justifiable. As usual No words for Al-Taza newly opened at kochi Salem High way Petrol pump or opposite to Lulu mall in NH47 … Al Taza doesn't require a introduction about the yummy and one of the best shawarmas in town which they serve. This outlet is in Indian Oil Petrol pump at edapally. They have take out counter as well as dine in place for customers the taste … Good Hospitality, Very neat serving, Shawarma 7/10 is just okay. … Al Taza anyway it's made its reputation, it's a good Shawarma, no doubt. And it's same here too. One should not expect much of hospitality or Ambience, just satisfy your taste buds and leave. Not much expensive, enough space to park your car, in the middle of the city. Easy to access. Quality remains consistent across all outlets. The quantity to quantity ratio leaves something to be desired though. I do wish the roll was a little larger. But have to give them kudos for maintaining a very clean kitchen. You can see … It was my first time at Al Taza and I had plate shawarma and fresh lime parcel.....quality,taste ,quantity,presentation and packing of food was superb.....even the customer service was soo good.Loved it ❤️ Average sized shawarma. Not too large nor too small. It's not the same kind available in GCC. Contains mayonnaise instead of the regular shawarma sauce. Taste has deteriorated from initial times Portion size of plate shawarma was horrible (single layer of meat was there ) As this is famous shawarma spot in kochi I also loved their shawarma. I liked their special shawarma very much since it was cheesy. Their drinks was average Good restaurant only waited 30 mins for hot water The best shawarma you can get, consistently. My favourite is their full meat chicken shawarma. A bit high priced but quality is worth.One time try.Shawarma burger is the one i would like to suggest. Friendly service and great taste. Heard a lot about altaza and i would say its just the hype. I dont think they have the best shawarma. The shawarma is just average. I dont know why these people are crazy about altaza. The quantity of chicken in the Shawarma is less as well … Their shawarma is awesome Try it. Now they opened calicut also.same taste same rush. If we talk about their taste,it is like Good and different experience on … One of the best shawarmas I have ever had One of the best falafel wraps available in kochi. Although, I was hoping for more of an authentic experience since Mayo is used instead of Hummus and mirchi. Anyhow, I'd go back for it when I'm in Kochi.")
    print(convo.last.text)



    return convo.last.text
    print ("Gemini Executed")


# method for Audio and Video Analysis
def audioVideo():
    print ("inside video")
    video_file_uri = "example.mp4"
    video = VideoFileClip(video_file_uri)

    video.audio.write_audiofile("example.mp3")
    genai.configure(api_key="AIzaSyDSPnAruCOszgDjbWXbvGPqHvTpaxX2YXk")

    your_file = genai.upload_file(path="./example.mp3")

    prompt = "Listen carefully to the following audio file. Provide a brief summary."
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content([prompt, your_file])

    # Set up the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 0,
      "max_output_tokens": 8192,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

 
    convo = model.start_chat(history=[])
    
    promt2 = "Hi there, you are going to act like a market research analyst who is looking at a particular product. The task for you is to analyze the customer reviews and suggest ways to improve the product. Overall Sentiment: What is the average star rating? Are there more positive, negative, or neutral reviews? Are there any trends in sentiment over time (e.g., recent improvement or decline)? Customer Feedback: What are the most frequently mentioned keywords or phrases? Are there recurring themes in the positive reviews (e.g., product quality, customer service, value for money)? Are there recurring themes in the negative reviews (e.g., long wait times, product malfunctions, staff attitude)? How is the business responding to negative reviews? Comparison: How do the star ratings and sentiment compare to similar businesses in the area? Are there any areas where this business stands out from the competition (according to the reviews)? Actionable Insights: Based on the reviews, what are some areas where the business could improve? Are there any opportunities to improve customer experience based on the feedback? Can the positive aspects highlighted in the reviews be leveraged in marketing or branding efforts? Additional Considerations: Be mindful of fake reviews. Look for patterns in language or inconsistencies that might indicate inauthentic reviews. Consider the volume of reviews. A small number of reviews may not provide a complete picture. Look for reviews from recent customers, as business practices may have changed over time. Giving you the trascrible of the feedback audio recording here -"
    feedback = response.text
    convo.send_message(promt2 + feedback)
    print(convo.last.text)


# method for Audio and Video Analysis
def imageMethod():
    print("inside image")
    genai.configure(api_key="AIzaSyDSPnAruCOszgDjbWXbvGPqHvTpaxX2YXk")

    prompt = "Act like a quality assurance professional, responsible for the final checks on the quality of product. Could you please have a check on the product and share your review. you can also get the help of the text, if available with the image"
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content([prompt, './spects1.PNG'])
    print(response.text)


####### Gemini End #########



if __name__ == "__main__":
    app.run(debug=True)