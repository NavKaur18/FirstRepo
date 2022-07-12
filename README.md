**#Content-Based-Movie-Recommender-System**

Content Based Recommender System recommends movies similar to the movie given by the user for that movie and also recommend movies based on genre.

Check out the live demo: https://navkaur18-firstrepo-app-sv6vkg.streamlitapp.com/

How to get the API key?

Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

How to run the project?

1.Clone or download this repository to your local machine.
2.Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
3.Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
4.Replace YOUR_API_KEY in both the places (line no. 35) of app.py file and hit save.
5.Open your terminal/command prompt from your project directory and run the file app.py by executing the command python streamlit run app.py.
6.Go to your browser and type http://127.0.0.1:5000/ in the address bar.
7.Hurray! That's it.

Similarity Score :

How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.


![cosine](https://user-images.githubusercontent.com/103022024/178485799-f65d6cf3-e586-43a7-8c04-20f3e6960272.png)

More about Cosine Similarity : Understanding the Math behind Cosine Similarity

