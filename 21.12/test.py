import pickle

student_info = [{'id': 20200000,'name': 'Nguyen Van A','score': { 'math': 7.8,'english': 8.9,'physics': 9.0,}},{'id': 20200001,'name': 'Le Van B','score': {'math': 9.8,'english': 8.7,'physics': 7.6,}}]
with open('student_info.pkl', 'wb') as f:
    pickle.dump(student_info, f)