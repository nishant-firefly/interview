
########################################
# 2, 3 lines of relevancy engineer 
# couple of 100 million documents
# search should come on top 
# Data is not coming on top 
# over 50 reps indexed , each api have , own data and relevancy.  
######################################## Relevance : context is difierent, for each department, API key 
                                # Pattern 
d1={1:"a", 2:"b"} 
d2 = {3:"c",4:"d", 5:"e"}

breakpoint()
dict1.update(dict2)
print(dict1) # {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}

def count_words(match_words, resume_data ):
    count_words =  {i:0 for i in match_words} #{'python': 0, 'java': 0}
    for word in  resume_data.split():
        if word in count_words:
           count_words[word] = count_words[word] +1 
    return count_words


if __name__=="__main__":
    match_texts =["python", "java"]
    test_resume_data="""

java    python ;lsdkl;kds;sldk; 
   python java  kjdshkjsk   python 
kalskjjl
   python 
"""
    print(count_words(match_texts ,test_resume_data ))