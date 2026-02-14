Milestone 1 – User Authentication System
📌 Project Title
PolicyNav – User Authentication System (Milestone 1)

📖 Description
In this milestone, we developed a complete user authentication system for the PolicyNav application using Streamlit and SQLite.
The system allows users to:
Create a new account with validation
Login securely
Access a Dashboard after successful login
Recover password using security questions
Logout securely and return to the home screen
Navigation is handled using Streamlit session state to simulate multi-page routing within a single application

✅ Features Implemented
🔹 User Signup with input validation
🔹 Login authentication using SQLite database
🔹 Dashboard redirection after successful login
🔹 Welcome message displaying logged-in username
🔹 Logout functionality
🔹 Forgot Password using security question verification
🔹 Background UI styling with custom design
🔹 Navigation between pages (Home, Signup, Login, Dashboard, Forgot Password)

⚙️ Technologies Used
Python
Streamlit
SQLite3
Base64 (for background image rendering)

▶️ How to Run the Application
Step 1: Install Required Dependencies
pip install streamlit
pip install pyjwt

Step 2: Navigate to the Project Folder
cd milestone1

Step 3: Run the Streamlit Application
streamlit run app.py

Step 4: Run ngrok
pip install pyngrok
from pyngrok import ngrok
ngrok.connect(8501)

📸 Screenshots
🔹Home Page
<img width="1917" height="911" alt="Screenshot 2026-02-14 112654" src="https://github.com/user-attachments/assets/40d92d0a-07bf-44e8-b134-2b3bc9edf521" />

🔹 Signup Page
<img width="1919" height="901" alt="Screenshot 2026-02-14 112958" src="https://github.com/user-attachments/assets/5befd41c-158b-43b6-b871-6f1142dcc843" />

🔹 Login Page
<img width="1919" height="900" alt="Screenshot 2026-02-14 113024" src="https://github.com/user-attachments/assets/da3f8c66-7148-4b49-847a-32cc7eb25781" />

🔹 Dashboard Page
<img width="1919" height="902" alt="Screenshot 2026-02-14 113040" src="https://github.com/user-attachments/assets/036679ae-fb3c-4ced-a667-bc72675f80ed" />

🔹 Forgot Password Page
<img width="1919" height="907" alt="Screenshot 2026-02-14 113113" src="https://github.com/user-attachments/assets/112c6472-bc4f-440e-b95a-20a3346feda6" />

🎯 Milestone 1 Outcome
By completing this milestone, we successfully built a fully functional authentication system with:
Secure login flow
Proper user session handling
Multi-page navigation structure
Clean and interactive UI

This forms the foundation for further development of the PolicyNav application.
