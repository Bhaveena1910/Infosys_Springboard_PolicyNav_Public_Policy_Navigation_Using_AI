📌 Project Title: PolicyNav – OTP Authentication & Readability Metrics (Milestone 2)
📖 Description

In Milestone 2, we enhanced the PolicyNav application by integrating advanced security features and intelligent policy analysis capabilities.

This milestone builds upon the authentication system from Milestone 1 and introduces:

Secure password hashing using bcrypt

Email-based password reset mechanism

Policy document upload (PDF)

Text readability analysis

Word Cloud visualization

Data analytics dashboard with interactive charts

The application is now more secure, data-driven, and interactive.

✅ Features Implemented: 
🔐 Security Enhancements

Password hashing using bcrypt

Secure database (policy_secure_final.db)

Email-based password reset using OTP/token

Strong password validation using regex

Session-based authentication handling

📄 Policy Document Processing

Upload policy documents in PDF format

Extract text using PyPDF2

Analyze readability using textstat

Generate:

Readability Score

Grade Level

Reading Ease

☁️ Word Cloud Visualization

Automatically generates Word Cloud from uploaded policy text

Highlights frequently used terms

Built using WordCloud and Matplotlib

📊 Analytics Dashboard

Interactive charts using Plotly

Policy insights visualization

Data tracking with Pandas

Real-time dashboard updates

📧 Email Integration

Secure password reset via email

Token-based verification system

SMTP integration for sending emails

⚙️ Technologies Used

Python

Streamlit

SQLite3

bcrypt (Password Hashing)

PyPDF2 (PDF Text Extraction)

textstat (Readability Analysis)

WordCloud

Matplotlib

Plotly

Pandas

SMTP (Email Services)

Pyngrok (Public Deployment)

▶️ How to Run the Application

Step 1: Install Dependencies

pip install streamlit bcrypt textstat wordcloud matplotlib pandas plotly PyPDF2 pyngrok


Step 2: Navigate to Project Folder

cd milestone2


Step 3: Run the Streamlit Application

streamlit run app.py


Step 4: Expose the App Publicly 

from pyngrok import ngrok

ngrok.set_auth_token("YOUR_NGROK_TOKEN")
ngrok.connect(8501)


📸 Screenshots

🔹 Home Page
<img width="1915" height="766" alt="Screenshot 2026-03-04 191509" src="https://github.com/user-attachments/assets/c5cfa022-9455-4b1a-8d1a-a57a96904893" />

🔹 User Registration
<img width="1919" height="828" alt="Screenshot 2026-03-04 192707" src="https://github.com/user-attachments/assets/af8bd09a-2732-4aa6-aacc-9f60d0ca4d0d" />

🔹 User Login
<img width="1901" height="761" alt="Screenshot 2026-03-04 191702" src="https://github.com/user-attachments/assets/da061e8d-fc9f-4548-9258-c58af4601d2d" />

🔹 User Dashboard
<img width="1919" height="851" alt="Screenshot 2026-03-04 192441" src="https://github.com/user-attachments/assets/39d274fe-9264-418c-9a5b-b32df7399648" />

🔹 Readability Analytics Dashboard
<img width="1919" height="806" alt="Screenshot 2026-03-04 192510" src="https://github.com/user-attachments/assets/8f6ace66-7511-4753-902c-2986c7964f8e" />
<img width="1910" height="278" alt="Screenshot 2026-03-04 192536" src="https://github.com/user-attachments/assets/3a9b71f5-d8cc-4bb0-86bd-fbc58d3bdc60" />


🔹 Word Cloud Visualization
<img width="1918" height="826" alt="Screenshot 2026-03-04 192525" src="https://github.com/user-attachments/assets/1e61d27f-6b8e-40d1-8dcf-a4fb73493403" />

🔹 Password Reset Email Flow
<img width="1897" height="807" alt="Screenshot 2026-03-04 192402" src="https://github.com/user-attachments/assets/98f9d652-bfdc-4467-a56a-b07609c41f4b" />

🔹 Failed Login
<img width="1914" height="762" alt="Screenshot 2026-03-04 192756" src="https://github.com/user-attachments/assets/7a5e5023-9ba0-4655-aeb7-338b0ab6710e" />

🔹 Admin Login
<img width="1870" height="717" alt="Screenshot 2026-03-04 192831" src="https://github.com/user-attachments/assets/19f5985d-d354-43a8-bfef-f9b38dfa7473" />

🔹 Admin Dashboard
<img width="1891" height="743" alt="Screenshot 2026-03-04 192853" src="https://github.com/user-attachments/assets/3489b79d-896c-4373-b79a-c7589170463a" />



🎯 Milestone 2 Outcome

By completing this milestone, we successfully transformed PolicyNav into a:

🔐 Secure and production-ready authentication system

📄 Intelligent policy analysis platform

📊 Data-driven dashboard application

📧 Email-integrated secure system

This milestone significantly improves both security and functional intelligence, making PolicyNav scalable for real-world deployment.
