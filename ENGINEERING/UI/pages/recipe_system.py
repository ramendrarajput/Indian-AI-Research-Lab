import streamlit as st
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector
from phi.tools.exa import ExaTools
from phi.agent import Agent
from ENGINEERING.UI.pages.research_system import ra    
def recipe_agent():
    db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

    knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://www.poshantracker.in/pdf/Awareness/MilletsRecipeBook2023_Low%20Res_V5.pdf",
        "https://www.cardiff.ac.uk/__data/assets/pdf_file/0003/123681/Recipe-Book.pdf",
    ],
    vector_db=PgVector(table_name="recipes", db_url=db_url),  # we are using PgVector here, you can also use other vector dbs
 )
    knowledge_base.load(recreate=False)
    return Agent(
    name="RecipeGenie",
    knowledge_base=knowledge_base,
    search_knowledge=True,
    tools=[ExaTools()],
    markdown=True,
    instructions=[
        "Search for recipes based on the ingredients and time available from the knowledge base.",
        "Include the exact calories, preparation time, cooking instructions, and highlight allergens for the recommended recipes.",
        "Always search exa for recipe links or tips related to the recipes apart from knowledge base.",
        "Provide a list of recipes that match the user's requirements and preferences.",
    ],
)

def recipe_system():
    user_query = st.text_area(
         "Give me detail about the recipe you want",
         placeholder="Ask any kind of recipe. The AI agent will analyze and gather additional context if needed.",
         help="Provide detailed information of the recipe you want. Ex.I have potatoes, tomatoes, onions, garlic, ginger, and chicken. Suggest me a quick recipe for dinner"
     )
    if st.button("🔍 Generate recipe", key="Generate_Recipe_button"):
         if not user_query:
             st.warning("Provide detailed information of the recipe you want")
         else:
             try:
                 with st.spinner("Processing and gathering insights..."):
                     # call the agent
                     
                     # Prompt generation for analysis
                     analysis_prompt = (
                         f"""
                         You are a Smart Recipe Maker Agent System of Ramendra. You are an expert in making Recipe and continuouly being trained to perform task like an agent. You are a part of multi model language model, trained and fine-tuned on massive amount of data by Ramendra Singh Rajput, working for Mp govt as a patwari.He is the team leader of google AI expert engineers those developed you. He is an Artificial intelligence expert, Machine learning and Deep learning engineer,also developing Health Expert System, Music Expert System, and developing a powerful ecosystem drived by Multi AI Agents.He is having google developer profile.His education and qualification is master of computer application.Machine learning, Deep learning and Generative AI certified developer.Keen in making corelation between philosophy and quantom physics.His email id is ramendra.rajput85@gmail.com, linkedin id is https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/ , github id is https://github.com/ramendrarajput, Google developer profile is https://g.dev/ramendrarajput. Always put these profile links at the and of Analysis report.
                         Search the web for content and context.
                         Respond to the following query using insights and supplementary web research:
                         {user_query}
 
                         Provide a detailed, user-friendly, and actionable response.
                         """
                     )
 
                     # AI agent processing
                     response =  ra.run(analysis_prompt)
                     #response = multimodal_Agent.run(analysis_prompt)
 
                 # Display the result
                 st.subheader("Your Recipe:")
                 st.markdown(response.content)
 
             except Exception as error:
                 st.error(f"An error occurred during analysis: {error}")
             #finally:
                 # Clean up temporary video file
                 #Path(video_path).unlink(missing_ok=True)
    else:
     st.info("Provide detailed information of the recipe you want.")

 # Customize text area height
    st.markdown(
     """
     <style>
     .stTextArea textarea {
         height: 100px;
     }
     </style>
     """,
     unsafe_allow_html=True
 )  

