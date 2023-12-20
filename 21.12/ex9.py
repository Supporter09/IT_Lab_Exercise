import pickle
from shutil import copyfile
copyfile('C:/Users/Admin/Desktop/Code/IT_Lab_Exercise/21.12/student_info.pkl', 'updated_info.pkl')
def add_student_info(file_path, student_id, new_student_info):

    ##################
    # YOUR CODE HERE #
    ##################    
    try:
        # Load existing student information from the file
        with open(file_path, 'rb') as file:
            student_info = pickle.load(file)

        # Check if the student ID already exists in the list
        for i, student in enumerate(student_info):
            if student['id'] == student_id:
                # Update the information if the student ID is found
                student_info[i] = new_student_info
                break
        else:
            # If the student ID is not found, add the new information
            student_info.append(new_student_info)

        # Write the updated information back to the file
        with open(file_path, 'wb') as file:
            pickle.dump(student_info, file)

        print(f"Student information for ID {student_id} updated successfully.")

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'C:/Users/Admin/Desktop/Code/IT_Lab_Exercise/21.12/student_info.pkl'

# Example student information to add/update
new_student_info = {
    'id': 20200002,
    'name': 'Tran Thi C',
    'score': {
        'math': 8.5,
        'english': 9.2,
        'physics': 7.0,
    }
}

# Update the student information in the file
add_student_info(file_path, new_student_info['id'], new_student_info)