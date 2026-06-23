# Unified-GenAI-Platform 

Command to run: python -m streamlit run app/main.py

## Text AI: 
- Ask anything. 
- Its able to answer/respond in the context of last 10 messages.
- Persists chat history, until the page is refreshed


## Image Generation
- Generates any image for the given prompt
- Persists history, until the page is refreshed

## Meeting assistant
- Accepts .mp4, WAV file formats (Meeting recordings)
- Generates meeting transcription, insights, summary, key points, action items and list of attendees 
- Answers queries in the context of the meeting

## Excel (data) Analytics
- Accepts excel files and reads the content
- Respond to user prompts in the context of file data
- Able to generate visuals (graphs, charts) if possible
- Persists history, until the page is refreshed

## Image to Text
- Accepts JPG, PNG file formats
- Extracts the text out of image and generates image discription
- Persists history, until the page is refreshed

## Database Search
- Receives user prompt and search the database
- This module uses LangChain
- To create the database, please execute this command: python helpers/createSQLiteDB.py

### Example prompts
- Total revenue
- Average revenue per customer
- Top 5 customers
- Revenue by month

## Relational Database Search 
- Receives user prompt and search the database
- Translates the user prompt into SQL query and then execute it
- Translate the query result in business language
- To create the database, please execute this command: python helpers/createSQLiteMultipleTableDB.py

### Example prompts
- Top 5 customers by revenue
- Revenue by product category
- Best selling product
- Sales by city
- Monthly sales trend


