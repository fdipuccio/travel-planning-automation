import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool
)





@CrewBase
class TravelPlannerProMallorcaFamilyAutomationCrew:
    """TravelPlannerProMallorcaFamilyAutomation crew"""

    
    @agent
    def travel_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["travel_research_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def travel_itinerary_coordinator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["travel_itinerary_coordinator"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def calendar_event_manager(self) -> Agent:
        
        return Agent(
            config=self.agents_config["calendar_event_manager"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "google_calendar/create_event",
                    ],
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def hotel_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["hotel_research_specialist"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def restaurant_budget_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["restaurant_budget_analyst"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def travel_report_compiler(self) -> Agent:
        
        return Agent(
            config=self.agents_config["travel_report_compiler"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def research_destination_attractions(self) -> Task:
        return Task(
            config=self.tasks_config["research_destination_attractions"],
            markdown=False,
            
            
        )
    
    @task
    def find_family_hotels(self) -> Task:
        return Task(
            config=self.tasks_config["find_family_hotels"],
            markdown=False,
            
            
        )
    
    @task
    def research_restaurants_and_calculate_budget(self) -> Task:
        return Task(
            config=self.tasks_config["research_restaurants_and_calculate_budget"],
            markdown=False,
            
            
        )
    
    @task
    def create_complete_itinerary(self) -> Task:
        return Task(
            config=self.tasks_config["create_complete_itinerary"],
            markdown=False,
            
            
        )
    
    @task
    def generate_final_travel_report(self) -> Task:
        return Task(
            config=self.tasks_config["generate_final_travel_report"],
            markdown=False,
            
            
        )
    
    @task
    def create_all_travel_calendar_events(self) -> Task:
        return Task(
            config=self.tasks_config["create_all_travel_calendar_events"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the TravelPlannerProMallorcaFamilyAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


