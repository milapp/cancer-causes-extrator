# cancer-causes-extrator
Dependency parsing based approach to extract multi-word causes of cancer from social media posts.  

Implemented 2 approaches. 

1. Naive rule based approach. 
   
   Defined rules like "X cause cancer" and tried to match sentences to that. 
   
   Successfully, captured single word causes that are near to the causal word (i.e. causes, will lead to, etc)
   
   This approach did not capture multiword and causes that occur far away from causal word. 

2. Implemented dependency parse based method. 
   
   Used StanfordNLP to get dependency parse of the sentence. 
   
   This captures dependencies that are far from the word. 
   
   Successfully, captured multiword causes and also words that are far from causal word. 
   
   Example: **The ultra violet radiations causes cancer.** 
   
   Captured Cause: **"The ultra violet radiations"**
