# AITA_data_exploration_and_ML

This project is a series of Jupyter notebooks.

In our previous project, we fetched thousands of posts and comments from Reddit. 
https://github.com/Nico404/scrap_reddit

We're now deep diving into the data to actually build our Text Classifier and hopefully be able to categorize a post from the AITA subreddit.

## Table of content
- [AITA_data_exploration](AITA_data_exploration.ipynb): This notebook contains a brief exploration and statistical analysis of the data we fetched.
- [ML_models](ML_models.ipynb): This notebook contains our first try at feeding our data to a Zero-Shot text classifier without any context and comparing performance over different parameters.
- [Data_Labeling_for_Model_Autotraing](Data_Labeling_for_Model_Autotraing.ipynb): This notebook contains our first model AutoTraining on our data with good performance.

[Training Dataset](data/AITA_labeled_posts.csv) 
<table>
  <thead>
    <tr>
      <th>post_id (string)</th>
      <th>post_content (string)</th>
      <th>post_title (string)</th>
      <th>verdict (string)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10uxee0</td>
      <td>"I know this post sounds super petty, but this is the most ridiculous fight I've had with my boyfriend, and unfortunately it's where we're at ... We're at an impasse but I wonder if I *am* being a little too petty about the whole thing."</td>
      <td>AITA for telling my boyfriend I'll shave my legs if he shaves his?</td>
      <td>NTA</td>
    </tr>
    <tr>
      <td>10ur722</td>
      <td>"My daughter Bryn F9 is going on a trip to a nearby water park with her class next week. She loves water and has been talking about it for months, so I was a bit thrown off ... Is my husband right? Or am I justified?"</td>
      <td>AITA for pulling my daughter from a waterpark trip because her teacher made her stay with a kid she doesn't like?</td>
      <td>NTA</td>
    </tr>
    <tr>
      <td>10upxdd</td>
      <td>"Alright so my son (17) has weekly therapy appointments that I take him to. Unfortunately, my husband let our daughter borrow his car and then had an emergency at work so he had to use my car so my son and I had to take the bus... AITA? A totally unrelated woman thought I was along with the two.I wasn’t sitting down and did not have a seat."</td>
      <td>AITA for not letting an elderly woman have my son’s seat on the bus?</td>
      <td>NTA</td>
    </tr>
  </tbody>
</table>
