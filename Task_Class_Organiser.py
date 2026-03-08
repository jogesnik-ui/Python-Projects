class Task:
    def __init__ (self, subject, description, date):
        self.subject = subject
        self.description = description 
        self.date = date

    def summary(self):
        return(f"Subject {self.subject}, Description {self.description}, Date {self.date}")
    
t1 = Task("Maths", "All of Chapter 1L", "Tommorrow")
t2 = Task("English", "Reading Analysis", "Thursday")

print(t1.summary())
print(t2.summary())
        
