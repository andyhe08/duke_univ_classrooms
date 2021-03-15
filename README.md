# duke_univ_classrooms

#### Motivation: 
In the midst of COVID, I wanted to find areas to study outside of my dorm, but as Duke began closing more locations, I needed a ***new systematic way to find private spaces***.

#### Concept:
A common area for students to study is in classrooms. However, most classrooms are locked in accordance with COVID policy. I noticed that if a classroom had an in-person class, that classroom would have to be unlocked for the entire day. Thus, if I were able to identify all of the in-person classes and their respective locations, I could find a variety of locations to study when the classrooms are unoccupied. Duke’s DukeHub system does not have a way to sort by in-person classes in an organized way, thus I needed to create a ***custom algorithm*** to systematically find classrooms that are open.

#### Solution:
To do this, I accessed the Duke Internal API to import all of the class data as a JSON into Python. I noticed, however, that each of the course numbers (which is used in the Duke System) seemed random. So, I had to loop through each subject code to find all possible classes. Then, I had to see which of those classes were being offered and stored each in-person offering as a row in a csv file. After creating this csv, I was able to convert it to excel and sort the list by classroom, time, and date, thus showing me where and when I can study. 

#### Results:
Through this project, I have been able to find and utilize many classrooms that I would have never found normally.  Because of my custom algorithm, I was able to obtain and store this information in a user-friendly manner. This has allowed me to be able leave my dorm and be certain that I will have somewhere to go study. (in accordance to COVID guidelines, of course)
