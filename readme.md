# Final project for CS 465 - Fall 2015 UIUC
- Peixian Wang, Jerry Chen, Jon Park, Zhili Feng (Group 8)
- 
## [Live Demo](https://whorleater.github.io/CS465-Project/)
- Some dependencies only load in the demo and not locally due to security reasons
- Redesign of the Compass2G website built for UIUC


#### Images:
- [Dashboard](https://raw.githubusercontent.com/Whorleater/CS465-Project/master/images/dashboard.png)
- [Grades](https://raw.githubusercontent.com/Whorleater/CS465-Project/master/images/grades.png)
- [Mobile](https://raw.githubusercontent.com/Whorleater/CS465-Project/master/images/mobile.png)

#### Specific website notes:
- The website is fully responsive, it will load just as well on mobile as on the desktop page. 
- Entire website is color coded:
    - Light blue means Info: Minor notifications such as changes in new homeworks, office hours, etc.
    - Yellow means Warning: Homework due soon, changes in lecture days, etc
    - Red means Alert: Large exam announcements, heavily weighted homeworks, etc
- Grades page:
    - Bars at the top show your current grade, Blue means B+ to A range, Yellow means C to B range, Red means below C range.
    - First graph is your grade per assignment vs the class average for that assignment
    - Second graph is your running average grade in the class, this graph takes into account the weights of the assignments. The bars denote the cutoffs for each letter grade.
- Course info:
    - Assignments is your assignments that are due soon. Sorted by priority by default, the list will order your assignments by a priority sorting algorithm which takes into account the weights of assignments, the due dates of assignments, your current grade in the class, etc. 
    - Announcements is your announcements page for specific announcements, color-coded as above. 
    - Contact info is the contact info page for your professors and TA's. Here you can find their emails, office hours, and whatever other contact info they wish to post. 
- All the buttons on the page are functional, they either lead to specific pages or are intended to do something. The entire UI is mostly functional, only the backend doesn't exist. 
