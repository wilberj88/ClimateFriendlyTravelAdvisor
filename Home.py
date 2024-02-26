import streamlit as st
import googlemaps
import gmaps
from datetime import date
from ipywidgets import embed
import streamlit.components.v1 as components
#import crewai
from crewai import Crew, Agent, Task
from textwrap import dedent
from langchain.llms import OpenAI
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

# set page layout
st.set_page_config(
    page_title="Climate Friendly Travel Advisor",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

#functions
class TripAgents():

  def city_selection_agent(self):
    return Agent(
        role='City Selection Expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)

  def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        verbose=True)

  def travel_concierge(self):
    return Agent(
        role='Amazing Travel Concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
            CalculatorTools.calculate,
        ],
        verbose=True)
    
class TripTasks():

  def identify_task(self, agent, origin, cities, interests, range):
    return Task(description=dedent(f"""
        Analyze and select the best city for the trip based 
        on specific criteria such as weather patterns, seasonal
        events, and travel costs. This task involves comparing
        multiple cities, considering factors like current weather
        conditions, upcoming cultural or seasonal events, and
        overall travel expenses. 
        
        Your final answer must be a detailed
        report on the chosen city, and everything you found out
        about it, including the actual flight costs, weather 
        forecast and attractions.
        {self.__tip_section()}

        Traveling from: {origin}
        City Options: {cities}
        Trip Date: {range}
        Traveler Interests: {interests}
      """),
                agent=agent)

  def gather_task(self, agent, origin, interests, range):
    return Task(description=dedent(f"""
        As a local expert on this city you must compile an 
        in-depth guide for someone traveling there and wanting 
        to have THE BEST trip ever!
        Gather information about  key attractions, local customs,
        special events, and daily activity recommendations.
        Find the best spots to go to, the kind of place only a
        local would know.
        This guide should provide a thorough overview of what 
        the city has to offer, including hidden gems, cultural
        hotspots, must-visit landmarks, weather forecasts, and
        high level costs.
        
        The final answer must be a comprehensive city guide, 
        rich in cultural insights and practical tips, 
        tailored to enhance the travel experience.
        {self.__tip_section()}

        Trip Date: {range}
        Traveling from: {origin}
        Traveler Interests: {interests}
      """),
                agent=agent)

  def plan_task(self, agent, origin, interests, range):
    return Task(description=dedent(f"""
        Expand this guide into a a full 7-day travel 
        itinerary with detailed per-day plans, including 
        weather forecasts, places to eat, packing suggestions, 
        and a budget breakdown.
        
        You MUST suggest actual places to visit, actual hotels 
        to stay and actual restaurants to go to.
        
        This itinerary should cover all aspects of the trip, 
        from arrival to departure, integrating the city guide
        information with practical travel logistics.
        
        Your final answer MUST be a complete expanded travel plan,
        formatted as markdown, encompassing a daily schedule,
        anticipated weather conditions, recommended clothing and
        items to pack, and a detailed budget, ensuring THE BEST
        TRIP EVER, Be specific and give it a reason why you picked
        # up each place, what make them special! {self.__tip_section()}

        Trip Date: {range}
        Traveling from: {origin}
        Traveler Interests: {interests}
      """),
                agent=agent)

  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"


class TripCrew:

  def __init__(self, origin, cities, date_range, interests):
    self.cities = cities
    self.origin = origin
    self.interests = interests
    self.date_range = date_range

  def run(self):
    agents = TripAgents()
    tasks = TripTasks()

    city_selector_agent = agents.city_selection_agent()
    local_expert_agent = agents.local_expert()
    travel_concierge_agent = agents.travel_concierge()

    identify_task = tasks.identify_task(
      city_selector_agent,
      self.origin,
      self.cities,
      self.interests,
      self.date_range
    )
    gather_task = tasks.gather_task(
      local_expert_agent,
      self.origin,
      self.interests,
      self.date_range
    )
    plan_task = tasks.plan_task(
      travel_concierge_agent, 
      self.origin,
      self.interests,
      self.date_range
    )

    crew = Crew(
      agents=[
        city_selector_agent, local_expert_agent, travel_concierge_agent
      ],
      tasks=[identify_task, gather_task, plan_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

st.title("🌎 Climate Friendly Travel Advisor📍")

with st.sidebar:
    st.header("Plan your Trip")
    st.subheader("& discuss with me 🤖")
    origin = st.text_input(
        "Origin Point 👇")
    end = st.text_input(
        "End Point 👇")
    when = st.time_input('Starts When?', value=None)
    activate = st.button("Calculate CO2 Alternatives", type="primary")
   
if activate:
    st.write("## Welcome to Trip Planner Crew")
    st.write('-------------------------------')
    location = st.text_input(
    dedent("""
      From where will you be traveling from?
    """))
    cities = st.text_input(
    dedent("""
      What are the cities options you are interested in visiting?
    """))
    date_range = st.text_input(
    dedent("""
      What is the date range you are interested in traveling?
    """))
    interests = st.text_input(
    dedent("""
      What are some of your high level interests and hobbies?
    """))
    
    trip_crew = TripCrew(location, cities, date_range, interests)
    result = trip_crew.run()
    st.write("\n\n########################")
    st.write("## Here is you Trip Plan")
    st.write("########################\n")
    st.write(result)
  
