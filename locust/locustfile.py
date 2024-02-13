from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def submit_form(self):
        form_data = {
            "names[first_name]": "John",
            "names[last_name]": "Doe",
            "country-list": "US",
            "numeric-field": "185",  # Example for Height in cm
            "numeric-field_1": "80",  # Example for Weight in kg
            "dropdown_8": "Male",  # Gender
            "dropdown_1": "Other",  # Ethnicity
            "dropdown_7": "Brown",  # Hair Color
            "dropdown_11": "Other",  # Eye Color
            "dropdown": "L",  # Shirt Size
            "numeric-field_2": "43",  # EU Foot Size
            "dropdown_2": "No",  # Smoker
            "dropdown_3": "Socially",  # Drinking Habits
            "dropdown_5": ">3000",  # Monthly Wage
            "dropdown_6": "Atheist",  # Religion
            "dropdown_9": "Heterosexual",  # Sexual Orientation
            "dropdown_10": "Liberalism",  # Political Orientation
            "terms-n-condition": "on"  # Assuming this is how you mark the checkbox as checked
        }

        # Replace "/submit-form-url" with the actual URL where the form data should be submitted.
        self.client.post("/wordpress/", data=form_data)




# from locust import HttpUser, task
# import random

# class WebsiteUser(HttpUser):
#     @task
#     def submit_form(self):
#         # Simulated form data with random selections for some fields
#         form_data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'numeric-field': str(random.randint(140, 250)),  # Random height in cm
#             'numeric-field_1': str(random.randint(30, 150)),  # Random weight in kg
#             'numeric-field_2': str(random.randint(20, 50)),  # Random shoe size
#             'dropdown': random.choice(['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']),  # Size
#             'dropdown_1': random.choice(['Black or African American', 'White (Caucasian)', 'Latino or Hispanic', 'Asian', 'Indian', 'Other']),  # Ethnicity
#             'dropdown_2': random.choice(['Yes', 'No']),  # Additional hypothetical question
#             'dropdown_3': random.choice(['Never', 'Socially', 'Regularly']),  # Social habit
#             'dropdown_5': random.choice(['0', '1 - 1000', '1001 - 2000', '2001 - 3000', '>3000']),  # Income range
#             'dropdown_6': random.choice(['Christianity', 'Islam', 'Atheist', 'Hinduism', 'Buddhism', 'Other']),  # Religion
#             'dropdown_7': random.choice(['Black', 'Blond', 'White', 'Red hair', 'Brown', 'Bald', 'Other']),  # Hair color
#             'dropdown_8': random.choice(['Male', 'Female', 'Cisgender', 'Transgender', 'Non-Binary', 'Genderfluid', 'Agender']),  # Gender
#             'dropdown_9': random.choice(['Heterosexual', 'Homosexual', 'Bisexual', 'Pansexual', 'Asexual', 'Other']),  # Sexual orientation
#             'dropdown_10': random.choice(['Conservatism', 'Liberalism', 'Socialism', 'Libertarianism', 'Communism', 'Capitalism', 'Other']),  # Political orientation
#             'dropdown_11': random.choice(['Blue', 'Black', 'Green', 'Yellow', 'Other']),  # Favorite color
#             'country-list': random.choice(['US', 'CA', 'GB', 'DE', 'FR', 'ES', 'PT', 'IT', 'BR', 'IN']),  # Country, simplified selection
#         }

#         # Sending the POST request with the form data
#         # Make sure to replace "/form-submission-url" with the actual URL where the form submits
#         response = self.client.post("/wordpress/", data=form_data)
        
#         # Optionally, print the status code to see if the form was submitted successfully
#         print(f"Form submitted with status code: {response.status_code}")
